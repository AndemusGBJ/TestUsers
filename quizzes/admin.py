from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from quizzes.models.epreuve import Epreuve
from quizzes.models.etudiant import Etudiant
from quizzes.models.questionaire import Questionaire
from quizzes.models.reponses import Reponse
from quizzes.models.validationEpreuve import ValidationEpreuve

class QuestionaireInlineAdmin(admin.TabularInline):
    model = Questionaire
    extra = 0





@admin.register(Etudiant)
class EtudiantAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('name', 'lastname', 'email', 'telephone', 'login','pwd')
    list_per_page = 10


@admin.register(Epreuve)
class EpreuveAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    inlines = [QuestionaireInlineAdmin]
    list_display = ('titre', 'description', 'ponderation', 'date', 'duree')
    list_per_page = 10

    prepopulated_fields = {'slug': ('titre',)}



@admin.register(Reponse)
class ReponseAdmin(ImportExportModelAdmin):
    list_display = ('contenu', 'pointsObtenus', 'idQuestion')
    readonly_fields = ('contenu', 'pointsObtenus', 'idQuestion')






@admin.register(ValidationEpreuve)
class ValidationEpreuveAdmin(ImportExportModelAdmin):
    list_display = ('epreuve', 'user', 'validation')

