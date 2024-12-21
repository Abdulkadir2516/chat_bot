from googletrans import Translator

def ceviri_programi(metin):
    # Translator nesnesi oluştur
    translator = Translator()

    print("Python Çeviri Programı")
    print("-----------------------")

    # Kullanıcıdan çevirilecek metni al
    metin =metin# input("Çevirmek istediğiniz metni girin: ")

    # Kullanıcıdan hedef dili al
    print("Hedef dil seçin (ör: 'tr' Türkçe, 'en' İngilizce, 'fr' Fransızca): ")
    hedef_dil = "en"#input("Hedef dil kodu: ").lower()

    try:
        # Metni çevir
        cevirilen = translator.translate(metin, dest=hedef_dil)

        # Sonuçları göster
        print("\nÇeviri:")
        return cevirilen.text
    except Exception as e:
        print(f"Hata oluştu: {e}")
        return "hatalı ceviri"


