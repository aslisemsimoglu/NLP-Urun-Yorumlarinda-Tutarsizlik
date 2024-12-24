import pandas as pd
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk
import nltk
print(nltk.data.path)

nltk.data.path.append(r'C:\Users\semsi\AppData\Roaming\nltk_data')
nltk.download('punkt')
nltk.download('stopwords')


# Veri yükleme fonksiyonu
def load_data(file_path):
    print("Veri seti yükleniyor...")
    df = pd.read_csv(file_path)
    print(f"Veri seti başarıyla yüklendi. Yorum sayısı: {len(df)}")
    return df


# Veri temizleme fonksiyonu
def clean_data(df):
    print("Veri temizleme işlemi başlıyor...")

    # Eksik değer doldurma
    df['title'] = df['title'].fillna('Eksik Başlık')
    df = df[df['review'].notnull() & df['review'].str.strip() != '']

    # Yorum metinlerini temizleme
    def temizle_metin(metin):
        metin = re.sub(r'[^\w\s]', '', metin)  # Noktalama işaretlerini kaldır
        metin = re.sub(r'\d+', '', metin)  # Sayıları kaldır
        return metin.lower().strip()  # Küçük harfe çevir ve boşlukları temizle

    df['temiz_metin'] = df['review'].apply(temizle_metin)

    # Stop words çıkarımı
    turkce_stopwords = set(stopwords.words('turkish'))

    def remove_stop_words(metin):
        kelimeler = word_tokenize(metin)
        temiz_kelimeler = [kelime for kelime in kelimeler if kelime not in turkce_stopwords]
        return ' '.join(temiz_kelimeler)

    df['temiz_metin'] = df['temiz_metin'].apply(remove_stop_words)

    print("Veri temizleme işlemi tamamlandı.")
    return df
