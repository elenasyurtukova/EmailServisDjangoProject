from django.urls import path
from emailservisapp.apps import EmailservisappConfig
from emailservisapp.views import ClientListView, ClientDetailView, ClientCreateView, ClientUpdateView, ClientDeleteView

app_name = EmailservisappConfig.name

urlpatterns = [
    path('', ClientListView.as_view(), name='clients_list'),
    path('clients/<int:pk>/', ClientDetailView.as_view(), name='client_detail'),
    path('clients/create', ClientCreateView.as_view(), name='client_create'),
    path('clients/<int:pk>/update', ClientUpdateView.as_view(), name='client_update'),
    path('clients/<int:pk>/delete', ClientDeleteView.as_view(), name='client_delete')
]
