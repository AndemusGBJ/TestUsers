from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render




@login_required
def index(request):

    return render(request, 'u_quizzes/index.html', locals())