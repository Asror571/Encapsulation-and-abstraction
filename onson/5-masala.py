from abc import ABC, abstractmethod      # abctrak import qilndi

class Transport(ABC):              # Transport nomli ota class yartildi 
    def harakat_qilish(self):
        pass

class Avtobus(Transport):          # Va bola class yaratildi avtobus uchun 
    def harakat_qilish(self):
        return "Avtobus yo'lda harakatlanadi."

class Poezd(Transport):           # Bola class poyezd uchun 
    def harakat_qilish(self):
        return "Poezd faqat relsda harakatlanadi."

class Transport_Factory:               # Bola class turini aniqlsh uchun 
    def yaratish(transport_turi):
        if transport_turi == "avtobus":    # Agar shtimi to'g'ri bo'lsa 
            return Avtobus() 
        elif transport_turi == "poezd":     #AKs holda
            return Poezd()
        

# Objectlar yartildi hamda metodlar call qilndi 

avtobus = Transport_Factory.yaratish("avtobus")
poezd = Transport_Factory.yaratish("poezd")

print(avtobus.harakat_qilish())  
print(poezd.harakat_qilish())    
