import os
from PIL import Image, ImageDraw, ImageFont

#
orijinal_yol = r"C:\Users\siz\OneDrive\Masaüstü\nergis.jpg.jpg"
cikti_yol = r"C:\Users\siz\OneDrive\Masaüstü\ucan_ev_tam_orta.jpg"

def yazi_ekle_tam_orta():
    if not os.path.exists(orijinal_yol): #os.path.exists=yazıyı yazmadan önce dosya gerçekten o konumda mı diye bakıyor.
        print("HATA: Orijinal resim bulunamadı!")  #değilse uyarı veriyor.
        return

    try:
        img = Image.open(orijinal_yol).convert("RGB")#Resmi açıp renk modunu RGB ye sabitliyor,renk kanallarını eşitler.
        draw = ImageDraw.Draw(img)  #resmin üstüne sanal bir katman koyup oraya yazı yazar
        W, H = img.size

       
        try:
            font = ImageFont.truetype("arial.ttf", 80)  #yazı tipi yüklüyor ve boyutunu 80 piksel ayarlıyor
        except:
            # Arial bulunamazsa standart fontu kullanıyor
            font = ImageFont.load_default()

        mesaj = "UCAN EV VE BALONLAR"

        left, top, right, bottom = draw.textbbox((0, 0), mesaj, font=font)#tam ortayı hesaplayıp yazıyı yazdıracak
        w = right - left
        h = bottom - top
        
        x = (W - w) / 2    #Tam orta koordinatlarını hesaplıyor
        y = (H - h) / 2

        # Yazıyı ekle (Önce gölge, sonra beyaz yazı)
        draw.text((x+4, y+4), mesaj, font=font, fill=(0, 0, 0)) # Gölge şeklinde yazı,hesaplanan konummun 4 piksel sağına ve soluna
        draw.text((x, y), mesaj, font=font, fill=(255, 255, 255)) # Ana yazı,beyaz olacak şekilde
                            #yazı tipi-boyutu  #beyaz renk kodu
        # Kaydetme ve Gösterme
        img.save(cikti_yol)
        print(f"BAŞARILI: Yazı eklendi. Dosya: {cikti_yol}")
        img.show()

    except Exception as e:
        print(f"Bir hata oluştu: {e}")

# Fonksiyonu çalıştır
yazi_ekle_tam_orta()
