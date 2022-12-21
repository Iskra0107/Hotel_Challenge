from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from .models import Hotel, Review
from .forms import ReviewForm

# Create your views here.

def hotel_list(request):
    if request.method == "POST":
        form_data = ReviewForm(request.POST)
        if form_data.is_valid():
            hotels = form_data.save(commit=False) #da vrati objakt koj seushte se nema zacuvano vo bazata
            hotels.user = request.user
            hotels = form_data.save()

    #fav_hotel = get_object_or_404(Hotel, id=id)
    #is_favourite = False
    #if fav_hotel.fav.filter(id=request.user.id).exists():
    #

    is_favourite = True
    queyset = Hotel.objects.all().order_by('hotel_name')
    context = {'hotel_list': queyset, "form": ReviewForm , 'is_favourite':is_favourite}
    return render(request, 'hotel_list.html', context=context)


def add_review(request):
    if request.method == "POST":
        form_data = ReviewForm(request.POST)
        if form_data.is_valid():
            hotels = form_data.save(commit=False)
            hotels.user = request.user
            current_user = request.user
            form_data.user_id = current_user.id
            hotels = form_data.save()
    queyset = Review.objects.all()
    context = {'add_review': queyset, "form": ReviewForm}
    return render(request, 'add_review.html', context=context)


def home(request):
    return render(request, 'home.html', {})


def favourite_hotels(request):
    return render(request,'favourite_hotels.html',{})



def search_hotels(request):
    if request.method == "POST":
        searched = request.POST['searched']
        hotelss = Hotel.objects.filter(hotel_name__contains=searched)

        return render(request, 'search_hotels.html',
                      {'searched': searched,
                       'hotelss': hotelss})
    else:
        return render(request, 'search_hotels.html', {})



def like_review(request, pk):
    hotels = get_object_or_404(Review, id=request.POST.get('hotels.id'))
    hotels.likes.add(request.user)
    return render(request, 'hotel_list.html')
