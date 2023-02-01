from django.urls import path

from .views import News_Processes_comments
from .views import processes_forms
from .views import Filter_processes
from .views import Search_Output
from .views import main
from .views import like_get

urlpatterns = [
    path('<int:id>', News_Processes_comments, name = 'News_Processes_comments'),
    path('create/', processes_forms),
    path('search/', Filter_processes),
    path('search/result/<int:id>', Search_Output, name = 'Search_Output'),
    path('', main, name = 'main'),
    path('<int:id>/like/', like_get, name='like'),
]