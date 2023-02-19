from django.shortcuts import render, redirect
from app.forms import CarrosForm
from app.models import Carros
from django.core.paginator import Paginator

# Create your views here.
def home(request):
    data = {}
    search = request.GET.get('search')
    if search:
        data['db'] = Carros.objects.filter(modelo__icontains=search)
    else:
        data['db'] = Carros.objects.all()
        
    # ====================================
    # Caso queria fazer uma paginação na página principal
    # all = Carros.objects.all()
    # paginator = Paginator(all, 3)
    # pages = request.GET.get('page')
    # data['db'] = paginator.get_page(pages)
    return render(request, 'index.html', data)


def form(request):
    data = {}
    data['form'] = CarrosForm()
    return render(request, 'form.html', data)


def create(request):
    form = CarrosForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    

def view(request, id):
    data = {}
    data['db'] = Carros.objects.get(id=id)
    return render(request, 'view.html', data)


def edit(request, id):
    data = {}
    data['db'] = Carros.objects.get(id=id)
    data['form'] = CarrosForm(instance=data['db'])
    return render(request, 'form.html', data)

def update(request, id):
    data = {}
    data['db'] = Carros.objects.get(id=id)
    form = CarrosForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('home')
    

def delete(request, id):
    db = Carros.objects.get(id=id)
    db.delete()
    return redirect('home')

