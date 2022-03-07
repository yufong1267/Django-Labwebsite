from django.shortcuts import render

def error_404(request, exception):
    return render(request, 'Labwebsite/page_404.html', status=404)

def error_500(request):
    return render(request, 'Labwebsite/page_500.html', status=404)