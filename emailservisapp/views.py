from .models import Client, Message, Mailing, Attempt
from .forms import ClientForm, MessageForm, MailingForm, AttemptForm
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.core.cache import cache
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View

from .services import send_message


def home(request):
    context = cache.get('home')

    if not context:
        total_mailings = Mailing.objects.count()
        active_mailings = Mailing.objects.filter(status_mailing='Запущена').count()

        # Получаем количество уникальных email-адресов получателей
        unique_clients = Client.objects.values('email').distinct().count()

        context = {
            'total_mailings': total_mailings,
            'active_mailings': active_mailings,
            'unique_clients': unique_clients,
        }
        cache.set('home', context, 60 * 15)

    return render(request, 'emailservisapp/home.html', context)

class ClientListView(ListView):
    model = Client

class ClientDetailView(DetailView):
    model = Client

class ClientCreateView(CreateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('emailservisapp:clients_list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class ClientUpdateView(UpdateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('emailservisapp:clients_list')

    # def get_form_class(self):
    #     user = self.request.user
    #     if user == self.object.owner:
    #         return ClientForm
    #     if user.has_perm('emailservisapp.can_unpublish_product'):
    #         return ProductModeratorForm
    #     raise PermissionDenied

class ClientDeleteView(DeleteView):
    model = Client
    success_url = reverse_lazy('emailservisapp:clients_list')

    # def post(self, request, *args, **kwargs):
    #     client_id = kwargs['pk']
    #     client = get_object_or_404(Client, id=client_id)
    #
    #     if not request.user.has_perm('catalog.can_delete_product'):
    #         return HttpResponseForbidden("У вас нет прав для удаления продукта.")
    #
    #     product.delete()
    #
    #     return redirect('catalog:products_list')

class MessageListView(ListView):
    model = Message

class MessageDetailView(DetailView):
    model = Message

class MessageCreateView(CreateView):
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('emailservisapp:messages_list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class MessageUpdateView(UpdateView):
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('emailservisapp:messages_list')

class MessageDeleteView(DeleteView):
    model = Message
    success_url = reverse_lazy('emailservisapp:messages_list')

class MailingListView(ListView):
    model = Mailing

class MailingDetailView(DetailView):
    model = Mailing

class MailingCreateView(CreateView):
    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy('emailservisapp:mailings_list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class MailingUpdateView(UpdateView):
    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy('emailservisapp:mailings_list')

class MailingDeleteView(DeleteView):
    model = Mailing
    success_url = reverse_lazy('emailservisapp:mailings_list')

class AttemptListView(ListView):
    model = Attempt
    context_object_name = 'attempts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        attempts = self.get_queryset()
        context['total_attempts'] = attempts.count()
        context['successful_attempts'] = attempts.filter(status_attempt='Успех').count()
        context['unsucessful_attempts'] = attempts.filter(status_attempt='Провал').count()
        context['sending_mails'] = sum(
            attempt.mailing.clients.count()
            for attempt in attempts.filter(status_attempt='Успех')
        )
        return context

class SendMailingView(View):
    template_name = 'emailservisapp/send_mailing.html'

    def get(self, request, pk):
        mailing = get_object_or_404(Mailing, pk=pk)

        success = send_message(mailing.pk, request)

        if success:
            print('Рассылка успешно отправлена')
        else:
            print('Рассылка не отправлена')

        return redirect('emailservisapp:mailings_list')

class AttemptDetailView(DetailView):
    model = Attempt

class AttemptCreateView(CreateView):
    model = Attempt
    form_class = AttemptForm
    success_url = reverse_lazy('emailservisapp:attempts_list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class AttemptUpdateView(UpdateView):
    model = Attempt
    form_class = AttemptForm
    success_url = reverse_lazy('emailservisapp:attempts_list')

class AttemptDeleteView(DeleteView):
    model = Attempt
    success_url = reverse_lazy('emailservisapp:attempts_list')
