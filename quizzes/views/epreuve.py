from django.shortcuts import render


def add_quiz(request):
    return render(request, 'u_quizzes/epreuves/add-quiz.html')


def edit_quiz(request):
    return render(request, 'u_quizzes/epreuves/edit-quiz.html')

def list_quizzes(request):
    return render(request, 'u_quizzes/epreuves/quizzes.html')

def details_quiz(request):
    return render(request, 'u_quizzes/epreuves/quiz-details.html')