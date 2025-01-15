class Xodim:        # Xodim nomli class yartildi 

    def __init__(self, ism_familiya, yosh, lavozim):  # Xususiytlar saqlandi 
        self._ism_familiya = ism_familiya
        self._yosh = yosh
        self._lavozim = lavozim

    def get_ism_familiya(self):    # ism _ Familiayani qaytarishi uchun  metod     
        return self._ism_familiya

    def set_ism_familiya(self, yangi_ism_familiya):     # Ism _familaiyani almashtirish uchun metod 
        self._ism_familiya = yangi_ism_familiya

    def get_yosh(self):         # Yoshini qaytarishi uchun metod 
        return self._yosh

    def set_yosh(self, yangi_yosh):     # Yoshini o'gartirish uchun metod yaratildi 
        if yangi_yosh > 0:                # Yosh kriitganda manfiy son kiritmasligi uchun 
            self._yosh = yangi_yosh

    def get_lavozim(self):             # Lavozimni qaytarish uchun metod yartildi 
        return self._lavozim

    def set_lavozim(self, yangi_lavozim):    # Lavozmini o'zgartirish uchun metod yartildi 
        if yangi_lavozim:
            self._lavozim = yangi_lavozim


# objectlar yartildi 

xodim1 = Xodim("Asror", 16, "Software Engineer")


# Metodlar call qilindi 

print("Ism va familiya:", xodim1.get_ism_familiya())
print("Yosh:", xodim1.get_yosh())
print("Lavozim:", xodim1.get_lavozim())

xodim1.set_ism_familiya("Abdurasul Salimov")
xodim1.set_yosh(35)
xodim1.set_lavozim("Direktor")

print("\nYangilangan ma'lumotlar:")
print("Ism va familiya:", xodim1.get_ism_familiya())
print("Yosh:", xodim1.get_yosh())
print("Lavozim:", xodim1.get_lavozim())
