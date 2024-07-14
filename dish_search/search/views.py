# Create your views here.
from django.shortcuts import render
from .models import Dish

def search(request):
    query = request.GET.get('q', '')
    results = Dish.objects.filter(name__icontains=query)
    context = {
        'query': query,
        'results': results
    }
    return render(request, 'search/search.html', context)
