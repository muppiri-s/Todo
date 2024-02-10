from django.views.generic import ListView
from .models import ToDoItem


# Create your views here.
class AllToDos(ListView):
    model = ToDoItem
    template_name = "todo/index.html"


class TodayToDos(ListView):
    model = ToDoItem
    template_name = "todo/today.html"

    def get_queryset(self):
        return ToDoItem.objects.filter(due_date=date.today())