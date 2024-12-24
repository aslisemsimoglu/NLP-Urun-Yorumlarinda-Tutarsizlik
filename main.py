import pandas as pd
from transformers import pipeline
import torch

# CUDA kontrolü
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print("Kullanılan cihaz:", device)

# CUDA belleği başlangıç kontrolü
if torch.cuda.is_available():
    print(f"Toplam GPU bellek (MB): {torch.cuda.get_device_properties(0).total_memory / 1024 / 1024}")
    print(f"Kullanılan GPU bellek (MB): {torch.cuda.memory_allocated() / 1024 / 1024}")
else:
    print("CUDA desteklenmiyor, işlem CPU ile devam ediyor.")

# 1. Veri setini yükleme ve temizleme
file_path = r"C:\Users\semsi\OneDrive\Masaüstü\Urun-Yorumlarinda-Tutarsizlik-Tespiti\ecommerce_review_dataset.csv"
print("Veri seti yükleniyor...")
df = pd.read_csv(file_path)
df['title'] = df['title'].fillna('Eksik Başlık')
df = df[df['review'].notnull() & df['review'].str.strip() != '']
print(f"Veri seti başarıyla yüklendi. Yorum sayısı: {len(df)}")

# 2. Modeli yükleme (GPU'ya taşındı)
print("Sentiment modeli yükleniyor...")
sentiment_model = pipeline(
    task="text-classification",
    model="savasy/bert-base-turkish-sentiment-cased",
    tokenizer="savasy/bert-base-turkish-sentiment-cased",
    device=0  # GPU'yu kullan
)
print("Model başarıyla yüklendi ve GPU'ya taşındı.")

# 3. Uzun metinleri işleyerek duygu analizi
def analyze_sentiment_with_split(text, max_length=512):
    sentences = [text[i:i+max_length] for i in range(0, len(text), max_length)]
    sentiments = [sentiment_model(sentence)[0]['label'] for sentence in sentences]
    # CUDA bellek durumu
    if torch.cuda.is_available():
        print(f"Kullanılan GPU bellek (MB): {torch.cuda.memory_allocated() / 1024 / 1024}")
    return max(set(sentiments), key=sentiments.count)

# Duygu analizi sırasında ilerleme kaydı
print("Duygu analizi başlıyor...")
for index, row in df.iterrows():
    df.at[index, 'sentiment'] = analyze_sentiment_with_split(row['review'])
    if index % 10 == 0:  # Her 10 yorumda bir durum bildirimi
        print(f"{index + 1}/{len(df)} yorum işlendi...")

# 4. Tutarlılık kontrolü
def check_consistency(row):
    if row['sentiment'] == "positive" and row['star'] <= 2:
        return 0  # Tutarsız
    elif row['sentiment'] == "negative" and row['star'] >= 4:
        return 0  # Tutarsız
    elif row['sentiment'] == "neutral":
        return 2  # Ne Tutarlı Ne Tutarsız
    else:
        return 1  # Tutarlı

print("Tutarlılık kontrolü yapılıyor...")
df['consistency'] = df.apply(check_consistency, axis=1)

# 5. Sonuçları kaydetme
output_file = "product_review_analysis.csv"
df.to_csv(output_file, index=False, encoding="utf-8")
print(f"Sonuçlar {output_file} dosyasına kaydedildi.")
