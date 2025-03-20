class Persona():
    nombre=''
    dni=''
    apellidos=''
    fechaNacimiento= ''
    texto=''

    def __init__(self,  nombre):
        
        self.nombre= nombre
       
    def darNombre(self, nombre):
        self.nombre= nombre


    def darApeliido(self, apellidos):
        self.apellidos= apellidos

    def darDNI(self, dni):
        self.dni= dni


    def darFechaNacimeitno(self, fechaNacimiento):
        self.fechaNacimiento= fechaNacimiento

    def mostrarNombre(self):
        return self.nombre
    
    def mostrarApellidos(self):
        return self.apellidos
    
    def mostrarDNI(self):
        return self.dni
    
    def mostrarFechaDeNacimiento(self):
        return self.fechaNacimiento
    

        
  