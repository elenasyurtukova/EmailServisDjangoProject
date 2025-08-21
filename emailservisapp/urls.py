from django.urls import path
from emailservisapp.apps import EmailservisappConfig
from .views import ClientListView, ClientDetailView, ClientCreateView, ClientUpdateView, ClientDeleteView, \
    MessageListView, MessageDetailView, MessageCreateView, MessageUpdateView, MessageDeleteView, MailingListView, \
    MailingDetailView, MailingCreateView, MailingUpdateView, MailingDeleteView, AttemptListView, AttemptDetailView, \
    AttemptCreateView, AttemptUpdateView, AttemptDeleteView, SendMailingView, home, UserListView, UserBlockView

app_name = EmailservisappConfig.name

urlpatterns = [
    path("clients/", ClientListView.as_view(), name="clients_list"),
    path("clients/<int:pk>/", ClientDetailView.as_view(), name="client_detail"),
    path("clients/create", ClientCreateView.as_view(), name="client_create"),
    path(
        "clients/<int:pk>/update",
        ClientUpdateView.as_view(),
        name="client_update",
    ),
    path(
        "clients/<int:pk>/delete",
        ClientDeleteView.as_view(),
        name="client_delete",
    ),
    path("messages/", MessageListView.as_view(), name="messages_list"),
    path(
        "messages/<int:pk>/", MessageDetailView.as_view(), name="message_detail"
    ),
    path("messages/create", MessageCreateView.as_view(), name="message_create"),
    path(
        "messages/<int:pk>/update",
        MessageUpdateView.as_view(),
        name="message_update",
    ),
    path(
        "messages/<int:pk>/delete",
        MessageDeleteView.as_view(),
        name="message_delete",
    ),
    path("mailings/", MailingListView.as_view(), name="mailings_list"),
    path(
        "mailings/<int:pk>/", MailingDetailView.as_view(), name="mailing_detail"
    ),
    path("mailings/create", MailingCreateView.as_view(), name="mailing_create"),
    path(
        "mailings/<int:pk>/update",
        MailingUpdateView.as_view(),
        name="mailing_update",
    ),
    path(
        "mailings/<int:pk>/delete",
        MailingDeleteView.as_view(),
        name="mailing_delete",
    ),
    path("attempts/", AttemptListView.as_view(), name="attempts_list"),
    path(
        "attempts/<int:pk>/", AttemptDetailView.as_view(), name="attempt_detail"
    ),
    path("attempts/create", AttemptCreateView.as_view(), name="attempt_create"),
    path(
        "attempts/<int:pk>/update",
        AttemptUpdateView.as_view(),
        name="attempt_update",
    ),
    path(
        "attempts/<int:pk>/delete",
        AttemptDeleteView.as_view(),
        name="attempt_delete",
    ),
    path(
        "mailing/<int:pk>/send/", SendMailingView.as_view(), name="send_mailing"
    ),
    path("", home, name="home"),
    path("users/", UserListView.as_view(), name="users_list"),
    path("users/<int:pk>/update", UserBlockView.as_view(), name="user_block"),
]
