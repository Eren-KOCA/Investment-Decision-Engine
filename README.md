# 📈 Yatırım Karar Destek Motoru (Investment Decision Engine)

Bu proje, **Marmara Üniversitesi Mekatronik Mühendisliği** öğrencisi olarak, finansal matematiğin temel prensiplerini Python ile dijitalleştirmek amacıyla geliştirdiğim bir araçtır. Özellikle **SPL 1009 (Sermaye Piyasası Faaliyetleri)** sınavı hazırlık sürecinde öğrendiğim "Paranın Zaman Değeri" (Time Value of Money) kavramını pratik bir uygulamaya dönüştürür.

## 🚀 Proje Ne İşe Yarar?
Bu yazılım, bir ekipman veya ürün alırken karşılaşılan **"Peşin mi almalıyım yoksa taksitli/kiralama mı yapmalıyım?"** ikilemini matematiksel olarak çözer.

### Temel Özellikler:
- **Bugünkü Değer (PV) Analizi:** Gelecekteki tüm nakit çıkışlarını (taksit, bakım masrafı vb.) bugünkü değerine indirger.
- **Zaman Birimi Senkronizasyonu:** Yıllık faiz oranları ile aylık taksit ödemeleri arasındaki uyuşmazlığı finansal matematik kurallarına göre otomatik olarak düzeltir.
- **Maliyet Karşılaştırması:** İki farklı senaryoyu (örneğin Peşin Alım vs. Kira) kıyaslayarak en düşük maliyetli (en karlı) seçeneği kullanıcıya önerir.

## 🛠️ Teknik Detaylar
- **Dil:** Python 3.x
- **Kütüphaneler:** Standart Python kütüphaneleri kullanılmıştır.
- **Finansal Model:** İskonto edilmiş nakit akışları (DCF) mantığı üzerine kurulmuştur.

## 📝 Kullanım Örneği
Program çalıştırıldığında kullanıcıdan şu verileri ister:
1. Beklenen yıllık faiz/getiri oranı.
2. Peşin alım senaryosu için maliyetler ve bakım yılları.
3. Taksitli alım senaryosu için peşinat, taksit tutarı ve vade süresi.

Sonuç olarak program, her iki seçeneğin **Net Bugünkü Değeri (NPV)** üzerinden hangisinin daha avantajlı olduğunu TL cinsinden raporlar.

---
*Bu proje finansal okuryazarlık ve yazılım geliştirme becerilerini birleştirmek için hazırlanmış bir eğitim çalışmasıdır.*
