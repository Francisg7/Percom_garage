import requests
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.contrib.auth.models import Group

import PercomGarage
from PercomGarage.decorators import unauthenticated, allowed_users, admin_only
from PercomGarage.models import User, Employe, Client, Vehicules
from PercomGarage.models import Garage

# Create your views here.
from PercomGarage.forms import clientForm, voitureForm

headers = {'Authorization': 'Token 97cfaaefc0263c6917733e3f13a316089f416b16'}


# ====================================== Authentication views================================================#

def register(request):
    return render(request, "register.html")


@unauthenticated
def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['email'], password=request.POST['password'])
        if user is not None:
            auth.login(request, user)

            group = Group.objects.get(name="garage_admin")
            user.groups.add(group)

            return redirect('index')
        else:
            return render(request, 'login.html', {'error': 'email or password is incorrect'})
    else:
        return render(request, "login.html")


@unauthenticated
def signupinfo(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('pass')
        cpassword = request.POST.get('cpass')
        if password != cpassword:
            return redirect('/register')
        else:
            user = PercomGarage.models.User.objects.create_user(username, email, password)
            garagelogin(request)
            user.save()
    return redirect('login')

@admin_only
def garagelogin(request):
    if request.method == "POST":
        nom = request.POST.get('gname')
        type = request.POST.get('typegarage')
        date_creation = request.POST.get('dc')
        telephone = request.POST.get('tel')
        logo = request.POST.get('logo')
        address = request.POST.get('address')
        employer = request.POST.get('employer')
        garage = Garage(nom_garage=nom, type_garage=type, date_creation_garage=date_creation, telephone=telephone,
                        logo=logo, address=address, numbre_employer=employer)
        garage.save()


def employe_regis(request):
    if request.method == "POST":
        nom = request.POST.get('nom')
        prenom = request.POST.get('prenom')
        date_naissance = request.POST.get('dnaissance')
        addresse = request.POST.get('addresse')
        telephone = request.POST.get('tel')
        cni = request.POST.get('cni')
        type = request.POST.get('contrat')
        salaire = request.POST.get('salaire')
        poste = request.POST.get('poste')
        specialite = request.POST.get('spec')
        profile = request.POST.get('profile')
        garagelogin(request)
        new_employer = Employe(
            nom=nom,
            prenom=prenom,
            addresse=addresse,
            date_de_naissance=date_naissance,
            type_de_contrat=type,
            salaire=salaire,
            cni=cni,
            poste=poste,
            specialite=specialite,
            # Garage=garagelogin(request),
            telephone=telephone,
            profile=profile,
        )
        new_employer.save()
        response = requests.post('http://127.0.0.1:8000/api/Employelist/', data={'key': new_employer},
                                 headers=headers).json()
        return render(request, "employee_register.html", {"response": response})
    return render(request, "employee_register.html")


def logout(request):
    auth.logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("/")


# ================================= Authorization views end======================================================#


@login_required(login_url='index')
@admin_only
def index(request):
    return render(request, "index.html")


def garagelist(request):
    response = requests.get('http://127.0.0.1:8000/api/GarageList/', headers=headers).json
    return render(request, "index.html", {'response': response})


# ------------------------------Client -------------------------------------------#


@login_required(login_url='index')
def add_client(request):
    if request.method == "POST":
        nom = request.POST.get('nom')
        prenom = request.POST.get('prenom')
        email = request.POST.get('email')
        addresse = request.POST.get('addresse')
        sex = request.POST.get('sex')
        CNI = request.POST.get('CNI')
        phone = request.POST.get('phone')
        image = request.POST.get('profile')
        all_client = Client(nom=nom, prenom=prenom, email=email, adresse=addresse, sex=sex,cni=CNI, telephone=phone, profile=image)
        all_client.save()
        return redirect("voiture")
    return render(request, "add_client.html")


@login_required(login_url='index')
def add_voiture(request):
    if request.method == "POST":
        immatriculation = request.POST.get('imm')
        marque = request.POST.get('marque')
        modele = request.POST.get('modele')
        couleur = request.POST.get('couleur')
        num_chassis = request.POST.get('num_chassis')
        nb_cheveaux = request.POST.get('nb_cheveaux')
        type = request.POST.get('type')
        num_porte = request.POST.get('num_port')
        nb_port = request.POST.get('nb_port')
        nb_place = request.POST.get('nb_place')
        desc = request.POST.get('desc')
        add_voiture = Vehicules(immatriculation=immatriculation,marque=marque, modele=modele, couleur=couleur, num_chasis=num_chassis, nb_chevaux=nb_cheveaux, type_moteur=type, num_portieres=num_porte, nb_portieres=nb_port, nb_places=nb_place, description=desc,
                                client=Client.objects.get(id=1))
        add_voiture.save()
        return redirect("list_client")
    else:
        return render(request, "add_voiture.html")



@login_required(login_url='index')
def list_client(request):
    list = Client.objects.all()
    return render(request, "list_client.html", {'list': list})


@login_required(login_url='index')
def detail_client(request, id):
    context = {"data": Client.objects.get(pk=id)}
    return render(request, "edit.html", context)


@login_required(login_url='index')
def update_client(request, id):
    context = {}
    # fetch the object related to passed id
    obj = get_object_or_404(Client, id=id)
    form = clientForm(request.POST or None, instance=obj)

    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("../" + id)
    context["form"] = form
    return render(request, "update_client.html", context)


@login_required(login_url='index')
def delete_client(request, id):
    edits = Client.objects.get(pk=id)
    edits.delete()
    return redirect("list_client")


# ------------------------------Client -------------------------------------------#


# ------------------------------Employer -------------------------------------------#
@login_required(login_url='index')
def add_employer(request):
    response = requests.post('http://127.0.0.1:8000/api/Employelist/', data={'key': 'value'}).json()
    return render(request, "add_employer.html", {'response': response})


@login_required(login_url='index')
def list_employer(request):
    response = requests.get('http://127.0.0.1:8000/api/Employelist/', headers=headers).json()
    return render(request, "list_employer.html", {'response': response})


@login_required(login_url='index')
def update_employer(request):
    response = requests.put('http://127.0.0.1:8000/api/Employelist/', data={'key': 'value'}).json()
    return render(request, "edit_employer.html", {'response': response})


@login_required(login_url='index')
def delete_employer(request):
    response = requests.delete('http://127.0.0.1:8000/api/Employelist/').json()
    return render(request, "list_employer.html", {'response': response})


# ----------------------------------Employer -------------------------------------------#


# ------------------------------Interventions -------------------------------------------#


@login_required(login_url='index')
def add_intervention(request):
    return render(request, "add_intervention.html")


@login_required(login_url='index')
def list_intervention(request):
    response = requests.get('http://127.0.0.1:8000/api/Interventionlist/', headers=headers).json()
    return render(request, "list_intervention.html", {'response': response})


@login_required(login_url='index')
def update_intervention(request, id):
    response = requests.put('http://127.0.0.1:8000/api/Interventionlist/', pk=id).json()
    return render(request, "edit_employer.html", {'response': response})


@login_required(login_url='index')
def delete_intervention(request):
    response = requests.delete('http://127.0.0.1:8000/api/Interventionlist/').json()
    return render(request, "list_employer.html", {'response': response})

# ----------------------------------Employer -------------------------------------------#
