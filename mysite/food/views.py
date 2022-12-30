from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Item
from .forms import ItemForm
from django.template import loader
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView

# Create your views here.
def index(request):
    #to retrieve the data from database Item.objects.all()
    item_list = Item.objects.all()
    #templates = loader.get_template('food/index.html') #get template by loader
    context = {
        'item_list':item_list,
    }
    #return HttpResponse(item_list)
    return render(request, 'food/index.html', context)
    #return HttpResponse(templates.render(context, request))

#class based view here...
class IndexClassView(ListView):
    model = Item;
    template_name = 'food/index.html'
    context_object_name = 'item_list'
    
class DetailsClassView(DetailView):
    model = Item
    template_name = 'food/details.html'
    #context_object_name = 'item'
####################################
def details(request, item_id):
    item = Item.objects.get(pk=item_id)
    context = {
        'item':item,
    }
    #return HttpResponse('This is a item no/id: %s' % item_id)
    return render(request, 'food/details.html', context)

def item(request):
   return HttpResponse('This is a Item section view.')

def create_item(request):
    form = ItemForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('food:index')
    return render(request, 'food/item-form.html', {'form':form})

# create item class view...
class CreateItemView(CreateView):
    model = Item
    fields = ['item_name', 'item_desc', 'item_price', 'item_image']
    template_name = 'food/item-form.html'
    def form_valid(self, form):
        form.instance.user_name = self.request.user

        return super().form_valid(form)

def update_item(request, id):
    item = Item.objects.get(id=id);
    form = ItemForm(request.POST or None, instance=item)

    if form.is_valid():
        form.save()
        return redirect('food:index')
    
    return render(request, 'food/item-form.html', {'form':form, 'item':item})

def delete_item(request, id):
    item = Item.objects.get(id=id);

    if request.method=='POST' :
        item.delete()
        return redirect('food:index')
    
    return render(request, 'food/item-delete.html', {'item':item})

# def delete_item_list(request):
#     items = Item.objects.all()
#     context = {
#         'items':items,
#     }
#     return render(request, 'food/delete_item_list.html', context)