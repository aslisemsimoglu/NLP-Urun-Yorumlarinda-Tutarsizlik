import pandas as pd
import re

# 1. Veri setini yükleme
file_path = "product_review_analysis.csv"
df = pd.read_csv(file_path)

# 2. Tutarsız olanları filtreleme
tutarsiz_veriler = df[df['consistency'] == 0].copy()  # Kopya oluşturarak SettingWithCopyWarning'u önle

# 3. Geçersiz karakterleri temizleme
def remove_illegal_characters(text):
    if isinstance(text, str):  # Sadece metinlere uygula
        # Unicode kontrol karakterlerini temizler
        return re.sub(r"[\x00-\x1F\x7F-\x9F]", "", text)
    return text

# Tüm metin sütunlarına temizleme işlemi uygula
columns_to_clean = ['title', 'review']
for column in columns_to_clean:
    tutarsiz_veriler.loc[:, column] = tutarsiz_veriler[column].apply(remove_illegal_characters)

# 4. Excel dosyasına kaydetme
output_excel = "tutarsiz_yorumlar.xlsx"
tutarsiz_veriler.to_excel(output_excel, index=False, columns=['product_id', 'title', 'review', 'star','clap','thumbsdown','sentiment', 'consistency'])
print(f"Tutarsız veriler başarıyla {output_excel} dosyasına kaydedildi.")
