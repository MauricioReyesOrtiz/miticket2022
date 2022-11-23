from django.urls import path
from .views import ClienteView
from .views import TicketView
 
urlpatterns=[
    path('clientes/', ClienteView.as_view(), name='companies_list'),
    path('clientes/<int:id>', ClienteView.as_view(), name='clientes_process'),
    path('tickets/', TicketView.as_view(), name='companies_list'),
    path('tickets/<int:id>', TicketView.as_view(), name='tickets_process')
]