from . import views
from django.urls import path


urlpatterns = [
    path('portfolio_creation', views.portfolio_creation_view, name='portfolio_creation'),
    path('portfolio_restauration', views.portfolio_restauration_view, name='portfolio_restauration'),
    path('contact', views.contact_view, name='contact'),
    path('portfolio_item/<int:id_furniture>', views.portfolio_item_view, name='portfolio_item'),
]