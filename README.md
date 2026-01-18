# Smart Navigation: Yol Planlama Simülatörü
- Smart Navigation, bir robotun farklı trafik yoğunlukları ve engeller altında en verimli yolu bulmasını sağlayan bir simülasyon projesidir. <br>
- Proje, en kısa yol algoritmalarının (Dijkstra, Bellman-Ford) ve arama algoritmalarının (BFS, DFS) davranışlarını karşılaştırmalı olarak sunar. <br>

<h2> 🛠️ Kullanılan Teknolojiler </h2>
<br> Python: Algoritma mantığı ve uygulama geliştirme.
<br> Numpy: Her çalıştırmada rastgele trafik yoğunluğu ve engel oluşturma (Objektif simülasyon).
<br> Matplotlib: Algoritmaların harita üzerindeki hareketlerinin görselleştirilmesi.

<h2>🛣️ Algoritmalar ve Yaklaşımlar </h2>
1) Ağırlıklı (Maliyet Odaklı) Algoritmalar
Trafik yoğunluğuna göre "en ucuz" yolu hesaplarlar.
- <h4> Dijkstra: </h4> En düşük maliyetli rotayı garanti eder.
- <h4> Bellman-Ford: </h4>  Negatif maliyetli yolları işleyebilir.
    - ⚠️ Not: Algoritma negatif döngüleri tespit eder; ancak simülasyonun çökmemesi için bu ağırlıklar bilinçli olarak 0'a             limitlenmiştir.

2) <h2> Ağırlıksız (Adım Odaklı) Algoritmalar </h2>
Yolların ağırlığı (trafik) yoksa en az adımda hedefe ulaşmayı sağlarlar.
- BFS (Breadth-First Search): En kısa adım sayısını bulur ve hedefi katman katman arar.
- DFS (Depth-First Search): Derinlemesine arama yaparak hedefi bulur.
    -Simülasyon Farkı: Robotun hedefe varmasından önce, harita üzerinde hedefi nasıl "taradıkları" görsel olarak simüle           edilmiştir.

✨ Projenin Öne Çıkan Özellikleri
- Dinamik Ortam: Numpy sayesinde her seferinde farklı bir trafik ve engel düzeni oluşur.
- Görsel Analiz: Algoritmaların harita üzerindeki arama stratejileri canlı olarak izlenebilir.
- Hata Yönetimi: Bellman-Ford üzerinde negatif döngü kontrolü (clamping) uygulanmıştır.
- 
![Ekran görüntüsü 2026-01-18 115129](https://github.com/user-attachments/assets/5979385d-73fb-4267-acf2-93adeecaff52)
![Ekran görüntüsü 2026-01-18 115157](https://github.com/user-attachments/assets/ca76b2f8-04fa-47b7-8695-44d775a6b770)


<h1>Dijkstra Algoritması</h1> 
<img src="https://github.com/user-attachments/assets/80bb056b-de3c-4dd0-bf25-c32d8bcecc78" width="49%" height="600" /> <img src="https://github.com/user-attachments/assets/f794d5c1-793a-4c26-b61c-f6c1e1f2ac76" width="49%" height="600" />


