from django.shortcuts import render

def run_html(request):
    return render (request , 'index.html')