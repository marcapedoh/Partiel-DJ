from django.db import models
from django.contrib.auth.models import User
# Create your models here.

STATES_CHOICES=(
    ('Lomé','TOGO'),
    ('Accra', 'GHANA'),

)
List_Matiere=(
    ('MTHS','Maths'),
    ('ALPG','Programmation'),
    ('MGSI','Methode Agiles'),
    ('IC3','bureautique'),
    ('CCNA','Reseau'),
    ('SCIN','securité informatique'),
    ('LINUX','systeme unix'),
    ('CRYPT','cryptographie'),
    ('LGUE','Langue'),
    ('EN','electronique'),
)

class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    locality = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    mobile = models.CharField(default='', max_length=50)
    state = models.CharField(choices=STATES_CHOICES, max_length=200)
    zipcode = models.IntegerField()
    
    def __str__(self):
        return self.name

class Matiere(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    category=models.CharField(choices=List_Matiere, max_length=5)
    mat_image=models.ImageField(upload_to='Cours')

    def __str__(self):
        return self.title

class Videos(models.Model):
    titre=models.CharField(max_length=100)
    description=models.TextField()
    category=models.CharField(choices=List_Matiere, max_length=5)
    videos=models.FileField(upload_to="Video")

    def __str__(self):
        return self.titre

class Professeurs(models.Model):
    nom=models.CharField(max_length=100)
    prenom=models.CharField(max_length=150)
    specialite=models.TextField()
    
    