import tkinter as tk
import random

# Asosiy funksiya
def play(user_choice):
    options = ['Tosh', 'Qog\'oz', 'Qaychi']
    computer_choice = random.choice(options)
    
    # G'olibni aniqlash mantiqi
    if user_choice == computer_choice:
        result = "Durang!"
        color = "gray"
    elif (user_choice == 'Tosh' and computer_choice == 'Qaychi') or \
         (user_choice == 'Qog\'oz' and computer_choice == 'Tosh') or \
         (user_choice == 'Qaychi' and computer_choice == 'Qog\'oz'):
        result = "Siz yutdingiz! 🎉"
        color = "green"
    else:
        result = "Kompyuter yutdi! 🤖"
        color = "red"
    
    # Natijani ekranga chiqarish
    label_res.config(text=f"Siz: {user_choice}\nKompyuter: {computer_choice}\n{result}", fg=color)

# Oyna sozlamalari
root = tk.Tk()
root.title("Tosh-Qaychi-Qog'oz 2026")
root.geometry("400x450")
root.configure(bg="#f0f0f0")

# Matnlar
tk.Label(root, text="O'yinni boshlang!", font=("Arial", 18, "bold"), bg="#f0f0f0").pack(pady=20)
tk.Label(root, text="Tanlang:", font=("Arial", 12), bg="#f0f0f0").pack()

# Tugmalar uchun dizayn
btn_style = {"font": ("Arial", 12, "bold"), "width": 15, "height": 2, "fg": "white"}

tk.Button(root, text="Tosh 🪨", bg="#5d5d5d", **btn_style, 
          command=lambda: play("Tosh")).pack(pady=5)

tk.Button(root, text="Qog'oz 📄", bg="#3498db", **btn_style, 
          command=lambda: play("Qog'oz")).pack(pady=5)

tk.Button(root, text="Qaychi ✂️", bg="#e74c3c", **btn_style, 
          command=lambda: play("Qaychi")).pack(pady=5)

# Natija chiqadigan joy
label_res = tk.Label(root, text="", font=("Arial", 14, "italic"), bg="#f0f0f0", pady=20)
label_res.pack()

root.mainloop()
