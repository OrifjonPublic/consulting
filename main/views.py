import requests

from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages

from .models import ( Activity, ActivityPhotos, Company, 
                     Contact, FAQ, Hamkorlar, Logo, HeroTitle,
                     Reviews, SocialMedia, Takliflar, Team, User, Videourl
                    )
from .forms import TakliflarForm


TELEGRAM_BOT_TOKEN = '7571072763:AAHdS-k5S-zvrklLXx-Oo1i6dg4a9ywW0YA'


def send_to_telegram(text):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        'chat_id':  6368117162,
        'text': text
    }
    response = requests.post(url, json=payload)
    print(response)
    return response.status_code


class HomeView(View):
    def get(self, request):

        title = HeroTitle.objects.last()
        logo = Logo.objects.last()
        contact = Contact.objects.last()
        social = SocialMedia.objects.last()
        team = Team.objects.all()
        video_url = Videourl.objects.last()
        reviews = Reviews.objects.all()
        hamkorlar = Hamkorlar.objects.all()
        activity = Activity.objects.all()
        faq = FAQ.objects.all()
        company = Company.objects.last()

        if video_url.video_url:
            x = str(video_url.video_url)
            x = x.replace('www', 'img')
            y = x[:23] + '/vi/' + x[32:] + '/0.jpg'  

        context = {
            'title': title, 'logo': logo, 'contact': contact,
            'social': social, 'team': team, 'video_url':video_url,
            'reviews': reviews, 'hamkorlar': hamkorlar,
            'activity': activity, 'faq': faq,
            'company': company, 'y': y
            }
        print(y)
        return render(request, 'index.html', context)
    def post(self, request):
        name = request.POST.get('name')
        telefon = request.POST.get('telefon')
        message = request.POST.get('message')
        if type(name)!= 'str' or type(telefon)!= 'str' or type(message)!= 'str' :
            messages.info(request, "Malumotlarni to'g'ri kiriting!")
            return redirect('main:home')
        new = Takliflar.objects.create(
              full_name = name,
              phone_number = telefon,
              message = message  
            )

        ans = send_to_telegram(f'{new.id}-xabar🎫 \n\n\nKlient:\t {name}\n Telefon raqam:\t {telefon} \n  Xabar:\t {message}')
        # print(ans)
        # if ans == 200:
        return redirect("main:home")


class Detail(View):
    def get(self, request, id):
        logo = Logo.objects.last()
        contact = Contact.objects.last()
        social = SocialMedia.objects.last()
        try:
            one = Activity.objects.get(id=id)
        except:
            context = {
            'logo': logo,
            'contact': contact,
            'social': social
        }
            return render(request, 'error.html', context)
        context = {
            'logo': logo,
            'contact': contact,
            'social': social,
            'one': one
        }
        return render(request, 'detail.html', context)


def error(request, exception):
    logo = Logo.objects.last()
    contact = Contact.objects.last()
    social = SocialMedia.objects.last()

    context = {
    'logo': logo,
    'contact': contact,
    'social': social
    }
    return render(request, 'error.html', context)