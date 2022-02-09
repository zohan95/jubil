from django.shortcuts import render


def cardshower(request):
    return render(request, 'viewcards/main.html')
