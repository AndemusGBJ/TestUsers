from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView

from quizzes.models.epreuve import Epreuve
from quizzes.models.etudiant import Etudiant
from quizzes.models.questionaire import Questionaire
from quizzes.views import accueil, etudiant, epreuve, validationEpreuve

from django.urls import path

app_name = 'quizzes'

urlpatterns = [

    #Url pour la page d'accueil
    path('', accueil.index, name='accueil'),
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

    path('mes_epreuves/<slug:slug>/questions/', validationEpreuve.list_questions, name="questions"),
    path('mes_epreuves/<slug:slug>/questions/resultats', validationEpreuve.resultats, name="resultats"),
    #path('reponses/enregistrer/', validationEpreuve.CreateReponse.as_view(), name="enregistrer"),
    #path('question/repondre/', validationEpreuve.new_response, name="repondre"),
    #path('epreuves/', validationEpreuve.list_epreuves, name="epreuves"),
    path('mes_epreuves/', validationEpreuve.list_validations, name="mes_epreuves"),
    path('mes_epreuves/<slug:slug>/questions/<int:id>', validationEpreuve.new_response, name="reponse"),


    path('mes_epreuves/<slug:slug>/',
             login_required(DetailView.as_view(model=Epreuve, template_name="u_quizzes/validationEpreuve/quiz-intro.html")), name='intro'),


]