from django.shortcuts import render

# Create your views here.
from .models import Post

def home(request):
    return render(request,'home.html')
def Add(request):
    if request.method == 'GET':
        if request.GET.get('fn', None) and request.GET.get('cm', None):
            post = Post()
            post.Full_Name = request.GET.get('fn', None)
            post.Car_Model= request.GET.get('cm', None)
            post.save()
        return render(request, 'Add.html')
    else:
        return render(request, 'Add.html')
def see(request):
    data=Post.objects.all()
    return render(request,'see.html',{'data':data})