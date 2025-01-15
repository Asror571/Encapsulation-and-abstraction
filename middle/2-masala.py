from abc import ABC, abstractmethod       # Import qilindi 

class Hayvon(ABC):         #  ota Class yaratildi abstrakt qilib 
    def __init__(self, turi, vazni):    
        self.turi = turi
        self.vazni = vazni

    def ovoz_chiqarish(self): 
        pass

class It(Hayvon):     # Bola class yartildi hamda xususiyatlar qo'shildi 
    def __init__(self, turi, vazni):
        super().__init__(turi, vazni)
    
    def ovoz_chiqarish(self):     # Ovoz chiqarishi uchun metod yozildi 
        return "vov-vov"

class Mushuk(Hayvon):            # Bola class 
    def __init__(self, turi, vazni):       
        super().__init__(turi, vazni)
    
    def ovoz_chiqarish(self):     # Ovoz chiqarishi uchun metod  
        return "miyov-miyov"

# Objetlar yaratildi hamda metodlar call qilindi 
it = It("It", 10)
mushuk = Mushuk("Mushuk", 5)

print(f"{it.turi} ovozi: {it.ovoz_chiqarish()}") 
print(f"{mushuk.turi} ovozi: {mushuk.ovoz_chiqarish()}")
