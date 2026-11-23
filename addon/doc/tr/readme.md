# Nesne Dolaşımı

* Yazar: Christopher Duffley <nvda@chrisduffley.com>, originally by Joseph Lee, Cleverson Uliana and others

Tek bir tuşa basarak çeşitli NVDA nesne komutlarını gerçekleştirin; bunlar arasında dolaşma ve daha fazlası yer alır.

## Komutlar

* Control+NVDA+Sekme: Nesne Dolaşımı ayarlarında seçilen Dolaşım modları arasında geçiş yapar (ayrıntılar için aşağıya bakın).

## Ok tuşu kipleri

Bu eklenti, ok tuşlarını dört farklı yolla kullanabilmeye imkan verir:

* Klasik (veya normal kip): imleci hareket ettirmek için ok tuşlarını kullanın.
* Nesne Dolaşımı: Sonraki/önceki/üst/ilk alt nesneye gitmek için ok tuşlarını kullanın.
* Tarama Kipi: Tarama Kipi öğeleri (web dahil) arasında geçiş yapmak ve öğeler arasında gezinmek için ok tuşlarını kullanın.
* Tarama kipi: Hiyerarşiden bağımsız olarak ekrandaki nesneler arasında dolaşmak için ok tuşlarını kullanın.

Ok tuşları nesne dolaşımına ayarlandığında aşağıdaki komutlar kullanılabilir:

* Sağ ok: sonraki nesne.
* Sol ok: önceki nesne.
* Yukarı ok: üst nesne.
* Aşağı ok: ilk alt nesne.
* Aralık veya ENTER: etkinleştirin.

Tarama Kipi etkin olduğunda (öğeler varsayılan olarak (nesneye/tüm öğelere göre hareket etme), başlık, tablo, bağlantı, form alanı, liste; ek Tarama Kipi öğeleri NVDA'nın Tarama Kipi ayarları veya özel bir Nesne Dolaşımı ayarları arayüzü aracılığıyla eklenebilir (aşağıya bakınız)):

* Sağ ok: sonraki öğe.
* Sol ok: önceki öğe.
* Yukarı ok: önceki öğe türü.
* Aşağı ok: sonraki öğe türü.
* Aralık veya ENTER: etkinleştirin.

Tarama modu aktifken:

* Aşağı ok: sonraki nesne veya sonraki satır.
* Yukarı ok: önceki nesne veya önceki satır.
* Sağ ok: Sonraki karakteri incele.
* Sol ok: önceki karakter.
* Kontrol+sağ ok: sonraki kelime.
* Kontrol+sol ok: önceki kelime.
* Aralık veya ENTER: etkinleştirin.

## Nesne Dolaşımı ayarları

Nesne Dolaşımı ayarları (NVDA ayarları ekranının bir parçası) aşağıdaki ayarları içerir:

* Geçiş Yapılacak Dolaşım Modları: Control+NVDA+Sekme tuş kombinasyonunun hangi modlar arasında geçiş yapacağını seçer (nesne dolaşım, göz atma modu, tarama modu). Normal mod her zaman dahildir. Tüm modlar varsayılan olarak seçilidir. En az bir modun seçili kalması gerekir; sonuncusunun işaretini kaldırırsanız, Nesne Dolaşımı sizi uyarır ve işaretli kalmasını sağlar.
* Göz atma modu dolaşım öğeleri: Göz atma modunun hangi öğeler arasında geçiş yapacağını seçin. Nesne Dolaşımı bu ayarı yalnızca dokunmatik ekranı olmayan bilgisayarlarda ve NVDA'nın taşınabilir sürümlerinde gösterir; aksi takdirde, bu ayar NVDA'nın kendi Tarama Kipi ayarlarında bulunur.

Her eklenti sürümü arasında yapılan değişikliklerin listesi için [eklenti sürümlerine ait Sürüm Geçmişi][1] belgesine bakın.

[1]: https://github.com/ChrisDuffley/objPad/blob/master/changes.md
