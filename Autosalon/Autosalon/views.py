from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def registratsiya(request):
    return render(request, 'registratsiya.html')

def sotib_olish(request):
    return render(request, 'sotib-olish.html')

def sotish(request):
    return render(request, 'sotish.html')

def sotuvchi_bolish(request):
    return render(request, 'sotuvchi-bolish.html')

def aktsiyalar(request):
    return render(request, 'aktsiyalar.html')

def tolov_turlari(request):
    return render(request, 'tolov-turlari.html')

def filiallar(request):
    return render(request, 'filiallar.html')

def kompaniya_haqida(request):
    return render(request, 'kompaniya-haqida.html')

def murojaat_uchun(request):
    return render(request, 'murojaat-uchun.html')