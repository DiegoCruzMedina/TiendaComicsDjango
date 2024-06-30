class Carrito:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carro = self.session.get("carro")
        if not carro:
            carro = self.session["carro"] = {}
        self.carro = carro

    def agregar(self, comic):
        if str(comic.id) not in self.carro.keys():
            self.carro[comic.id] = {
                "producto_id": comic.id,
                "nombre": comic.nombre,
                "precio": str(comic.precio),
                "cantidad": 1,
                "imagen": comic.imagen 
            }
        else:
            for key, value in self.carro.items():
                if key == str(comic.id):
                    value["cantidad"] = value["cantidad"] + 1
                    value["precio"] = float(value["precio"]) + comic.precio
                    break  
        self.guardar_carro()

    def guardar_carro(self):
        self.session["carro"] = self.carro
        self.session.modified = True

    def eliminar(self, comic):
        comic_id = str(comic.id)
        if comic_id in self.carro:
            del self.carro[comic_id]
            self.guardar_carro()

    def restar(self,comic):
        for key, value in self.carro.items():
            if key==str(comic.id):
                value["cantidad"]=value["cantidad"]-1
                value["precio"]=float(value["precio"]) - comic.precio
                if value["cantidad"]<1:
                    self.eliminar(comic)
                    break
        self.guardar_carro()

    def limpiar(self):
        self.session["carro"] = {}
        self.session.modified = True
    
    def total(request):
        total= 0
        if request.user_authenticated:
            if 'carro' in request.session:
                for key, value in request.session["carro"].items():
                    total = total + float(value["precio"])
        return {
        "total":total
    }
