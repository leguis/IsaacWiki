from django.shortcuts import render
from .models import Card

# Create your views here.
def list_view(request):
    card_list = Card.objects
    return render(request, 'list.html', { 'card_list' : card_list })

def card_view(request, card_id):
    card = Card.objects.get(id=card_id)
    return render(request, 'card.html', { 'card' : card })