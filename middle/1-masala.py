class Avtomobil:      # Avtomobile nomli class yartildi 
    def __init__(self, model, rang, marka, narx, yil):
        self.model = model      # Public    ularni abtirbut turlari berildi 
        self.rang = rang       # Public
        self.__marka = marka   # Private
        self.__narx = narx     # Private
        self.__yil = yil       # Private

    def get_narx(self):        # Narxni qaytarishi uchun metod 
        return self.__narx

    def get_yil(self):
        return self.__yil

    def set_narx(self, yangi_narx):     # Narxni yangilash uchun metod 
        if yangi_narx < 0:            # AGar manfiy bo'lsa 
            print("Xato: Narx manfiy bo'la olmaydi!")
        else:
            self.__narx = yangi_narx


# Metodlar call qilindi  object;ar yartildi 
avto = Avtomobil("Chevrolet Malibu", "Qizil", "Chevrolet", 20000, 2020)

print(f"Model: {avto.model}")
print(f"Rang: {avto.rang}")

print(f"Narx: {avto.get_narx()}")  
print(f"Ishlab chiqarilgan yil: {avto.get_yil()}")

avto.set_narx(-5000)  

avto.set_narx(25000) 
print(f"Yangilangan narx: {avto.get_narx()}") 
