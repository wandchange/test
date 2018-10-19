from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # http://127.0.0.1:8000/polls/344152/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
