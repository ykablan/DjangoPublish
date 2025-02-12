from django.shortcuts import render, HttpResponse

# Create your views here.
def anasayfa(request):
    return HttpResponse('Ana Sayfa')