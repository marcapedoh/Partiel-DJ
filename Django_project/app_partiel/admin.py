from django.contrib import admin
from app_partiel.models import Matiere,Videos,Professeurs
# Register your models here.

@admin.register(Matiere)
class MatiereModelAdmin(admin.ModelAdmin):
    list_diplay=['title','description','categorie','mat_image']

@admin.register(Videos)
class VideoModelAdmin(admin.ModelAdmin):
    list_display=['titre','description','category','videos']

@admin.register(Professeurs)
class ProfesseursModelAdmin(admin.ModelAdmin):
    list_display=['nom','prenom','specialite']