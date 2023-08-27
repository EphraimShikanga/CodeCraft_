from django.urls import path
from .views import HomeTemplateView, IndexTemplateView, SearchTemplateView

app_name = 'core'
urlpatterns = [
	path('', IndexTemplateView.as_view(), name='index'),
	path('home/', HomeTemplateView.as_view(), name='home'),
    path('home/search_results/', SearchTemplateView.as_view(), name='search'),
]
