from django.shortcuts import redirect
from django.urls import reverse
from django.views import generic

from api.models import Transactions


class IndexListView(generic.ListView):
    """
    Класс отображения главной страницы,
    выводящий все транзакции с помощью
    пагинации в 10 объектов.
    """
    queryset = Transactions.objects.all()
    paginate_by = 10
    template_name = 'base.html'
    context_object_name = 'objects'


class ChangeStatusRedirectView(generic.RedirectView):
    """
    Класс определяющий метод POST, для изменения статуса транзакции
    """
    def post(self, request, *args, **kwargs):
        object_id = int(self.request.POST.get('object_id'))
        status = self.request.POST.get('status')
        page = self.request.POST.get('page')

        obj = Transactions.objects.get(id=object_id)

        if status == 'approved':
            obj.fraud = 'approved'
        elif status == 'denied':
            obj.is_denied = True
        obj.save()
        return redirect(reverse('index') + f'?page={page}')