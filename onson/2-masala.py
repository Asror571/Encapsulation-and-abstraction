class Telefon:                     # TElefon nomli class yartildi 
    def __init__(self):
        self._kontaktlar = {}       # Kantaklarni saqlash uchun dict yaratilidi
        
    def add_kontakt(self, name, number):     # Kantak qo'shish uchun metod yartildi 
        if name in self._kontaktlar:          #Agar kantak mavjud bo'lsa   
            print(f"{name} kontakt allaqachon qo'shilgan.")
        else:
            self._kontaktlar[name] = number      #Qo'shiladi    
            print(f"{name} kontakti muvaffaqiyatli qo'shildi.")
    
    def get_kontakt(self, name):                  # Kantakni chiqarish uchun metod yaratildi 
        if name not in self._kontaktlar:        # Agar kantak topilmasa 
            return "Kontakt mavjud emas."
        else:
            return f"{name}: {self._kontaktlar[name]}"    # Aks holda qo'shiladi 


telefonlar = Telefon()

# Objectlar yartildi va metodlar call qilindi 
telefonlar.add_kontakt("Asror", "1234")
telefonlar.add_kontakt("Suxrobbek", "1987")


print(telefonlar.get_kontakt("Asror"))
print(telefonlar.get_kontakt("Abdullajon"))

print(telefonlar.get_kontakt("Doston"))
