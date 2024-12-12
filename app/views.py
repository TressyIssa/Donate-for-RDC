from django.shortcuts import render, redirect
from django.http import HttpResponse
from .blockchain import web3, contract
from .forms import *
from django.contrib.auth import authenticate, login, logout
import random, string
from web3 import Web3
from django.conf import settings
from django.http import JsonResponse

# Initialise Web3
web3 = Web3(Web3.HTTPProvider(settings.WEB3_PROVIDER))
def generate_username(email):
    """Allows you to retrieve the email address and generate a random username with this address"""
    username = ""

    part_one = email.split("@")[0]
    bad_characters = ".'!?"

    username += "".join(x for x in part_one if x not in bad_characters)
    end = "".join(random.sample(string.ascii_lowercase + string.digits, 6))
    username += "_" + end
    return username

def test(request):
    return HttpResponse("Hello amede")

def index(request):
    context = {}
    return render(request, "index.html", context)

def login_view(request):
    form = LoginForm(request.POST or None)
    msg = ""

    if form.is_valid():
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            if user.is_active:
                return redirect("home")
            else:
                msg = "Please confirm your email before logging in."
        else:
            msg = "We couldn't validate your email. Please try again."
    else:
        if request.method == "POST":
            msg = "We couldn't validate your email. Please try again."

    context = {
        "form": form
    }
    return render(request, "login.html", context)

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            email = form.cleaned_data.get('email')
            user.username = generate_username(email)
            user.save()
        else:
            print(form.errors)
    else:
        form = RegisterForm()
    context = {
        "form": form
    }
    return render(request, "inscription.html", context)



def addDon(request):
    if request.method == 'POST':
        form = DonForm(request.POST)
        if form.is_valid():
            don = form.save(commit=False)
            don.user = request.user
            don.save()

            project = form.cleaned_data.get('project')
            montant = form.cleaned_data.get('montant')
            adresse = form.cleaned_data.get('adresse')
            email = request.user.email

            # Convertir le montant en Wei (l'unité minimale d'Ethereum)
            montant_wei = Web3.to_wei(montant, 'ether')  # Utilisez Web3.to_wei (underscore)

            contract_address = '0x44aab30910E4b63eD3f761c514695d4263c93AeB'

            # Préparer la transaction
            transaction = {
                'from': adresse,
                'to': contract_address,
                'value': montant_wei,
                'gas': 2000000,
                'gasPrice': Web3.to_wei('50', 'gwei'),  # Conversion de gasPrice en gwei
            }

            # Envoyer la transaction
            tx_hash = web3.eth.send_transaction(transaction)
            print(f"Transaction envoyée avec succès, hash: {tx_hash.hex()}")
        else:
            print(form.errors)
    else:
        form = DonForm()
    context = {
        "form": form
    }
    return render(request, "formdon.html", context)

def addProjet(request):
    if request.method == 'POST':
        form = ProjetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
        else:
            print(form.errors)
    else:
        form = ProjetForm()
    context = {
        "form": form
    }
    return render(request, "projet.html", context)

def home(request):
    projets = Projet.objects.all()
    dons = Don.objects.all().order_by("-date")
    context = {
        "projets": projets,
        "dons": dons,
    }
    return render(request, "home.html", context)



def save_transaction(request):
    try:
        user = request.user
        #sender = request.POST.get('account')
        sender = request.POST.get('sender')
        receiver = request.POST.get('recipient')
        amount = request.POST.get('amount')
        
        don = Don()
        don.user = user
        don.sender = sender
        don.receiver = receiver
        don.montant = amount
        don.save()
        
        status = 200
        
        data = {
            "message": "Saved",
            "trans_id": don.pk,
        }
        
    except Exception as e:
        print(e)
        status = 500
        
        data = {
            "message": e
        }
        
    return JsonResponse(data, status = status)
        

def update_transaction(request):
    try:
        user = request.user
        #sender = request.POST.get('account')
        id = int(request.POST.get('id'))
        hash = request.POST.get('hash')
        don = Don.objects.get(pk=id)
        don.hash = hash
        don.save()
        
        status = 200
        
        data = {
            "message": "updated"
        }
        
    except Exception as e:
        print(e)
        status = 500
        
        data = {
            "message": e
        }
        
    return JsonResponse(data, status = status)
        



def logout_view(request):
    logout(request)
    return redirect("home")
    
