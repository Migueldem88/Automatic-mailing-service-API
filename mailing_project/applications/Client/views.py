from django.shortcuts import render

from django.shortcuts import render
from django.views.generic import (
    TemplateView,
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView)

from .models import Client
from django.urls import reverse_lazy

from .forms import ClientForm

class StartView(TemplateView):
    """view that loads start page"""
    template_name = 'start_page.html'

class ListAllClients(ListView):
    template_name = 'Client/list_all_clients.html'
    paginate_by = 2
    #ordering = 'id'
    context_object_name = 'clients'

    def get_queryset(self):
        client_list = Client.objects.all()
        return client_list

class ClientCreateView(CreateView):
    template_name = 'Client/add_client.html'
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('Client_app:list-all-clients')

    def form_valid(self,form):
        #logica del proceso
        client = form.save(commit=False)
        client.save()
        return super(ClientCreateView,self).form_valid(form)

class ClientUpdView(UpdateView):
    model = Client
    template_name = "Client/update_client.html"
    fields = [
        'number',
        'op_code',
        'tag',
        'tz',
        'email',
    ]
    success_url = reverse_lazy('Client_app:list-all-clients')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

    def form_valid(self,form):
        print('******Metodo form valid*****')
        return super(ClientUpdView,self).form_valid(form)

class ClientDelView(DeleteView):
    model = Client
    template_name = "Client/delete_client.html"
    success_url = reverse_lazy('Client_app:list-all-clients')


class ClientbyKword(ListView):
    template_name = 'Client/client_by_kword.html'
    context_object_name = 'clients'

    def get_queryset(self):
        area = self.kwargs['nname']
        lista = Client.objects.filter(
        email__icontains=area)

        return lista

