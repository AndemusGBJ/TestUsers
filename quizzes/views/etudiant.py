from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator, EmptyPage
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from quizzes.forms.etudiant import EtudiantForm
from quizzes.models.etudiant import Etudiant


def add_student(request):
    return render(request, 'u_quizzes/etudiants/add-student.html', locals())


def edit_student(request):
    return render(request, 'u_quizzes/etudiants/edit-student.html', locals())

def list_student(request):
    return render(request, 'u_quizzes/etudiants/students.html', locals())

def details_student(request):
    return render(request, 'u_quizzes/etudiants/student-details.html', locals())

@login_required
def list_etudiants(request):
    select = "etudiants"
    list_etudiants=Etudiant.objects.all()

    #Pagination : 10 éléments par page
    paginator = Paginator(list_etudiants, 10)
    try:
        page = request.GET.get("page")
        if not page:
            page = 1
        list_etudiants = paginator.page(page)

    except EmptyPage:
        #si on dépasse la limite des pages on prends la dernière
        list_etudiants=paginator.page(paginator.num_pages())

    return render(request, "u_quizzes/etudiants/list-etudiants.html", locals())

class CreateEtudiant(CreateView, LoginRequiredMixin):
    model = Etudiant
    form_class = EtudiantForm
    template_name = "u_quizzes/etudiants/etudiantForm.html"

    def get_success_url(self):
        return reverse_lazy("quizzes:details", kwargs={"pk": self.object.id})


class UpdateEtudiant(UpdateView, LoginRequiredMixin):
    model = Etudiant
    form_class = EtudiantForm
    template_name = "u_quizzes/etudiants/etudiantForm.html"

    def get_success_url(self):
        return reverse_lazy("quizzes:details", kwargs={"pk": self.object.id})