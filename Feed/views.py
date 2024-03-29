
from django.views.generic import ListView
from .models import Airport, Airline, Flight
# Create your views here.

class HomePage(ListView):
    
    http_method_names = ["get"]
    template_name = "feed/homepage.html"
    model = Flight

    context_object_name = "flights"
    #queryset = Airport.objects.all().order_by('-id')[0:30]

    
    def get_queryset(self):
        # Return a queryset of Airport objects
        return Airport.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['airlines'] = Airline.objects.all()  # Add queryset of Airline objects
        context['flights'] = Flight.objects.all()    # Add queryset of Flight objects
        return context

    

