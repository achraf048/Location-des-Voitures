from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Voiture

def accueil(request):
    # Get all cars from database
    cars = Voiture.objects.filter(disponible=True)
    
    # Apply filters if any
    search_query = request.GET.get('search', '')
    category = request.GET.get('categorie', '')
    fuel = request.GET.get('carburant', '')
    
    if search_query:
        cars = cars.filter(
            models.Q(nom__icontains=search_query) | 
            models.Q(marque__icontains=search_query)
        )
    
    if category:
        cars = cars.filter(categorie__icontains=category)
    
    if fuel:
        cars = cars.filter(carburant__icontains=fuel)
    
    # Pagination
    paginator = Paginator(cars, 12)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    
    context = {
        'cars': page_obj,
        'pages': page_obj,
    }
    
    return render(request, 'accueil.html', context)

def voiture_detail(request, id):
    car = get_object_or_404(Voiture, id=id)
    return render(request, 'voiture_detail.html', {'car': car})