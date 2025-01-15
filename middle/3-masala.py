from abc import ABC,abstractmethod     # Import qilindi 

class Education(ABC):           # Education ota  nomli class yaratildi 
    def __init__(self,nomi):
        self.name = nomi

    def dars_jarayoni(self):
        pass

class IT_center(Education):    # Bola class yaratildi   
    def __init__(self, nomi):
        super().__init__(nomi)
    
    def dars_jarayoni(self):      # Qayday tarxda dars o'tilishi ni qaytaradigan metod 
        return "Bootcamp tarzda o'tiladi"
    
class Til_center(Education):      # Bola class Til o'quv marzaklari uchun 
    def __init__(self, nomi):
        super().__init__(nomi)
    
    def dars_jarayoni(self):      # Dars qaynad tarzda o'tilishini uchun metod 
        return "Standard ko'rinishda o'tiladi "

# Objectlar yaratildi metodlar call qilindi 

it_markazi = IT_center("It markaz")
til_markazi = Til_center("Til markazi")

print(it_markazi.dars_jarayoni()) 
print(til_markazi.dars_jarayoni())