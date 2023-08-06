from django.shortcuts import render, HttpResponse, redirect

from .forms import MovieForm
from .models import Movies

# Create your views here.
def index(request):
    movies=Movies.objects.all()
    context={'movies':movies}

    return render(request,'index.html',context)

def detail(request,movie_id):
    movies = Movies.objects.get(id=movie_id)
    context = {'movies': movies}
    return render(request,'detail.html',context)


def add(request):
    if request.method == "POST":
        name=request.POST['name']
        year=request.POST['year']
        dec=request.POST['dec']
        img=request.FILES['img']
        movie=Movies(name=name,year=year,dec=dec,img=img)
        movie.save()
        return redirect('/')

    return render(request,'add.html')

def update(request,id):
    movie=Movies.objects.get(id=id)
    form=MovieForm(request.POST or None,request.FILES,instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'update.html',{'form':form,'movie':movie})

def remove(request,id):
    movie = Movies.objects.get(id=id)
    if request.method=='POST':
        movie=Movies.objects.get(id=id)
        movie.delete()
        return redirect('/')
    context = {'movies': movie}
    return render(request,'remove.html',context)