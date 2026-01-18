import random
import time

def matematika_dueli():
    print("="*40)
    print(" MATEMATIKA DUELI: +, -, *, / ")
    print("="*40)
    print("To'xtatish uchun 'stop' deb yozing.")
    
    ball = 0
    jami_savol = 0
    boshlanish = time.time()

    while True:
        # Amallar ro'yxati
        amallar = ['+', '-', '*', '/']
        amal = random.choice(amallar)
        
        # Sonlarni tanlash va mantiqni sozlash
        if amal == '+':
            a, b = random.randint(1, 100), random.randint(1, 100)
            javob = a + b
        
        elif amal == '-':
            # Ayirishda manfiy son chiqmasligi uchun:
            a, b = random.randint(10, 100), random.randint(1, 50)
            if a < b: a, b = b, a
            javob = a - b
            
        elif amal == '*':
            a, b = random.randint(2, 15), random.randint(2, 12)
            javob = a * b
            
        elif amal == '/':
            # Bo'lishda faqat butun son chiqishi uchun:
            b = random.randint(2, 12)
            javob = random.randint(2, 12)
            a = b * javob
            
        # Savolni chiqarish
        print(f"\nSavol: {a} {amal} {b} = ?")
        user_input = input("Javobingiz: ").lower().strip()

        if user_input == 'stop':
            break

        # Tekshirish
        try:
            if int(user_input) == javob:
                print("Barakalla! ✅")
                ball += 10
            else:
                print(f"Xato! ❌ To'g'ri javob: {javob}")
                ball -= 5
            jami_savol += 1
        except ValueError:
            print("Iltimos, son kiriting!")

    # Yakuniy natija
    vaqt = round(time.time() - boshlanish, 1)
    print("\n" + "="*30)
    print(f"O'YIN TUGADI!")
    print(f"Jami savollar: {jami_savol}")
    print(f"To'plangan ball: {ball}")
    print(f"Sarflangan vaqt: {vaqt} soniya")
    print("="*30)

if __name__ == "__main__":
    matematika_dueli()
