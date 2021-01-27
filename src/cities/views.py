from django.db.models import Q
from django.views.generic import TemplateView, ListView
from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render


from .models import City


class HomePageView(TemplateView):
    template_name = 'home.html'

class SearchResultsView(ListView):
    model = City
    template_name = 'search_results.html'

    def get_queryset(self): # new
        query = self.request.GET.get('q')
        object_list = City.objects.filter(
            Q(name__icontains=query) | Q(country__icontains=query)
        )
        return object_list

def description(request, question_id):
    city = get_object_or_404(City, pk=city_id)
    return render(request, 'description.html', {'city': city})
