from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView

from quizzes.models.etudiant import Etudiant
from quizzes.views import accueil, etudiant, epreuve

from django.urls import path

app_name = 'quizzes'

urlpatterns = [

    #Url pour la page d'accueil
    path('Accueil/', accueil.index, name='accueil'),

    #Urls pour les quizzes
    path('add_quiz/', epreuve.add_quiz, name='ajout_epreuve'),
    path('edit_quiz/', epreuve.edit_quiz, name='modifier_epreuve'),
    path('list_quizzes/', epreuve.list_quizzes, name='toutes_les_epreuves'),
    path('details_quiz/', epreuve.details_quiz, name='dtails_epreuve'),

    #urls pour les étudiants
    path('add_student/', etudiant.add_student, name='ajout_etudiant'),
    path('edit_student/', etudiant.edit_student, name='modifier_etudiant'),
    path('list_students/', etudiant.list_student, name='tous_les_etudiants'),
    path('details_student/', etudiant.details_student, name='details_etudiant'),


    path('etudiants/', etudiant.list_etudiants, name="etudiants"),
    path('etudiants/creer', etudiant.CreateEtudiant.as_view(), name="creer"),
    path('etudiants/modifier/<int:pk>/', etudiant.UpdateEtudiant.as_view(), name="modifier"),
    path('etudiants/<int:pk>/',
         login_required(DetailView.as_view(model=Etudiant, template_name="u_quizzes/etudiants/details-etudiant.html")), name='details'),

]