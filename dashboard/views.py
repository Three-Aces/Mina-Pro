from django.shortcuts import render


def dashboardPage(request):
    context = {}
    return render(request, 'dashboard/index.html', context)


def blankPage(request):
    context = {}
    return render(request, 'dashboard/pages/blank.html', context)


def loginPage(request):
    context = {}
    return render(request, 'dashboard/pages/login.html', context)


def chartPage(request):
    context = {}
    return render(request, 'dashboard/charts.html', context)