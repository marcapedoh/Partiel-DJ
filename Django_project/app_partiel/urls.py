from django.urls import path
from app_partiel.views import baseView,homeView,base1View,CustomerRegistrationView,CategoryView,MathsView,Categorie_detailView,rechercheView,ProfileView,address,CoursDetail
from django.contrib.auth import views as auth_view
from app_partiel.forms import LoginForm
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('base/',baseView.as_view()),
    path('home/',homeView,name='home'),
    path('login/',auth_view.LoginView.as_view(template_name="app/login.html", authentication_form=LoginForm),name='login'),
    path('registration/',CustomerRegistrationView.as_view(),name='enregistrement'),
    path('category/',CategoryView,name='categorie'),
    path('categorie_detail/<slug:val>',Categorie_detailView.as_view(),name='detail'),
    path("cours_detail/<int:pk>",CoursDetail.as_view(),name='coursdetail'),
    path('maths/',MathsView,name='maths'),
    path('recherche/',rechercheView.as_view(),name='recherche'),
    path('adresse/',address, name='adresse'),
    path('profile/',ProfileView.as_view(), name='profile'),
]+static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT)
