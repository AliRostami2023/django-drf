from django.urls import path
from . import views

app_name='home'
urlpatterns = [
    path('', views.Home.as_view()),
    path('question/', views.QuestionListView.as_view()),
    path('question/create', views.QuestionCreateView.as_view()),
    path('question/update/<int:pk>', views.QuestionUpdateView.as_view()),
    path('question/delete/<int:pk>', views.QuestionDeleteView.as_view()),
    path('questions/', views.QuestionViewMixin.as_view()),
    path('questions/<int:pk>', views.QuestionUpdateView.as_view()),
    path('questionsapi/', views.QuestionGenericApi.as_view()),
    path('questionsapi/<int:pk>', views.QuestionGenericUpdateApi.as_view()),
]

 