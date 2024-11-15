import datetime 
class nota:
    def __init__(self):
        self.fechaNota = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.mensaje = ""
    
    def getFecha(self):
        return self.fechaNota

    def getMensaje(self):
        return self.mensaje
    
    def setMensaje(self, msj):
        self.mensaje = msj
