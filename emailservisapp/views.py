from .models import Client
from .forms import ClientForm
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

class ClientListView(ListView):
    model = Client

class ClientDetailView(LoginRequiredMixin, DetailView):
    model = Client

class ClientCreateView(LoginRequiredMixin, CreateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('emailservisapp:clients_list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class ClientUpdateView(LoginRequiredMixin, UpdateView):
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

class ClientDeleteView(LoginRequiredMixin, DeleteView):
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