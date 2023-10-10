from django.shortcuts import render
from django.views import View
from isodate import parse_duration
from django.conf import settings
from app_partiel.models import Customer,Matiere
from app_partiel.forms import CustomerRegistrationForm,CustomerProfileForm
from django.contrib import messages
import requests
# Create your views here.
class baseView(View):
    def get(self,request):
        return render(request,"app/base.html",locals())


def homeView(request,*args,**kwargs):
    return render(request,"app/home.html",{})

def base1View(request,*args,**kwargs):
    return render(request,"app/base1.html",{})
class CustomerRegistrationView(View):
    def get(self,request):
        form=CustomerRegistrationForm()
        return render(request, "app/registration.html", locals())

    def post(self, request):
        form=CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Congratulations! User Registered Successfully")
        else:
            messages.warning(request,"Invalid Input Data")
        return render(request, "app/registration.html", locals())

def CategoryView(request,*args,**kwargs):
    return render(request,"app/category.html",{})

def MathsView(request,*args,**kwargs):
    return render(request,"app/maths.html",{})

class Categorie_detailView(View):
    def get(self,request,val):
        matiere=Matiere.objects.filter(category=val)
        titre=Matiere.objects.filter(category=val).values('title')
        return render(request,"app/categorie_detail.html",locals())

class CoursDetail(View):
    def get(self, request, pk):
        matiere=Matiere.objects.get(pk=pk)
        return render(request,"app/cours_detail.html", locals())


class rechercheView(View):

    def get(self,request):
        #videos_content=[]
        
        #if(request.method == "POST"):   
        recherche_url='https://www.googleapis.com/youtube/v3/search'
        video_url='https://www.googleapis.com/youtube/v3/videos'
        search_params={
            'part': 'snippet',
            'q': 'cours django python',
            'maxResults':9,
            'key': settings.YOUTUBE_DATA_API_KEY,
            'type':'video'
                
        }
        video_ids=[]
        recherche_user=requests.get(recherche_url,params=search_params)
        resultat=recherche_user.json()['items']
            
        for res in resultat:
            video_ids.append(res['id']['videoId'])

        video_params={
            'key': settings.YOUTUBE_DATA_API_KEY,
            'part': 'snippet,contentDetails',
            'id':','.join(video_ids)
        }
        r= requests.get(video_url,params=video_params)
        resultat_video=r.json()['items']
        videos_content=[]
        for res1 in resultat_video:    
            video_data={
                'title': res1['snippet']['title'],
                'id': res1['id'],
                'url':f'https://www.youtube.com/watch?v={res1["id"] }',
                'duration': int(parse_duration(res1['contentDetails']['duration']).total_seconds()//60),
                'thumbnail': res1['snippet']['thumbnails']['high']['url']
            }
            videos_content.append(video_data)
            
        context={
            'videos': videos_content
        }
        return render(request,"app/recherche.html",locals())



class ProfileView(View):
    def get(self,request):
        form = CustomerProfileForm
        return render(request, "app/profile.html", locals())
    def post(self, request):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            user = request.user
            name = form.cleaned_data['name']
            locality = form.cleaned_data['locality']
            city = form.cleaned_data['city']
            mobile = form.cleaned_data['mobile']
            state = form.cleaned_data['state']
            zipcode = form.cleaned_data['zipcode']

            reg = Customer(user=user, name = name,locality=locality, city=city, mobile=mobile, state=state, zipcode=zipcode)
            reg.save()
            messages.success(request, "Congratulations! Address Updated Successfully")
        else:
             messages.warning(request, "Invalid Input Data")
        return render(request, "app/profile.html", locals())


def address(request):
    add = Customer.objects.filter(user=request.user)
    return render(request,"app/adresse.html", locals())