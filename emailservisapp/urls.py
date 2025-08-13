from django.urls import path
from emailservisapp.apps import EmailservisappConfig
from emailservisapp import views

app_name = EmailservisappConfig.name

urlpatterns = [
    path('clients/', views.ClientListView.as_view(), name='clients_list'),
    path('clients/<int:pk>/', views.ClientDetailView.as_view(), name='client_detail'),
    path('clients/create', views.ClientCreateView.as_view(), name='client_create'),
    path('clients/<int:pk>/update', views.ClientUpdateView.as_view(), name='client_update'),
    path('clients/<int:pk>/delete', views.ClientDeleteView.as_view(), name='client_delete'),
    path('messages/', views.MessageListView.as_view(), name='messages_list'),
    path('messages/<int:pk>/', views.MessageDetailView.as_view(), name='message_detail'),
    path('messages/create', views.MessageCreateView.as_view(), name='message_create'),
    path('messages/<int:pk>/update', views.MessageUpdateView.as_view(), name='message_update'),
    path('messages/<int:pk>/delete', views.MessageDeleteView.as_view(), name='message_delete'),
    path('mailings/', views.MailingListView.as_view(), name='mailings_list'),
    path('mailings/<int:pk>/', views.MailingDetailView.as_view(), name='mailing_detail'),
    path('mailings/create', views.MailingCreateView.as_view(), name='mailing_create'),
    path('mailings/<int:pk>/update', views.MailingUpdateView.as_view(), name='mailing_update'),
    path('mailings/<int:pk>/delete', views.MailingDeleteView.as_view(), name='mailing_delete'),
    path('attempts/', views.AttemptListView.as_view(), name='attempts_list'),
    path('attempts/<int:pk>/', views.AttemptDetailView.as_view(), name='attempt_detail'),
    path('attempts/create', views.AttemptCreateView.as_view(), name='attempt_create'),
    path('attempts/<int:pk>/update', views.AttemptUpdateView.as_view(), name='attempt_update'),
    path('attempts/<int:pk>/delete', views.AttemptDeleteView.as_view(), name='attempt_delete'),
    path('mailing/<int:pk>/send/', views.SendMailingView.as_view(), name='send_mailing'),
    path('', views.home, name='home')

]
