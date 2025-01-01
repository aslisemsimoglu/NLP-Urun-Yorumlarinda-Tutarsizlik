# NLP Dersi Dönem Sonu Projesi Raporu

**Ad Soyad**: Aslı Şemşimoğlu  
**Öğrenci Numarası**: 212923001

----------

## Türkçe Ürün Yorumlarında Duygu Analizi ve Tutarlılık Tespiti

Bu proje, bir Türkçe e-ticaret ürün yorumları veri seti üzerinde duygu analizi ve tutarlılık tespiti yapmak için geliştirilmiştir. Amaç, yorumların yıldız puanları ile olan tutarlılığını analiz ederek sonuçları detaylı bir şekilde raporlamaktır.

----------

## Projenin Amacı 🎯

Bu proje, **Türkçe ürün yorumlarının** analizi üzerinden duygu tespiti ve yıldız puanlarıyla tutarlılığın kontrol edilmesini amaçlamaktadır. Kullanıcı memnuniyetini ve yorumlardaki ortak ifadeleri incelemek için çeşitli NLP teknikleri kullanılmıştır.

----------

## Veri Seti Tanımı 📊

**Veri Seti Adı**: Turkish Product Review Dataset  
**Sütunlar:**

-   **`product_id`**: Ürüne özgü kimlik numarası
-   **`title`**: Yorum başlığı
-   **`review`**: Kullanıcı yorumu
-   **`star`**: Yıldız puanı (1-5)
-   **`clap`**: Beğeni sayısı
-   **`thumbsdown`**: Olumsuz geri bildirim sayısı

**Toplam Veri:** 430,916 yorum

----------

## Projede Yapılanlar ✅

-   **Veri Temizleme ve Ön İşleme**
    
    -   Eksik başlıklar "Eksik Başlık" ile dolduruldu ✅
    -   Yorum metinlerinden gereksiz karakterler ve stop words temizlendi ✅
-   **Kelime Bulutu Analizi**
    
    -   Temizlenmiş yorumlardan kelime bulutları oluşturuldu ✅
-   **Duygu Analizi**
    
    -   `savasy/bert-base-turkish-sentiment-cased` modeli kullanılarak olumlu, olumsuz ve nötr sınıflandırma yapıldı ✅
-   **Tutarlılık Tespiti**
    
    -   Yıldız puanları ile duygu sonuçlarının uyumu kontrol edildi ✅
    -   Tutarsız yorumlar belirlendi ve ayrı bir dosyada kaydedildi ✅
-   **Model Eğitimi**
    
    -   Yorumlar üzerinde fine-tuning işlemi başarıyla tamamlandı ✅

----------

## Sonuç ve Özet 🌟

Proje kapsamında, Türkçe ürün yorumları analiz edilmiştir. Yıldız puanlarıyla uyumlu olmayan yorumlar tespit edilmiştir.

----------

## Projeyi İnceleyin 🔍

Proje ile ilgili tüm kodları ve detayları içeren Kaggle notebook'una aşağıdaki bağlantıdan ulaşabilirsiniz:  
[**NLP Proje - Ürün Yorumları**](https://www.kaggle.com/code/aslemimolu/nlp-proje-r-n-yorumlar)

Tıklayarak notebook'u doğrudan inceleyebilir ve kodları çalıştırabilirsiniz.
