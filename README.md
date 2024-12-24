# NLP Dersi Dönem Sonu Projesi

## Türkçe Ürün Yorumlarında Duygu Analizi ve Tutarlılık Tespiti

Bu proje, bir Türkçe e-ticaret ürün yorumları veri seti üzerinde duygu analizi ve tutarlılık tespiti yapmak için geliştirilmiştir. Amaç, yorumların yıldız puanları ile olan tutarlılığını analiz ederek sonuçları detaylı bir şekilde raporlamaktır.

---

## Kullanılan Teknolojiler
- Python 3.9+
- Transformers (Hugging Face)
- PyTorch
- NLTK
- Pandas
- OpenPyXL

---

## Veri Seti
Proje, Türkçe ürün yorumlarını içeren **430.916 satırlık** bir veri seti üzerinde çalışmaktadır. Veri seti şu sütunları içerir:
- `product_id`: Ürünün kimlik numarası.
- `title`: Yorum başlığı (eksik olanlar doldurulmuştur).
- `review`: Kullanıcı yorumu metni.
- `star`: Yıldız puanı (1-5).
- `clap`: Beğeni sayısı.
- `thumbsdown`: Olumsuz geri bildirim sayısı.

Kaggle bağlantıları:
- [Product Review Analysis](https://www.kaggle.com/datasets/aslemimolu/product-review-analysis)
- [Product Review Analysis Comparison](https://www.kaggle.com/datasets/aslemimolu/product-review-analysis-comparison)
- [Tutarsız Yorumlar](https://www.kaggle.com/datasets/aslemimolu/tutarsiz-yorumlar)

---

## Proje Aşamaları
1. **Veri Temizleme**:
   - Eksik başlıklar dolduruldu.
   - Geçersiz veya boş yorumlar temizlendi.
   - Noktalama işaretleri, sayılar ve Türkçe stop words kaldırıldı.

2. **Duygu Analizi**:
   - `savasy/bert-base-turkish-sentiment-cased` ve `saribasmetehan/bert-base-turkish-sentiment-analysis` modelleri kullanılarak yorumlar sınıflandırıldı.
   - Uzun metinler bölünerek analiz edildi.

3. **Tutarlılık Tespiti**:
   - Duygu analizi sonuçları ile yıldız puanları karşılaştırılarak yorumlar **tutarlı**, **tutarsız** veya **nötr** olarak işaretlendi.

4. **Sonuçların Kaydedilmesi**:
   - Genel analiz sonuçları `product_review_analysis.csv` dosyasına kaydedildi.
   - Tutarsız yorumlar ayrı bir Excel dosyasına (`tutarsiz_yorumlar.xlsx`) aktarıldı.

---
