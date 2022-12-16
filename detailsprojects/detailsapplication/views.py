from django.shortcuts import render,redirect
from .models import table

# Create your views here.
def ones(request):
    a=table.objects.all()
    print(a)
    return render(request,'oness.html',{'a':a})
def b(request):
    if request.method=='POST':
        name=request.POST['name']
        address=request.POST['address']
        phone=request.POST['phone']
        c=table(name=name,address=address,phone=phone)
        c.save()
        print(c)
        a=table.objects.all()
        print(a)
        return render(request,'oness.html',{'a':a})
    return render(request,'oness.html')
def delete(request,dele):
    b=table.objects.get(id=dele)
    b.delete()
    return redirect('one')

def edit(request,ed):
    c=table.objects.get(id=ed)
    print(c)
    return render(request,'edit.html',{'c':c})

def formupdate(request,con):
    if request.method=='POST':
        Add=table.objects.get(id=con)
        Add.name=request.POST['name']
        Add.address=request.POST['address']
        Add.phone=request.POST['phone']
        Add.save()
    return redirect('one')