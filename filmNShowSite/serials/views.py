from django.views import generic
from .models import Serial, Cast

class SerialsView(generic.ListView):
    template_name = 'serials/list-serials.html'
    queryset = Serial.objects.all()

class SerialCreateView(generic.CreateView):
    template_name = 'serials/add-serial.html'
    model = Serial
    fields = [
        'title',
        'description',
        'image',
        'duration',
        'age_limit',
    ]