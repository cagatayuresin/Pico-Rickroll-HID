# 🖥️ Raspberry Pi Pico HID Rickroll Script

🇬🇧 **[Türkçe okumak için tıklayın](README_TR.md)**  

![License](https://img.shields.io/github/license/cagatayuresin/Pico-Rickroll-HID) ![Windows](https://img.shields.io/badge/Windows-Supported-brightgreen?logo=windows) ![macOS](https://img.shields.io/badge/macOS-Supported-brightgreen?logo=apple) ![Raspberry Pi](https://img.shields.io/badge/Raspberry%20Pi-Supported-red?logo=raspberrypi&logoColor=white) ![Pico](https://img.shields.io/badge/Pico-RP2040-orange?logo=raspberrypi&logoColor=white) ![RP2040](https://img.shields.io/badge/RP2040-Microcontroller-blue?logo=raspberrypi&logoColor=white) ![Adafruit](https://img.shields.io/badge/Powered%20by-Adafruit-red?logo=adafruit&logoColor=white) ![MicroPython](https://img.shields.io/badge/MicroPython-Compatible-orange?logo=micropython&logoColor=white)

![Pico Rickroll in Action](rickroll-roll.gif)

Bu proje, **Raspberry Pi Pico'yu bir klavye olarak kullanarak** takıldığı bilgisayarda **otomatik olarak Rickroll videosunu açan** bir HID (Human Interface Device) saldırı betiğidir.  

✅ **Windows ve macOS** desteği içerir.  
✅ **Türkçe Q klavye uyumluluğu eklenmiştir.**  
✅ **Otomatik olarak YouTube’u açar, tam ekran yapar ve sesi maksimuma çıkarır.**  

---

## 📌 Gereksinimler & Kurulum  

### 1️⃣ Gerekli Donanım  

- **Raspberry Pi Pico**  
- **USB Type-C veya micro USB kablo**  

### 2️⃣ Gerekli Yazılımlar  

- **CircuitPython 8.x veya 9.x** Pico'ya yüklü olmalıdır.  
- **Adafruit HID Kütüphaneleri** yüklenmiş olmalıdır.  

**📌 Adım Adım Kurulum:**  

1. **Raspberry Pi Pico’yu BOOTSEL modunda başlat.**  
   - Pico’yu bilgisayara bağlamadan önce `BOOTSEL` tuşuna basılı tut.  
   - Bilgisayara tak, sonra tuşu bırak.  
   - `RPI-RP2` isminde bir sürücü olarak görünmelidir.  

2. **CircuitPython Firmware’i Yükle**  
   - Güncel sürümü şu adresten indir: [https://circuitpython.org/board/raspberry_pi_pico/](https://circuitpython.org/board/raspberry_pi_pico/)  
   - `RPI-RP2` sürücüsüne `.uf2` dosyasını sürükleyip bırak.  

3. **Adafruit HID Kütüphanelerini Yükle**  
   - [https://github.com/adafruit/Adafruit_CircuitPython_HID/releases](https://github.com/adafruit/Adafruit_CircuitPython_HID/releases) adresinden **`adafruit_hid`** kütüphanesini indir.  
   - Pico’nun `CIRCUITPY` sürücüsündeki `lib` klasörüne **`adafruit_hid`** klasörünü kopyala.  

---

## 🔍 Nasıl Çalışır?  

1. **Pico bilgisayara takıldığında otomatik çalışır.**  
2. **Bilgisayarın işletim sistemini algılar.**  
   - **Windows ise:** `Win + R` ile Çalıştır penceresini açar.  
   - **MacOS ise:** `Cmd + Space` ile Spotlight’ı açar.  
3. **Türkçe Q klavye düzenine göre URL’yi doğru yazar.**  
4. **YouTube’u açar ve videoyu başlatır.**  
5. **Tam ekran yapar ve sesi maksimuma çıkarır.**  

📢 **Taktığın anda çalışır, çıkardığında durur!**  

---

## ⚙️ Klavye Desteği  

| **Klavye Düzeni** | **Destek Durumu** |
|-----------------|----------------|
| 🇹🇷 **Türkçe Q** | ✅ Destekleniyor |
| 🇹🇷 **Türkçe F** | ❌ Desteklenmiyor |
| 🇺🇸 **İngilizce Q (US)** | ✅ Destekleniyor |
| 🇬🇧 **İngilizce UK** | ❌ Desteklenmiyor |

**📢 NOT:** Bu kod **Türkçe Q klavye düzenine göre yazılmıştır.**  

**Eğer UK klavye kullanıyorsan, işletim sisteminde dil ayarlarını "English (US)" olarak değiştir.**  

---

## 🚀 Çalıştırma Talimatları  

1️⃣ **Kod Dosyasını Pico'ya Yükle**  

- **Bu `code.py` dosyasını** Pico’nun `CIRCUITPY` sürücüsüne at.  

2️⃣ **Pico’yu Çıkartıp Tekrar Tak**  

- **Artık taktığın anda çalışacaktır!**  

3️⃣ **Rickroll Başladı mı?**  

- Eğer `https://www.youtube.com/watch?v=dQw4w9WgXcQ` açıldıysa ve sesi sonuna kadar açtıysa HER ŞEY ÇALIŞIYOR! 😈🎵  

---

## 🛠 Olası Hatalar ve Çözümler  

**1️⃣ Problem:** URL yanlış yazılıyor, `/` yerine başka karakterler çıkıyor.  
**✅ Çözüm:**  

- Bilgisayarının klavye düzenini **English (US) olarak değiştir.**  

**2️⃣ Problem:** YouTube açılıyor ama tam ekran olmuyor.  
**✅ Çözüm:**  

- `F` tuşu bazı sistemlerde çalışmayabilir. **Kodda `Keycode.F` yerine `Keycode.CONTROL, Keycode.COMMAND, Keycode.F` deneyebilirsin.**  

**3️⃣ Problem:** Ses maksimuma çıkmıyor.  
**✅ Çözüm:**  

- **Ses tuşları işletim sistemine göre değişebilir.** `ConsumerControlCode.VOLUME_INCREMENT` yerine `Keycode.VOLUME_UP` deneyebilirsin.  

---

## 📢 Yasal Uyarı  

Bu kod **etik siber güvenlik amaçlıdır.** İzinsiz kullanım **suç teşkil edebilir.**  

🔹 **Güvenlik testleri ve eğlence amaçlı kullanın!**  
🔹 **Lütfen birini Rickroll yaparken dikkatli olun!** 😆  

---

## 🤝 Katkıda Bulunma

Her türlü katkı, hata bildirimi ve yeni özellik önerisi memnuniyetle karşılanır! Projeyi fork edip geliştirebilir, eksik gördüğün noktaları düzeltebilirsin.

Eğer bir hata fark edersen veya yeni bir özellik eklemek istersen, bir "issue" açabilir veya "pull request" gönderebilirsin.

---

## 📜 Lisans

Bu proje MIT Lisansı altında lisanslanmıştır.

🔹 Projeyi özgürce kullanabilir, değiştirebilir ve paylaşabilirsin.
🔹 Ancak lisans şartlarına uymayı unutma! 📜

Daha fazla bilgi için [LICENSE](LICENSE) dosyasına göz atabilirsin. 🚀

---

🎵 **"Never gonna give you up, never gonna let you down..."** 🎵  
