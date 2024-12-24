# NLP Dersi Dönem Sonu Projesi  

## Ürün Yorumlarında Duygu Analizi ve Tutarlılık Tespiti  

Bu proje, bir Türkçe e-ticaret ürün yorumları veri seti üzerinde duygu analizi ve tutarlılık tespiti yapmak için geliştirilmiştir. Proje kapsamında, iki farklı Türkçe duygu analizi modeli kullanılmış ve yorumların yıldız puanları ile tutarlılığı değerlendirilmiştir.  

## Projenin Özeti  
Proje, kullanıcıların ürünlere verdikleri yorumlar ve yıldız puanları arasındaki tutarlılığı analiz etmeyi hedefler. Örneğin:  
- **Olumsuz bir yorumun** yüksek yıldız puanıyla eşleşmesi.  
- **Olumlu bir yorumun** düşük yıldız puanıyla eşleşmesi.  

Bu durumlar tespit edilip `tutarsız` olarak işaretlenir. Ayrıca sonuçlar detaylı bir şekilde analiz edilir ve kaydedilir.  

---

## Kullanılan Teknolojiler  
- **Python 3.9**  
- **NLTK (Natural Language Toolkit)**  
- **Transformers (Hugging Face)**  
- **PyTorch**  
- **Pandas**  
- **OpenPyXL**  

---

## Veri Seti  
Veri seti, e-ticaret ürün yorumlarını içermektedir ve şu sütunlardan oluşmaktadır:  
- **`product_id`**: Ürünün ID'si.  
- **`title`**: Ürün başlığı (Eksik olanlar doldurulur).  
- **`review`**: Kullanıcı tarafından yazılmış yorum.  
- **`star`**: Yıldız puanı (1-5).  
- **`clap`**: Beğeni sayısı.  
- **`thumbsdown`**: Olumsuz geri bildirim sayısı.  

### Veri Seti Linki  
Analiz sonrası hazırlanmış sonuç dosyasına [Kaggle üzerinden erişebilirsiniz](https://www.kaggle.com/datasets/aslemimolu/rn-yorumlar-nlp-analizi/data).  

---

## Proje Adımları  

### 1. Veri Setinin Yüklenmesi  
- Veri seti `Pandas` kütüphanesi ile okunur.  
- Eksik başlıklar `Eksik Başlık` değeriyle doldurulur.  
- Boş veya geçersiz yorumlar temizlenir.  

### 2. Metin Temizleme  
- Noktalama işaretleri ve sayılar kaldırılır.  
- Metinler küçük harfe dönüştürülür.  
- Türkçe stop words (önemsiz kelimeler) kaldırılır.  

### 3. Duygu Analizi  
- **Model 1**: `savasy/bert-base-turkish-sentiment-cased`  
- **Model 2**: `saribasmetehan/bert-base-turkish-sentiment-analysis`  

Yorumlar, her iki model ile analiz edilir ve sonuçlar karşılaştırılır. Uzun metinler, 512 karakterlik parçalara bölünerek analiz edilir.  

### 4. Tutarlılık Kontrolü  
- **Tutarsızlık Tespiti**:  
  - Yıldız puanı ≤ 2 ve `positive` sonuç dönen yorumlar.  
  - Yıldız puanı ≥ 4 ve `negative` sonuç dönen yorumlar.  
- Sonuçlar `tutarlı`, `tutarsız` veya `nötr` olarak işaretlenir.  

### 5. Sonuçların Kaydedilmesi  
- Tüm analiz sonuçları bir CSV dosyasına kaydedilir.  
- Tutarsız yorumlar ayrıca bir Excel dosyasına kaydedilir.  

---

## Gereksinimler ve Kurulum  

### Gerekli Kütüphaneler ve Yükleme Komutları  
Aşağıdaki komutlar, Python 3.9+ ortamında çalıştırılmalıdır.

#### 1. **Pandas**  
pip install pandas
pip install transformers
pip install torch
pip install nltk
pip install openpyxl
