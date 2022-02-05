from django.urls import path

from pybo import views

app_name='pybo'

urlpatterns = [
    path('index/', views.index,name='index'),
    path('detail/<int:question_id>/',views.detail,name='detail'),
    path('answer/delete/<int:answer_id>/',views.answer_delete,name='answer_delete'),
    path('answer/update/<int:answer_id>/',views.answer_update,name='answer_update'),
    path('question/delete/<int:question_id>/',views.question_delete,name='question_delete'),
    path('question/update/<int:question_id>/',views.question_update,name='question_update'),

]
