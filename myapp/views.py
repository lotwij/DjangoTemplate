from django.shortcuts import render_to_response

# Create your views here.
def index(request):
    return render_to_response('index.html')

def store(request):
    return render_to_response('store.html')

def about(request):
    return render_to_response('about.html')

def products(request):
    return render_to_response('products.html')

