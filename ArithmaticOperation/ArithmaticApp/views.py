from django.shortcuts import render,redirect
from django.http.response import HttpResponse

i=None
j=None

def Input(request):
    return render(request,'Arithmatic.html')

def Output(request):
    Num1=request.GET['N1']
    Num2=request.GET['N2']
    global i
    global j
    i=int(Num1)
    j=int(Num2)
    cal=request.GET['but']
    if cal=='add':
        return redirect(add)

    if cal=='sub':
        return redirect(sub)

    if cal=='mul':
        return redirect(mul)

    if cal=='div':
        return redirect(div)

def add(request):
    Total=i+j
    data="The Addition of",i,"and",j,"is:",Total
    return HttpResponse(data)

def sub(request):
    Total=i-j
    data="The Substraction of",i,"and",j,"is:",Total
    return HttpResponse(data)
def mul(request):
    Total=i*j
    data="The Multiplication of",i,"and",j,"is:",Total
    return HttpResponse(data)
def div(request):
    Total=i/j
    data="The Division of",i,"and",j,"is:",Total
    return HttpResponse(data)

