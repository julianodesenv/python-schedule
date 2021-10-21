from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.core.paginator import Paginator
from django.db.models import Q, Value
from django.db.models.functions import Concat
from .models import Contact


def index(request):
    contacts = Contact.objects.order_by('-id').filter(
        view=True
    )
    paginator = Paginator(contacts, 10)
    page = request.GET.get('page')
    contacts = paginator.get_page(page)

    return render(request, 'contacts/index.html', {'contacts': contacts})


def show(request, contact_id):
    contact = get_object_or_404(Contact, id=contact_id)

    if not contact.view:
        raise Http404()

    return render(request, 'contacts/show.html', {'contact': contact})
    
def search(request):
    term = request.GET.get('term')

    if term is None or not term:
        raise Http404()

    campos = Concat('name', Value(' '), 'last_name')
    
    #contacts = Contact.objects.order_by('-id').filter(
    #    Q(name__icontains=term) | Q(last_name_icontains=term), # add OR in query
    #    view=True
    #)

    contacts = Contact.objects.annotate(
        full_name=campos
    ).filter(
        Q(full_name__icontains=term) | Q(phone__icontains=term)
    )

    #print(contacts.query)
    paginator = Paginator(contacts, 10)
    page = request.GET.get('page')
    contacts = paginator.get_page(page)

    return render(request, 'contacts/index.html', {'contacts': contacts})