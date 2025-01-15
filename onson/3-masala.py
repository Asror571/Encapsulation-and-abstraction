class Hayvon:              # Hayvon nomli ota class yartildi 
    def __init__(self, name, turi):     # Va xususiyatlari saqlandi 
        self.name = name
        self.turi = turi

    def info(self):      # Hayvonni malumotini aytarish uchun metod yozildi 
        return f"{self.name} {self.turi} turiga mansub."

class Yirtiqch(Hayvon):       # Va ota class dan voris olga holda class yaratildi 
    def __init__(self, name, turi, sound):     # Va Yirtqich hayvonni ovozi qo'shildi 
        super().__init__(name, turi)          
        self.sound = sound

    def speak(self):                           # Va gapirishi uchun metod yozildi 

        return f"{self.name} o'kirmoqda  : {self.sound}"

class Herbivore(Hayvon):       # O'txor hayvonlar uchun ota class dan metod yaratildi 
    def __init__(self, name, turi, favorite_foods):   # Va unaga o'txo'r hayvonni sevimli ovqati o'shildi 
        super().__init__(name, turi)                
        self.favorite_foods = favorite_foods 

    def eat_feed(self):      # Va hayvonni yeydigan ovqatini chiqarish uchun metdo yozildi 
        return f"{self.name} quyidagilarni yeydi: {', '.join(self.favorite_foods)}"  


# VA metodlar call qilindi objectlar berildi 
yirtqich_hayvon = Yirtiqch("Sher", "Yirtqich", "IIRRRRR")
otxor_hayvon = Herbivore("Sigir", "O'txo'r", ["maysa", "kartoshka"])

print(yirtqich_hayvon.info())
print(yirtqich_hayvon.speak())

print(otxor_hayvon.info())
print(otxor_hayvon.eat_feed())
