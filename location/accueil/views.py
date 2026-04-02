from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from vehicules.models import Voiture

def accueil(request):
    # Get all available cars from database
    cars_list = Voiture.objects.filter(disponible=True).order_by('-date_ajout')
    
    # Pagination
    paginator = Paginator(cars_list, 12)
    page = request.GET.get('page', 1)
    
    try:
        cars = paginator.page(page)
    except PageNotAnInteger:
        cars = paginator.page(1)
    except EmptyPage:
        cars = paginator.page(paginator.num_pages)
    
    context = {
        'cars': cars,
        'pages': cars,  # So your template pagination works
        'current_page': cars.number
    }
    
    return render(request, 'accueil.html', context)