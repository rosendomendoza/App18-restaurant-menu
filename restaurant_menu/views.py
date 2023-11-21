from django.shortcuts import render
from django.views import generic
from .models import ItemModel, MEAL_TYPE
from .admin import MenuItemAdmin


class MenuListView(generic.ListView):
    # queryset = Item.objects.order_by("-date_created")
    queryset = ItemModel.objects.order_by("meal")
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['meals'] = MEAL_TYPE
        return context


class MenuItemDetailView(generic.DetailView):
    model = ItemModel
    template_name = "menu_item_detail.html"

def admin():
    admin.site.register(ItemModel, MenuItemAdmin)
