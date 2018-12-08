import web
import application.models.model_datos as model_datos

render = web.template.render('application/views/', base='master')

class View:
    def __init__(self):
        pass

    def GET(self, Id):  
        datos = model_datos.select_Id(Id)
        return render.view(datos)
