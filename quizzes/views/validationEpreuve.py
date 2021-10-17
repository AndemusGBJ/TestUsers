from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator, EmptyPage
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from quizzes.forms.reponse import ReponseForm
from quizzes.models.epreuve import Epreuve
from quizzes.models.questionaire import Questionaire
from quizzes.models.reponses import Reponse
from quizzes.models.validationEpreuve import ValidationEpreuve


@login_required
def list_questions(request):
    select = "questionnaire"
    list_questions=Questionaire.objects.all()

    #Pagination : 1 éléments par page
    paginator = Paginator(list_questions, 1)
    try:
        page = request.GET.get("page")
        if not page:
            page = 1
        list_questions = paginator.page(page)

    except EmptyPage:
        #si on dépasse la limite des pages on prends la dernière
        list_questions = paginator.page(paginator.num_pages())

    return render(request, "u_quizzes/validationEpreuve/reponseForm.html", locals())

@login_required()
def list_epreuves(request):
    select = "epreuve"
    list_epreuves = Epreuve.objects.all()

    # Pagination : 1 éléments par page
    paginator = Paginator(list_epreuves, 5)
    try:
        page = request.GET.get("page")
        if not page:
            page = 1
        list_epreuves = paginator.page(page)

    except EmptyPage:
        # si on dépasse la limite des pages on prends la dernière
        list_epreuves = paginator.page(paginator.num_pages())

    return render(request, "u_quizzes/validationEpreuve/quiz-list.html", locals())

@login_required()
def list_validations(request):
    select = "epreuve"
    list_epreuves = ValidationEpreuve.objects.all()

    # Pagination : 1 éléments par page
    paginator = Paginator(list_epreuves, 5)
    try:
        page = request.GET.get("page")
        if not page:
            page = 1
        list_epreuves = paginator.page(page)

    except EmptyPage:
        # si on dépasse la limite des pages on prends la dernière
        list_epreuves = paginator.page(paginator.num_pages())

    return render(request, "u_quizzes/validationEpreuve/quiz-list.html", locals())

class CreateReponse(CreateView, LoginRequiredMixin):
    model = Reponse
    form_class = ReponseForm
    template_name = "u_quizzes/validationEpreuve/reponseForm.html"

    def get_success_url(self):
        #return reverse_lazy("quizzes:details", kwargs={"pk": self.object.id})
        pass