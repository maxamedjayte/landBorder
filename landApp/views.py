from django.shortcuts import render

# Create your views here.
def dashboard(request):
    return render(request,"dashboard.html")

def borderReg(request):
    return render(request,"reg/border_reg.html")

def borderList(request):
    return render(request,"list/border_list.html")