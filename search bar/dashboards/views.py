from django.shortcuts import render
from .models import Data
from django.db.models import Q
# Create your views here.

def index(request):
    if 'qr' in request.GET: #SEARCHING
        q=request.GET['qr']
        #data=Data.objects.filter(first_name__icontains=q)
        multiple_query=Q(Q(first_name__icontains=q) | Q(last_name__icontains=q))
        data=Data.objects.filter(multiple_query)
    else:
        data=Data.objects.all()
    context={
        'data':data
    }
    return render(request,'dashboard/index.html',context)
