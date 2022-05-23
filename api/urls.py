from django.urls import path
from rest_framework_swagger.views import get_swagger_view

from api import views

urlpatterns = [
    # Url API
    path("UserAuth/", views.UserAuth.as_view()),

    #===================Client Route=========================#

    path("Clientlist/", views.ClientList.as_view()),
    path("ClientCreate/", views.ClientCreate.as_view()),
    path("ClientUpdate/<int:pk>", views.ClientUpdate.as_view()),
    path("ClientDetail/<str:pk>", views.ClientDetail.as_view()),

    # ===================Client Route=========================#

    # ===================Commande Route=========================#
    path("Commandelist/", views.CommandeList.as_view()),
    path("CommandeDetail/<str:pk>", views.CommandeDetail.as_view()),

    # ===================Commande Route=========================#

    # ===================Employer Route=========================#
    path("Employelist/", views.EmployeList.as_view()),
    path("EmployeDetail/<str:pk>", views.EmployesDetail.as_view()),

    # ===================Employer Route=========================#

    # ===================Facturation Route=========================#
    path("Facturelist/", views.FacturationList.as_view()),
    path("FactureDetail/<str:pk>", views.FactureDetail.as_view()),

    # ===================Facturation Route=========================#

    # ===================Garage Route=========================#
    path("GarageDetail/<str:pk>", views.GarageDetail.as_view()),
    path("GarageList/", views.GarageList.as_view()),

    # ===================Garage Route=========================#

    # ===================Intervention Route=========================#
    path("Interventionlist/", views.InterventionList.as_view()),
    path("InterventionDetail/<str:pk>", views.InterventionDetail.as_view()),

    # ===================Intervention Route=========================#

    # ===================Laverie Route=========================#
    path("Laverielist/", views.LaverieList.as_view()),
    path("LaverieDetail/<str:pk>", views.LaverieDetail.as_view()),

    # ===================Laverie Route=========================#

    # ===================Locations Route=========================#
    path("Locationlist/", views.LocationList.as_view()),
    path("LocationDetail/<str:pk>", views.LocationDetail.as_view()),

    # ===================Locations Route=========================#

    # ===================RendezVous Route=========================#
    path("RendezVouslist/", views.RendezVousList.as_view()),
    path("RendezVousDetail/<str:pk>", views.RendezVousDetail.as_view()),

    # ===================RendezVous Route=========================#

    # ===================Stock Route=========================#
    path("Stocklist/", views.StockList.as_view()),
    path("StockDetail/<str:pk>", views.StockDetail.as_view()),

    # ===================Stock Route=========================#

    # ===================Vehicule Route=========================#
    path("VoitureList/", views.VoitureList.as_view()),
    path("VoitureDetail/<str:pk>", views.VoitureDetail.as_view()),

    # ===================Vehicule Route=========================#

    # ===================Piece Route=========================#
    path("PieceList/", views.PieceList.as_view()),
    path("PieceDetail/<str:pk>", views.PieceDetail.as_view()),
    # ===================Vehicule Route=========================#






    # path("listclient/", views.listclient, name="list client"),
    # path("Detailclient/<str:pk>/", views.Detailclient, name="Detail client"),
    # path("Ajoutclient/", views.Ajoutclient, name="Ajouter client"),
    # path("Updateclient/<str:pk>/", views.Updatelient, name="Update client"),
    # path("Deleteclient/<str:pk>/", views.Deleteclient, name="Delete client"),
    # path("Ajoutgarage/", views.Ajoutgarage, name="Ajout garage"),
    # path("listgarage/", views.listgarage, name="list garage"),
    # path("updategarage/<str:pk>/", views.Updategarage, name="update garage"),
    # path("deletegarage/<str:pk>/", views.Deletegarage, name ="delete garage"),
    # path("detailgarage/<str:pk>/", views.Detailgarage, name ="detail garage"),
]
