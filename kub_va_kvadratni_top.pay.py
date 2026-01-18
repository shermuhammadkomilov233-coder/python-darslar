import random
import time

def kvadrat_kub_oyini():
    print("="*45)
    print(" 🚀 SONLARNING KVADRATI VA KUBINI TOPING! 🚀 ")
    print("="*45)
    print("To'xtatish uchun 'stop' deb yozing.")
    
    ball = 0
    savollar_soni = 0
    boshlanish_vaqti = time.time()

    while True:
        # Darajani tasodifiy tanlash (2-kvadrat, 3-kub)
        daraja = random.choice([2, 3])
        
        if daraja == 2:
            son = random.randint(2, 25) # Kvadrat uchun 25 gacha
            togri_javob = son ** 2
            savol_matni = f"{son} ning kvadrati (kvadrati) nechaga teng? "
        else:
            son = random.randint(2, 12) # Kub uchun 12 gacha
            togri_javob = son ** 3
            savol_matni = f"{son} ning kubi nechaga teng? "

        # Foydalanuvchi javobini olish
        print(f"\nSavol #{savollar_soni + 1}:")
        user_input = input(savol_matni).lower().strip()

        if user_input == 'stop':
            break

        # Tekshirish
        try:
            if int(user_input) == togri_javob:
                print("Dahshat! To'g'ri! 🔥")
                ball += 15 if daraja == 3 else 10 # Kub uchun ko'proq ball
            else:
                print(f"Xato! ❌ To'g'ri javob: {togri_javob}")
                ball -= 5
            savollar_soni += 1
        except ValueError:
            print("Iltimos, faqat son kiriting yoki 'stop' deb yozing!")

    # Yakuniy natijalar
    sarflangan_vaqt = round(time.time() - boshlanish_vaqti, 1)
    
    print("\n" + "="*40)
    print("🏁 O'YIN YAKUNLANDI! 🏁")
    print(f"Jami yechilgan savollar: {savollar_soni}")
    print(f"To'plangan umumiy ball: {ball}")
    print(f"Umumiy vaqt: {sarflangan_vaqt} soniya")
    if savollar_soni > 0:
        print(f"O'rtacha tezlik: {round(sarflangan_vaqt/savollar_soni, 2)} sek/savol")
    print("="*40)

if __name__ == "__main__":
    kvadrat_kub_oyini()
