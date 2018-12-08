import web
import application.models.model_datos as model_datos

render = web.template.render('application/views/', base='master')

class Update:
    def __init__(self):
        pass

    def GET(self, Id): 
        datos = model_datos.select_Id(Id) 
        return render.update(datos)
    
    def POST(self, Id):
        formulario = web.input()
        Id = formulario['Id']
        Nombre = formulario['Nombre']
        A_Paterno = formulario['A_Paterno']
        A_Materno = formulario['A_Materno']
        Direccion = formulario['Direccion']
        Telefono = formulario['Telefono']
        model_datos.update_datos(Id, Nombre, A_Paterno, A_Materno, Direccion, Telefono)
        raise web.seeother('/')
