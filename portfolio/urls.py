
from django.urls import path
from . import views

app_name = "portfolio"

urlpatterns = [
    path('home', views.home_page_view, name='home'),
    path('licenciatura', views.licenciatura_page_view, name='licenciatura'),
    path('projetos', views.projetos_page_view, name='projetos'),
    path('blog', views.blog_page_view, name='blog'),
    path('novo', views.novo_topico_view, name='novo'),
    path('edita/<int:topico_id>', views.edita_topico_view, name='edita'),
    path('apaga/<int:topico_id>', views.apaga_topico_view, name='apaga'),
    path('quiz', views.quizz, name='quizz'),
    path('login', views.view_login, name='login'),
    path('logout', views.view_logout, name='logout'),
    path('', views.home_page_view, name='home'),
]