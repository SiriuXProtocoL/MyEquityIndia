from django.shortcuts import render, redirect
#import from the internet
import requests
#parse it
import json
#accessing models
from .models import stock_db
#create a form file with this calss
from .forms import StockForm
#for pop up messages
from django.contrib import messages


# Create your views here.
def index(request):
    return render(request, 'index.html', {})

def about(request):
    return render(request, 'about.html', {})

def accounts(request):
    return render(request, 'accounts.html', {})

def app(request):
    return render(request, 'app.html', {})

def blog(request):
    return render(request, 'blog.html', {})

def blogsingle(request):
    return render(request, 'blogsingle.html', {})

def career(request):
    return render(request, 'career.html', {})

def contact(request):
    return render(request, 'contact.html', {})

def dashboard(request):
    return render(request, 'dashboard.html', {})

def faq(request):
    return render(request, 'faq.html', {})

def helpdesk(request):
    return render(request, 'helpdesk.html', {})

def intro(request):
    return render(request, 'intro.html', {})

def lock(request):
    return render(request, 'lock.html', {})

def otp1(request):
    
    return render(request, 'otp1.html', {})

def price(request):
    from django.contrib.admin.utils import flatten

    if request.method == 'POST':
        form = StockForm(request.POST or None)
        
        if form.is_valid():
            form.save()
            messages.success(request,("Stock has been Added!"))
            return redirect('price')
        
    else:
        #get all items in the databse
        ticker = stock_db.objects.all()

        #A list to save the looped api data's
        output = []

        #Loop through the items to pull the data of all
        for tick in ticker:
            api_request = requests.get("https://fmpcloud.io/api/v3/profile/" + str(tick) + "?apikey=d588337e29bcd754ec1599a1938642cd")

            try:
                #conver to json
                api = json.loads(api_request.content)
                #saving the item to output list
                output.append(api)

            #if there api does not return anything as json
            except Exception as e:
                api = "Error..."
        
    flatten(output)

    return render(request, 'price.html', {"ticker": ticker, "output": output})

def pricedetails(request):

    return render(request, 'pricedetails.html', {})

def privacypolicy(request):
    return render(request, 'privacypolicy.html', {})

def profile(request):
    return render(request, 'profile.html', {})

def reset(request):
    return render(request, 'reset.html', {})

def settingsactivity(request):
    return render(request, 'settingsactivity.html', {})

def settingsprofile(request):
    return render(request, 'settingsprofile.html', {})

def signin(request):
    return render(request, 'signin.html', {})

def signup(request):
    return render(request, 'signup.html', {})

def team(request):
    return render(request, 'team.html', {})

def trade(request):
    return render(request, 'trade.html', {})

def wallet(request):
    return render(request, 'wallet.html', {})




