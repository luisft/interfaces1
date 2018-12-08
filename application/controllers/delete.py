import web
import application.models.model_datos as model_datos

render = web.template.render('application/views/', base='master')

class Delete:
    def __init__(self):
        pass

    def GET(self, Id): 
        datos = model_datos.select_Id(Id) 
        return render.delete(datos)
    
    def POST(self, Id):
        formulario = web.input()
        Id = formulario['Id']
        model_datos.delete_datos(Id)
        raise web.seeother('/')
