from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
#crear la direccion de los templates para que funcione el index
TEMPLATE_DIRS = (
    'os.path.join(BASE_DIR, "templates")'
)
#definir el index
def index(request):
    return render(request, "index.html"),