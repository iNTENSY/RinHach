from django.views import generic

from api.models import Transactions


class IndexListView(generic.ListView):
    queryset = Transactions.objects.all()
    paginate_by = 20
    template_name = 'base.html'
    context_object_name = 'objects'
