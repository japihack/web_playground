from django.shortcuts import render
from django.views.generic import TemplateView

class Home(TemplateView):
    template_name = "core/home.html"
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'title':"Mi super web playground", 'nombre_usuario':"pepito"})

class Sample(TemplateView):
    template_name = "core/sample.html"

