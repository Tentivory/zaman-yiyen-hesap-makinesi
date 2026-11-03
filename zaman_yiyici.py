#!/usr/bin/env python3
# Zaman Yiyen Hesap Makinesi
# Bu kod gerçekten çalışır ama zamanı yer. Absürt seviyede.

import time
import random
import base64

def zaman_ye(saniye):
    print(f"🐋 Zaman yiyiliyor... {saniye} saniye bekleniyor. Kahve molası mı verdin?")
    time.sleep(saniye)

def hesapla(a, b, islem):
    print("🤔 Hesaplama başlıyor... ama acele etmeyin, evrenin yasalarına göre yavaş olmalı.")
    zaman_ye(random.randint(1, 3))
    print("📝 Formüller kontrol ediliyor... üst makamlardan onay bekleniyor...")
    zaman_ye(random.randint(2, 5))
    
    # Gizli siyasi anlam (base64 ile saklı): her hesaplama bir mini bürokrasi simülasyonu
    gizli = base64.b64decode("YnVyb2tyYXNpIHl1enVuZGVuIGhlciBzZXkgeWF2YXMgZ2lkaXlvcg==").decode('utf-8')
    # print(gizli)  # Açmak isterseniz yorumu kaldırın
    
    if islem == "+":
        sonuc = a + b
        mesaj = "Toplama işlemi, evrenin en basit ama en yavaş mucizesi."
    elif islem == "-":
        sonuc = a - b
        mesaj = "Çıkarma, kayıpların matematiği."
    elif islem == "*":
        sonuc = a * b
        mesaj = "Çarpma, çoğalmanın absürt dansı."
    elif islem == "/":
        if b == 0:
            print("😱 Sıfıra bölme? Bu, varoluşsal bir kriz!")
            zaman_ye(10)
            return "Sonsuzluk (veya hata, hangisi daha felsefiyse)"
        sonuc = a / b
        mesaj = "Bölme, paylaşmanın zorlu yolu."
    else:
        return "Geçersiz işlem! Sadece +, -, *, / destekleniyor. Ve çok yavaş."
    
    print(mesaj)
    zaman_ye(random.randint(1, 2))
    return sonuc

def main():
    print("🌟 Zaman Yiyen Hesap Makinesine Hoş Geldiniz!")
    print("Bu makine, basit işlemleri bile çağlar geçirerek yapar. Neden? Çünkü neden olmasın!")
    print("Örnek: 2 + 2 için biraz bekleyin...")
    
    a = 2
    b = 2
    islem = "+"
    sonuc = hesapla(a, b, islem)
    print(f"🎉 Sonuç: {sonuc}")
    print("\n🔍 Daha fazla hesap için kodu değiştirin. Veya sadece izleyin, zaman yiyilsin.")

if __name__ == "__main__":
    main()
