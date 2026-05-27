from PIL import Image
import os

# Dönüştürülecek klasör yolu
folder_path = "resimler"

# Klasördeki tüm dosyaları gez
for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)

    # Uygun uzantı kontrolü (istediğiniz her uzantı türünü ekleyebilirsiniz.)
    if filename.lower().endswith((".png", ".jpeg", ".jpg")):

        # Dosya adı ve uzantıyı ayır
        name, ext = os.path.splitext(filename)

        # Yeni dosya adı (.jpg olacak)
        new_filename = f"{name}.jpg"
        new_path = os.path.join(folder_path, new_filename)

        # PNG'de alfa kanalı olabileceği için 'RGB' çeviriyoruz
        try:
            img = Image.open(file_path).convert("RGB")
            img.save(new_path, "JPEG")
            print(f"Dönüştürüldü → {new_filename}")
        except Exception as e:
            print(f"Hata: {filename} Lütfen resimlerini kontrol edin. İşlem Başarısız. ({e})")
