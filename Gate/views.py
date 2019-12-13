from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("welcome to red gate")

def hiddenpage(request):
    return HttpResponse("welcome to Mariessas Hidden Cool Zone. No Slouches or Stoners")

def drummer(request):
    return HttpResponse("Duuuhhhh Hit Harrd")


def gal(request):
    return HttpResponse("oink oink https://vancouver.ca/police/")
