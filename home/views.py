from django.shortcuts import render, HttpResponse
from doubt.models import PostQuery

# Create your views here.
def home(request):
    
    allquery = PostQuery.objects.all()
    context = {'allquery':allquery}
    return render(request,'home/home.html',context)

def search(request):
    search = request.GET['search']
    allquery = PostQuery.objects.filter(title__icontains=search)
    params = {'allquery':allquery}
    return render(request,"home/search.html",params)
    #return HttpResponse("this is search")