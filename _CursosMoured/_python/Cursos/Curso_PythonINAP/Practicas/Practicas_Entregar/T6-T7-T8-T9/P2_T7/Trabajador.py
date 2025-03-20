from Persona import Persona

class Trabajador():
    cargo=''
    sueldo=''

    def __init__(self,cargo):
            
        self.cargo = cargo
        

    def darCargo(self, cargo):
    
        self.cargo= cargo
    
    def darSueldo(self, sueldo):
    
        self.sueldo= sueldo

    def mostrarCargo(self):
        return "El cargo del trabajador es " + self.cargo 

    def mostrarSueldo(self):
        return "Y el salario que recibe en la acutalidad es " +  str(self.sueldo) + " €."
 