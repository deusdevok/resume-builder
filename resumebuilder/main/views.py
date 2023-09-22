from django.views.generic import TemplateView, ListView
from django.views import View
from django.shortcuts import render

class IndexView(View):
    template_name = "main/index.html"

    def get(self, request):
        return render(request, self.template_name, None)
    
    def post(self, request):
        name = request.POST['your_name']
        print(name)
        return render(request, self.template_name, {'name': name})
