from django.urls import path

from PercomGarage import views


urlpatterns = [
    # Path for login
    path("", views.login, name="login"),
    path("home/", views.index, name="index"),
    path("Garage/register", views.register, name="register"),
    path("Employer/register", views.employe_regis, name="employe_regis"),
    path("signup", views.signupinfo, name="signupinfo"),
    path("home/logout", views.logout, name="logout"),
    path("garagelogin", views.garagelogin, name="garagelogin"),







    path("home/voiture", views.add_voiture, name="voiture"),
    path("home/list_client/<str:id>", views.detail_client, name="detail"),
    path("home/add_client/", views.add_client, name="add_client"),
    path("home/list_client/", views.list_client, name="list_client"),
    path("home/list_client/update/<str:id>", views.update_client, name="update"),
    path("home/list_client/delete/<str:id>", views.delete_client, name="delete"),
    path("home/add_employer/", views.add_employer, name="add_employer"),
    path("list_employer/update/<str:id>", views.update_employer, name="update_employer"),
    path("list_employer/delete/<str:id>", views.delete_employer, name="delete_employer"),
    path("home/list_employer/", views.list_employer, name="list_employer"),
    path("home/add_intervention/", views.add_intervention, name="add_intervention"),
    path("list_intervention/update/<str:id>", views.update_intervention, name="update_intervention"),
    path("list_intervention/delete/<str:id>", views.delete_intervention, name="delete_intervention"),
    path("home/list_intervention/", views.list_intervention, name="list_intervention"),



    # path("add_employer/", views.add_employer, name="add_employer"),
    # path("edit_employer/<int:id>", views.edit_employer),
    # path("list_employer/", views.list_employer, name="list_employer"),
    # path("update_employer/<int:id>", views.update_employer),
    # path("delete_employer/<int:id>", views.delete_employer),

]