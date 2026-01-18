# 🤖 Smart Navigation: Yol Planlama Simülatörü

* **Proje Amacı:** Bir robotun; farklı trafik yoğunlukları ve engeller altında en verimli yolu bulmasını sağlayan bir simülasyon projesidir.
* **Kapsam:** En kısa yol algoritmaları (Dijkstra, Bellman-Ford) ve arama algoritmalarının (BFS, DFS) davranışlarını karşılaştırmalı olarak sunar.

## 🛠️ Kullanılan Teknolojiler

* **Python:** Algoritma mantığı ve çekirdek uygulama geliştirme.
* **Numpy:** Her çalıştırmada rastgele trafik ve engel oluşturarak **objektif simülasyon** sağlama.
* **Matplotlib:** Algoritmaların harita üzerindeki hareketlerinin anlık görselleştirilmesi.

## 🛣️ Algoritmalar ve Yaklaşımlar

### 1️⃣ Ağırlıklı (Maliyet Odaklı) Algoritmalar
Trafik yoğunluğuna göre "en ucuz" yolu hesaplarlar.

* **Dijkstra:** En düşük maliyetli rotayı kesin olarak garanti eder.
* **Bellman-Ford:** Negatif maliyetli yolları işleme yeteneğine sahiptir.
> [!WARNING]
> **Teknik Detay:** Algoritma negatif döngüleri tespit eder; ancak simülasyonun sürekliliği için bu ağırlıklar bilinçli olarak **0'a** limitlenmiştir (clamping).



### 2️⃣ Ağırlıksız (Adım Odaklı) Algoritmalar
Yolların maliyeti (trafik) yoksa, hedefe en az adımda ulaşmayı hedeflerler.

* **BFS (Breadth-First Search):** Hedefi katman katman arayarak en kısa adım sayısını bulur.
* **DFS (Depth-First Search):** Derinlemesine arama stratejisiyle hedefi bulur.
* **Simülasyon Farkı:** Robot hedefe varmadan önce, algoritmanın harita üzerinde yaptığı **"hedef arama/tarama"** süreci görsel olarak simüle edilmiştir.


## ✨ Projenin Öne Çıkan Özellikleri

* 🚀 **Dinamik Ortam:** Numpy ile her başlangıçta farklı bir trafik ve engel düzeni.
* 📊 **Görsel Analiz:** Arama stratejilerinin harita üzerinde canlı olarak izlenebilmesi.
* 🛠️ **Hata Yönetimi:** Bellman-Ford üzerinde gelişmiş negatif döngü kontrolü.


## 🖼️ Simülasyon Görselleri ve Analiz

**🟥 Bellman-Ford Algoritması** <sub>__________________________________</sub>

*Negatif maliyetlerin ve döngü kontrollerinin yapıldığı yol planlaması.*

**Hedef Arama Süreci:**  
<img src="https://github.com/user-attachments/assets/ca76b2f8-04fa-47b7-8695-44d775a6b770" width="600">


**Rotanın Tamamlanması:**  

<img src="https://github.com/user-attachments/assets/5979385d-73fb-4267-acf2-93adeecaff52" width="600">


### 🟦 Dijkstra Algoritması 
<hr>
*En düşük maliyetli rotanın (trafik yoğunluğu dahil) hesaplanma anı.*

<img src="https://github.com/user-attachments/assets/80bb056b-de3c-4dd0-bf25-c32d8bcecc78" width="49%" height="600" /> <img src="https://github.com/user-attachments/assets/f794d5c1-793a-4c26-b61c-f6c1e1f2ac76" width="49%" height="600" />


### 🟩 BFS ve DFS Karşılaştırması
*Arama stratejilerinin (katman katman vs. derinlemesine) harita üzerindeki tarama farkları.*
<br>
<img src="bfs_resim_linki" width="45%"> <img src="dfs_resim_linki" width="45%">
