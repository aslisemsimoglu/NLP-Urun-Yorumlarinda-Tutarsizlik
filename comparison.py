import pandas as pd
from transformers import pipeline
import torch

# CUDA kontrolü
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print("Kullanılan cihaz:", device)

# 1. Veri setini yükleme ve temizleme
file_path = r"C:\Users\semsi\OneDrive\Masaüstü\Urun-Yorumlarinda-Tutarsizlik-Tespiti\ecommerce_review_dataset.csv"
print("Veri seti yükleniyor...")
df = pd.read_csv(file_path)
df['title'] = df['title'].fillna('Eksik Başlık')
df = df[df['review'].notnull() & df['review'].str.strip() != '']
print(f"Veri seti başarıyla yüklendi. Yorum sayısı: {len(df)}")

# 2. Model 1: İlk Türkçe duygu analizi modeli
print("Model 1: savasy/bert-base-turkish-sentiment-cased yükleniyor...")
model_1 = pipeline(
    task="text-classification",
    model="savasy/bert-base-turkish-sentiment-cased",
    tokenizer="savasy/bert-base-turkish-sentiment-cased",
    device=0  # GPU'yu kullan
)
print("Model 1 başarıyla yüklendi.")

# 3. Model 2: Yeni Türkçe duygu analizi modeli
print("Model 2: saribasmetehan/bert-base-turkish-sentiment-analysis yükleniyor...")
model_2 = pipeline(
    task="text-classification",
    model="saribasmetehan/bert-base-turkish-sentiment-analysis",
    tokenizer="saribasmetehan/bert-base-turkish-sentiment-analysis",
    device=0  # GPU'yu kullan
)
print("Model 2 başarıyla yüklendi.")

# 4. Uzun metinleri işleyerek duygu analizi fonksiyonu
def analyze_sentiment(text, model, max_length=512):
    sentences = [text[i:i+max_length] for i in range(0, len(text), max_length)]
    sentiments = [model(sentence)[0]['label'] for sentence in sentences]
    return max(set(sentiments), key=sentiments.count)

# Duygu analizi sırasında ilerleme kaydı
print("Duygu analizi başlıyor...")
for index, row in df.iterrows():
    # Model 1: savasy/bert-base-turkish-sentiment-cased
    df.at[index, 'sentiment_model_1'] = analyze_sentiment(row['review'], model_1)
    # Model 2: saribasmetehan/bert-base-turkish-sentiment-analysis
    df.at[index, 'sentiment_model_2'] = analyze_sentiment(row['review'], model_2)

    # Her 10 yorumda bir durum bildirimi
    if (index + 1) % 10 == 0 or (index + 1) == len(df):
        print(f"{index + 1}/{len(df)} yorum işlendi...")

# 5. Sonuçları kaydetme
output_excel = "product_review_analysis_comparison.csv"
df.to_excel(output_excel, index=False, encoding="utf-8", columns=['product_id', 'title', 'review', 'star','clap','thumbsdown','sentiment', 'consistency'])
print(f"Sonuçlar {output_excel} dosyasına kaydedildi.")

