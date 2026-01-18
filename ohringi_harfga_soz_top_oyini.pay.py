import sys

def soz_oyini():
    ishlatilgan_sozlar = []
    print("--- Oxirgi harfga so'z topish o'yiniga xush kelibsiz! ---")
    print("O'yinni to'xtatish uchun 'stop' deb yozing.")
    
    # Birinchi so'zni kiritish
    oldingi_soz = input("O'yinni boshlash uchun istalgan so'z kiriting: ").lower().strip()
    
    if not oldingi_soz or oldingi_soz == 'stop':
        print("O'yin yakunlandi.")
        return

    ishlatilgan_sozlar.append(oldingi_soz)

    while True:
        oxirgi_harf = oldingi_soz[-1]
        print(f"\nNavbatdagi so'z '{oxirgi_harf}' harfi bilan boshlanishi kerak.")
        
        yangi_soz = input("So'z kiriting: ").lower().strip()

        # O'yinni to'xtatish sharti
        if yangi_soz == 'stop':
            print(f"\nO'yin tugadi! Siz jami {len(ishlatilgan_sozlar)} ta so'z aytdingiz.")
            break

        # Shartlarni tekshirish:
        # 1. Bo'sh emasligi
        if not yangi_soz:
            print("Iltimos, so'z kiriting!")
            continue
            
        # 2. Avval ishlatilmaganligi
        if yangi_soz in ishlatilgan_sozlar:
            print(f"Xato! '{yangi_soz}' so'zi oldin ishlatilgan.")
            continue

        # 3. Oxirgi harfga mosligi
        if yangi_soz[0] != oxirgi_harf:
            print(f"Xato! So'z '{oxirgi_harf}' harfi bilan boshlanishi kerak edi.")
            continue

        # Agar hamma shart bajarilsa
        ishlatilgan_sozlar.append(yangi_soz)
        oldingi_soz = yangi_soz
        print(f"Barakalla! '{yangi_soz}' qabul qilindi.")

if __name__ == "__main__":
    soz_oyini()