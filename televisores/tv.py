class TV:
    _numTV = 0
    def __init__(self, marca, estado):
        self._marca = marca
        self._canal = 1
        self._precio = 500
        self._estado = estado
        self._volumen = 1
        TV._numTV += 1

    ## Métodos get
    def getMarca(self):
        return self._marca
    
    def getCanal(self):
        return self._canal
    
    def getPrecio(self):
        return self._precio
    
    def getVolumen(self):
        return self._volumen
    
    def getControl(self):
        return self._control
    
    ## Métodos set
    def setMarca(self, marca):
        self._marca = marca
    
    def setCanal(self, canal):
        if (self._estado == True): ## Condición
            if (canal >= 1 and canal <= 120): ## Condición
                self._canal = canal
            else:
                return
        else:
            return
    
    def setPrecio(self, precio):
        self._precio = precio

    def setVolumen(self, volumen):
        if (self._estado == True): ## Condición
            if (volumen >= 0 and volumen <= 7): ## Condición
                self._volumen = volumen
            else:
                return
        else:
            return
        
    def setControl(self, control):
        self._control = control

    ## Métodos numTV
    def getNumTV(cls):
        return cls._numTV
    
    def setNumTV(cls, num):
        cls._numTV = num

    ## Métodos encendido y apagado
    def turnOn(self):
        self._estado = True

    def turnOff(self):
        self._estado = False

    def getEstado(self):
        return self._estado
    
    ## Cambio de Canal
    def canalUp(self):
        if (self._estado == True and self._canal < 120):
            self._canal += 1
        else:
            return

    def canalDown(self):
        if (self._estado == True and self._canal > 1):
            self._canal -=1
        else:
            return
    
    ## Aumentar Volumen 
    def volumenUp(self):
        if (self._estado == True and self._volumen < 7):
            self._volumen += 1
        else:
            return
    
    def volumenDown(self):
        if (self._estado == True and self._volumen > 0):
            self._volumen -= 1
        else:
            return