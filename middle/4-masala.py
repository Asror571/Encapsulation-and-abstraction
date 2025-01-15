class Kitobdokoni:        # Ota class yaratildi 
    def __init__(self, nomi, joylashuvi, kitoblar, xizmatlar):      # Xususiyatlari 
        self.nomi = nomi
        self.joylashuvi = joylashuvi
        self.kitoblar = kitoblar  
        self.xizmatlar = xizmatlar  

    def ilmiy_kitoblar_mavjud(self):       # Ilmiy kitoblar bor yo'qligini bilish uchun metod
        return any("ilmiy" in kitob.lower() for kitob in self.kitoblar)      # Bor yoki yo'qligini tekshirish uchun 

    def kitobdokon_haqida(self):            # Bor yoki yo'qligini qaytaradigan metod 
        if self.ilmiy_kitoblar_mavjud():
            return f"{self.nomi} ({self.joylashuvi}) do'konida ilmiy kitoblar mavjud."
        else:
            return f"{self.nomi} ({self.joylashuvi}) do'konida ilmiy kitoblar yo'q."

# Objectlar yaratldi hamda metodlar call qilindi 

kitobdokon1 = Kitobdokoni(
    nomi="Dasturchi  Kitob do'koni",
    joylashuvi="Toshkent",
    kitoblar=["Ilmiy Fizika", "Roman", "Ilmiy Kimyo"],
    xizmatlar=["Kitob buyurtma qilish",]
)

kitobdokon2 = Kitobdokoni(
    nomi="Yoshlar Kitob do'koni",
    joylashuvi="Samarkand",
    kitoblar=["Roman", "Poema"],
    xizmatlar=["Kitob sotib olish"]
)


print(kitobdokon1.kitobdokon_haqida())  
print(kitobdokon2.kitobdokon_haqida())  
