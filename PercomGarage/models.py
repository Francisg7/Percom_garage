from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models


class Client(models.Model):
    Male = 'M'
    Female = 'F'
    Sex = [(Male, 'Male'), (Female, 'Female')]
    id = models.BigAutoField(primary_key=True)
    nom = models.CharField(max_length=254)
    prenom = models.CharField(max_length=254)
    adresse = models.CharField(max_length=254)
    email = models.EmailField(max_length=254, unique=True)
    cni = models.CharField(unique=True, max_length=14, default=1, validators=[RegexValidator(r'^\d{1,14}$')])
    sex = models.CharField(max_length=10, choices=Sex, default=Male, )
    telephone = models.CharField(max_length=9, validators=[RegexValidator(r'^\d{1,10}$')], default=1)
    profile = models.ImageField(upload_to='pics_clients')
    # vehicule = models.ForeignKey('Vehicules', on_delete=models.SET_NULL, default='', null=True, blank=True)

    class Meta:
        db_table = 'client'
        ordering = ['nom']

    def __str__(self):
        return self.nom


class Commande(models.Model):
    id = models.BigAutoField(primary_key=True)
    date_livraison = models.DateField(auto_now=False, auto_now_add=False)
    prix = models.IntegerField()
    quantite = models.IntegerField()
    remise = models.IntegerField()
    description = models.CharField(max_length=254)
    stocks = models.ManyToManyField('Stock', blank=True)
    client = models.ForeignKey('Client', on_delete=models.SET_NULL, default='', null=True, blank=True)
    employer = models.ForeignKey('Employe', on_delete=models.SET_NULL, default='', null=True, blank=True)

    class Meta:
        db_table = 'commande'
        ordering = ['description']


class Employe(models.Model):
    CDI = 'CDI'
    CDD = 'CDD'
    Carrosier = 'Carrosier'
    Controleur_Automobile = 'Controleur Automobile'
    Depanneur_remorquer = 'Depanneur remorquer'
    Electricien_Automobile = 'Electricien Automobile'
    Mecanicien_Automobile = 'Mecanicien Automobile'
    Mecanicien_motocycle = 'Mecanicien motocycle'
    Monteur_en_pneumatique = 'Monteur en pneumatique'
    Peintre_en_carroserie = 'Peintre en carroserie'
    Technicien_en_Mecanique = 'Technicien en Mecanique'

    Poste = [(Carrosier, 'Carrosier/Carrosière'), (Electricien_Automobile, 'Electricien_Automobile'),
             (Mecanicien_Automobile, 'Mecanicien_Automobile'), (Mecanicien_motocycle, 'Mecanicien_motocycle'),
             (Peintre_en_carroserie, 'Peintre_en_carroserie'), (Technicien_en_Mecanique, 'Technicien_en_Mecanique')
             ]

    Speciality = [(Carrosier, 'Carrosier/Carrosière'),
                  (Controleur_Automobile, 'Controleur Automobile'),
                  (Depanneur_remorquer, 'Depanneur remorquer'),
                  (Electricien_Automobile, 'Electricien Automobile'),
                  (Mecanicien_Automobile, 'Mecanicien Automobile'),
                  (Mecanicien_motocycle, 'Mecanicien motocycle'),
                  (Monteur_en_pneumatique, 'Monteur en pneumatique'),
                  (Peintre_en_carroserie, 'Peintre en carroserie'),
                  (Technicien_en_Mecanique, 'Technicien en Mecanique')]

    contrat = [(CDI, 'CDI'), (CDD, 'CDD')]

    id = models.BigAutoField(primary_key=True)
    nom = models.CharField(max_length=254)
    prenom = models.CharField(max_length=254)
    date_de_naissance = models.DateField(auto_now=False, auto_now_add=False)
    type_de_contrat = models.CharField(max_length=254, choices=contrat)
    addresse = models.CharField(max_length=254)
    salaire = models.CharField(max_length=254)
    cni = models.IntegerField()
    telephone = models.IntegerField()
    poste = models.CharField(max_length=254, choices=Poste, default=Carrosier)
    specialite = models.CharField(max_length=254, choices=Speciality, default=Electricien_Automobile)
    profile = models.ImageField(upload_to='pics_employe')
    Garage = models.ForeignKey('Garage', on_delete=models.SET_NULL, default='', null=True, blank=True)

    class Meta:
        db_table = 'employe'
        ordering = ['nom']

    def __str__(self):
        return self.nom


class Facturation(models.Model):
    id = models.BigAutoField(primary_key=True)
    reference = models.CharField(max_length=250, unique=True)
    libelle = models.CharField(max_length=254)
    montant = models.IntegerField()
    date = models.DateField(auto_now=False, auto_now_add=False)
    client = models.ManyToManyField('Client', blank=True)
    employer = models.ForeignKey('Employe', on_delete=models.SET_NULL, default='', null=True, blank=True)

    class Meta:
        db_table = 'facturation'
        ordering = ['reference']


class Garage(models.Model):
    Reparateur_agrée_par_les_constructeur = 'Reparateur agrée par les constructeur'
    Mécanicien_Réparateur_Automobile = 'Mécanicien Réparateur Automobile'
    Type_garage = [(Reparateur_agrée_par_les_constructeur, 'Reparateur agrée par les constructeur'),
                   (Mécanicien_Réparateur_Automobile, 'Mécanicien Réparateur Automobile(MRA)')]

    id = models.BigAutoField(primary_key=True)
    nom_garage = models.CharField(max_length=254, unique=True)
    type_garage = models.CharField(max_length=50, choices=Type_garage, default=Reparateur_agrée_par_les_constructeur)
    date_creation_garage = models.DateField(auto_now=False, auto_now_add=False)
    telephone = models.CharField(max_length=254, default='')
    address = models.CharField(max_length=254, default='')
    logo = models.ImageField(upload_to='pics_garage', default='')
    numbre_employer = models.IntegerField(default=1)
    employer = models.ForeignKey('Employe', on_delete=models.SET_NULL, default='', null=True, blank=True)
    vehicule = models.ManyToManyField('Vehicules', blank=True)

    class Meta:
        db_table = 'garage'
        ordering = ['nom_garage']


class Intervention(models.Model):
    Remorquage = 'Remorquage'
    Depannage = 'Depannage'
    Consultation_Externe = 'Consultation Externe'

    Type_intervention = [(Remorquage, 'Remorquage'), (Depannage, 'Depannage'),
                         (Consultation_Externe, 'Consultation Externe')]
    id = models.BigAutoField(primary_key=True)
    description = models.TextField(max_length=254)
    date_debut = models.DateField()
    date_fin = models.DateField(blank=True)
    duree = models.TimeField(blank=True)
    activite = models.TextField(max_length=254)
    observation = models.TextField(max_length=254, blank=True)
    employer = models.ManyToManyField('Employe', blank=True)
    type_intervention = models.CharField(max_length=254, choices=Type_intervention, default=Remorquage)
    client = models.ForeignKey('Client', on_delete=models.SET_NULL, default='', null=True, blank=True)
    vehicule = models.ManyToManyField('vehicules', blank=True)

    class Meta:
        db_table = 'intervention'
        ordering = ['duree']


class Laverie(models.Model):
    id = models.BigAutoField(primary_key=True)
    prix = models.IntegerField()
    employer = models.ForeignKey('Employe', on_delete=models.SET_NULL, default='', null=True, blank=True)
    vehicule = models.ForeignKey('Vehicules', on_delete=models.SET_NULL, default='', null=True, blank=True)

    class Meta:
        db_table = 'laverie'


class Locations(models.Model):
    id = models.BigAutoField(primary_key=True)
    date_location = models.DateField(auto_now=False, auto_now_add=False)
    montant = models.IntegerField()
    date_retour = models.DateField()
    vehicule = models.ManyToManyField('Vehicules', blank=True)
    client = models.ForeignKey('Client', on_delete=models.SET_NULL, default='', null=True, blank=True)

    class Meta:
        db_table = 'locations'
        ordering = ['date_location']


class RendezVous(models.Model):
    id = models.BigAutoField(primary_key=True)
    date_rdv = models.DateField(auto_now=False, auto_now_add=False)
    type_rdv = models.CharField(max_length=254)
    description = models.CharField(max_length=254)
    clients = models.ManyToManyField('Client', blank=True)

    class Meta:
        db_table = 'rendez_vous'
        ordering = ['date_rdv']


class Stock(models.Model):
    id = models.BigAutoField(primary_key=True)
    image = models.ImageField(upload_to='pics_piece')
    employer = models.ManyToManyField('Employe', blank=True)
    piece = models.ManyToManyField('Pieces', blank=True)

    class Meta:
        db_table = 'stock'


class Voiture(models.Model):
    id = models.BigAutoField(primary_key=True)
    marque = models.CharField(max_length=254)
    modele = models.CharField(max_length=254)
    version = models.CharField(max_length=254)
    genre = models.CharField(max_length=254)
    carrosserie = models.CharField(max_length=254)
    energie = models.CharField(max_length=254)
    couleur = models.CharField(max_length=254)
    ingredient = models.CharField(max_length=254)



class Vehicules(models.Model):
    id = models.BigAutoField(primary_key=True)
    immatriculation = models.CharField(max_length=254)
    couleur = models.CharField(max_length=254)
    marque = models.CharField(max_length=254)
    num_chasis = models.CharField(unique=True, max_length=17, default=1, validators=[RegexValidator(r'^\d{1,17}$')])
    nb_chevaux = models.IntegerField()
    modele = models.CharField(max_length=254)
    type_moteur = models.CharField(max_length=254)
    nb_places = models.CharField(max_length=254)
    nb_portieres = models.IntegerField(default=1)
    num_portieres = models.CharField(unique=True, max_length=17, default=1,validators=[RegexValidator(r'^\d{1,17}$')])
    description = models.CharField(max_length=254)
    client = models.ForeignKey(Client,on_delete=models.SET_NULL, default='', null=True, blank=True )


    class Meta:
        db_table = 'vehicules'
        ordering = ['marque']

    def __str__(self):
        return self.marque + ' ' + self.modele


class Pieces(models.Model):
    id = models.BigAutoField(primary_key=True)
    nom_piece = models.CharField(max_length=254)
    modele_piece = models.CharField(max_length=254)
    fabricant = models.CharField(max_length=254)
    quantite = models.IntegerField()

    class Meta:
        db_table = 'pieces'
        ordering = ['nom_piece']


class User(AbstractUser):
    email = models.EmailField(verbose_name="email", max_length=254, unique=True)
    cpassword = models.CharField(max_length=254, blank=False, default='')
    phone = models.CharField(null=True, max_length=254)
    REQUIRED_FIELDS = ['first_name', 'last_name', 'username', 'phone']

    USERNAME_FIELD = "email"

    class Meta:
        db_table = 'user'

    def get_username(self):
        return self.email
