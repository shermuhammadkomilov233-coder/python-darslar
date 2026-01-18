# import matplotlib.pyplot as plt

# # Ma'lumotlar
# x = [1, 2, 3, 4, 5]
# y = [2, 4, 6, 8, 10]

# plt.plot(x, y, label='To‘g‘ri chiziq', color='blue', marker='o')
# plt.title('Oddiy chiziqli grafik')
# plt.xlabel('X o‘qi')
# plt.ylabel('Y o‘qi')
# plt.legend()
# plt.grid(True)
# plt.show()

# import matplotlib.pyplot as plt

# mevalar = ['Olma', 'Banan', 'Gilos', 'Qovun']
# miqdori = [10, 15, 7, 12]

# plt.bar(mevalar, miqdori, color='green')
# plt.title('Mevalar miqdori')
# plt.show()

# import matplotlib.pyplot as plt

# x = [5, 7, 8, 7, 2, 17, 2, 9, 4, 11]
# y = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78]

# plt.scatter(x, y, color='red')
# plt.title('Nuqtali tarqalish grafigi')
# plt.show()

import matplotlib.pyplot as plt

tillar = ['Python', 'Java', 'C++', 'JavaScript']
ulush = [45, 25, 15, 15]

plt.pie(ulush, labels=tillar, autopct='%1.1f%%', startangle=140)
plt.title('Dasturlash tillari ulushi')
plt.show()