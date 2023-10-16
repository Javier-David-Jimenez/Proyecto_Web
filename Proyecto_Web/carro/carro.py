
# (manejo de sesion)cogemos los datos de la sesion para guardarlos y mantener los productos en carro si sale o entra
class Carro:
    def __init__(self, request):
        
        self.request = request
        self.session = request.session
        carro = self.session.get("carro")
        
        # si no existe carro lo creamos  con un diccionario si existe cogemos el que habia
        if not carro:
           carro = self.session["carro"] = {}
      
        self.carro = carro
        
        
        #agregamos un poducto al carro   agregara de 1 producto  con el if crea el carro
        #con el else agrega al carro  mas productos si ya existia
    def agregar_producto(self, producto):
        if (str(producto.id) not in self.carro.keys()):
            self.carro[producto.id] = {
                "producto_id" : producto.id,
                "nombre" : producto.nombre,
                "precio" : str(producto.precio),
                "cantidad": 1,
                "imagen" : producto.imagen.url 
                
            }
        else:
            for key, value in self.carro.items():
                if key == str(producto.id):
                    value["cantidad"] = value["cantidad"] + 1
                    value["precio"] = float(value["precio"]) + producto.precio
                    break #para que no recorra mas una vez encontrado
        
        self.guardar_carro()
    
    #guardamos las modificaciones en el carro
    def guardar_carro(self):
        self.session["carro"] = self.carro
        self.session.modified = True
        #se modifico la sesion despues de modificar?  = true
    
    #Quita el producto entero del carro    
    def eliminar(self, producto):
        producto.id = str(producto.id)
        if producto.id in self.carro:
            del self.carro[producto.id]
            self.guardar_carro()
    
    #restamos uno de la cantidad de un producto
    def restar_producto(self, producto):
        for key, value in self.carro.items():
                if key == str(producto.id):
                    value["cantidad"] = value ["cantidad"]-1
                    value["precio"] = float(value["precio"]) - producto.precio
                    if value["cantidad"]<1:
                        self.eliminar(producto) 
                    break
        self.guardar_carro()
    
    # lvacia el carro la sesion en la que estamos es un diccionario vacio 
    def limpiar_carro(self):
        self.session["carro"] = {} 
        self.session.modified = True