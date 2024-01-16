from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse#
from .models import QuizLibary, Question
from django.core.serializers import serialize
from django.core.serializers import serialize
from django.http import JsonResponse

# Create your views here.

class QuizForm(forms.ModelForm):
    class Meta:
        model= Question
        
        fields = ['Question', 'Answer1', 'Answer2', 'Answer3', 'Answer4','CorrectAnswerIndex']


def index(request):

    

    quiz = QuizLibary()
    print(quiz)

    if quiz == "None :":
        print("No active quiz.")
        return render(request, "QuizQuaz/error.html", {"message": "No active quiz."})
    
       

    
    form = QuizForm()

    if request.method == "POST":
        form = QuizForm(request.POST)
        if form.is_valid():
            form.save()
            #Question.objects.create(Question=request.POST["Question"], Answer1=request.POST["Answer1"], Answer2=request.POST["Answer2"], Answer3=request.POST["Answer3"], Answer4=request.POST["Answer4"], CorrectAnswerIndex=request.POST["CorrectAnswerIndex"])
            
            
            
            return HttpResponseRedirect(reverse("index"))
        


    
    return render(request, "QuizQuaz/index.html", {'form': form} )






def quiz(request, id):

    try:
        quiz_id = int(id)
    except ValueError:
        return render(request, "QuizQuaz/error.html", {"message": "Invalid quiz id."})

    #chck if quiz exists
    try:
        quiz = QuizLibary.objects.get(pk=quiz_id)
    except QuizLibary.DoesNotExist:
        return render(request, "QuizQuaz/error.html", {"message": "Quiz does not exist."})
    


    
    questions = quiz.Questions.all()

    quiz_json = serialize('json', [quiz])
    questions_json = serialize('json', questions)
    return render(request, "QuizQuaz/quiz.html" )

def quiz_data_view(request, id):
    quiz = QuizLibary.objects.get(pk=1)
    quizmaster = quiz.Quizmaster


    questions = []
    answers = []
    correctanswer = []

    for question in quiz.Questions.all():
        questions.append(question.Question)
        correctanswer.append(question.CorrectAnswerIndex)
        answers.append([
            question.Answer1,
            question.Answer2,
            question.Answer3,
            question.Answer4,

        
        ])




    return JsonResponse({

        'quizmaster': quizmaster,
        'questions': questions,
        'answers': answers,
        'correctanswer': correctanswer

        
    })

    
    