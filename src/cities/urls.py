
from django.urls import path
from . import views
from .views import HomePageView, SearchResultsView
app_name = 'cities'
urlpatterns = [
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('', HomePageView.as_view(), name='home'),
     path('<int:city_id>/', views.description, name='description'),
]
