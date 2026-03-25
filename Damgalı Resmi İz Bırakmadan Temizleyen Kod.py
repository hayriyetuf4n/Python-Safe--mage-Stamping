import os
from PIL import Image

#Temiz olan resmin yolu:
orijinal_temiz_resim = r"C:\Users\hayri\OneDrive\Masaüstü\nergis.jpg.jpg"

# Üzerine yazı eklenen(bozulmuş) resmin yolu:
yazili_bozuk_resim =r"C:\Users\siz\OneDrive\Masaüstü\ucan_ev_tam_orta.jpg"

def yaziyi_sil_ve_orijinale_don():
    print("--- İşlem Başlatıldı: Yazı Kaldırılıyor ---")

    if os.path.exists(yazili_bozuk_resim): #Yazılı olan dosya gerçekten var mı diye bakar
        try:
            os.remove(yazili_bozuk_resim) #Yazılı olan dosyayı bilgisayardan tamamen siler
            print(f"BAŞARILI: Yazılı dosya ({yazili_bozuk_resim}) sistemden temizlendi.")
        except Exception as e:  #Hata olursa bunun sayesinde yazdırır.
            print(f"HATA: Dosya silinirken bir sorun oluştu: {e}")
            return                                       # "e" hatayı isimlendirir.

        #Orijinal temiz dosyayı tekrar kullanıcıya gösterme
        if os.path.exists(orijinal_temiz_resim): #dosya var mı diye bakıyor
            print("BİLGİ: Orijinal resminiz zaten güvendeydi,resim açılıyor")
            temiz_img = Image.open(orijinal_temiz_resim)
            temiz_img.show() #Temiz, yazısız hali ekranda açılır
            print(" Resim eski haline getirildi")
        else:
            print("UYARI: Yazılı dosyayı silindi ama orijinal 'nergis.jpg' dosyasını bulunamadı.")
    
    else:
        print("BİLGİ:Yazılı bir dosya yok, resim zaten temiz.")

# --- ÇALIŞTIRMA ---
yaziyi_sil_ve_orijinale_don()
