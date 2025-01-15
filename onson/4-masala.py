class Avtomobile:                        # Avtomobile nomli class yaratildi 
    def __init__(self,nom,marka,narxi):   
        self.__nom = nom      # Privete       # Barchasi  Privete atribu qilindi 
        self.__marka = marka   # Privete
        self.__narxi = narxi    # Privete 

    def get_nom(self):          # Mashina nomini chiqarish uchun metod yozildi 
        return f"Mashina nomi : {self.__nom}"
    
    def set_nom(self, yangi_nom):   # Mashinani nomini yangilash uchun metod yartildi 
        self.__nom = yangi_nom

    def get_marka(self):              # Markani choqaraish uchun metod
        return f"Yangilanagan marka :{self.__marka}"
    
    def set_marka(self, yangi_marka):  # MArkani yangilash 
        self.__marka = yangi_marka
    
    def get_narxi(self):
        return f"Yangilangan narxi : {self.__narxi}"
    
    def set_narxi(self, yangi_narxi):
        self.__narxi = yangi_narxi
    


# Metodlar call qilindi hamda objectlar yartildi 

mashinalar = Avtomobile("Cobalt", "Ravon", 1234)

print(mashinalar.get_nom())   
print(mashinalar.get_marka()) 
print(mashinalar.get_narxi()) 

mashinalar.set_nom("Malibu")
mashinalar.set_marka("Chevrolet")
mashinalar.set_narxi(6437)


print(mashinalar.get_nom())   
print(mashinalar.get_marka()) 
print(mashinalar.get_narxi())
 

    

        