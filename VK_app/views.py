from django.views.generic import TemplateView
from django.shortcuts import render
from django.http import HttpResponse
from VK_app.models import ItemType,MenuItem
# Create your views here.

class HomeView(TemplateView):

    template_name = 'VK_app/homepage.html'

def appetizers(request):
    items_list = MenuItem.objects.order_by('item_code')
    item_dict = {'appetizers_items':items_list}
    return render(request, 'VK_app/appetizers.html', context=item_dict)
