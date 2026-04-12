from django.contrib import admin
from django.urls import path
from gestion_stock import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_view, name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('gestionnaire/', views.gestionnaire_view, name='gestionnaire'),
    path('gestionnaire/ajouter/', views.ajouter_produit, name='ajouter_produit'),
    path('gestionnaire/modifier/<int:pk>/', views.modifier_produit, name='modifier_produit'),
    path('gestionnaire/supprimer/<int:pk>/', views.supprimer_produit, name='supprimer_produit'),
    path('mouvements/', views.mouvement_view, name='mouvements'),
    path('secretaire/', views.secretaire_view, name='secretaire'),
    path('utilisateurs/', views.utilisateurs_view, name='utilisateurs'),
    path('utilisateurs/creer/', views.creer_utilisateur, name='creer_utilisateur'),
    path('utilisateurs/toggle/<int:pk>/', views.toggle_utilisateur, name='toggle_utilisateur'),
    path('utilisateurs/supprimer/<int:pk>/', views.supprimer_utilisateur, name='supprimer_utilisateur'),
    path('export/excel/', views.export_excel, name='export_excel'),
    path('export/pdf/', views.export_pdf, name='export_pdf'),
]
