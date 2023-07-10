from django.template import loader
from django.shortcuts import redirect, render 
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from voteapp.models import Question,choice,name,Image
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, auth
import datetime


def logins(request):
    if request.method == 'POST':
        username = request.POST['name']
        password = request.POST['password']

        user = auth.authenticate(username=username, password = password)

        if user is not None:
            auth.login(request, user)
            # return render(request, 'index.html')
            return redirect('dashbord/')
        else:
            messages.info(request, "Invalid credentials")
            return redirect('/')
    return render(request, 'logins.html')


def register(request):
    now = datetime.datetime.now()
    if request.method == 'POST':
        firstname = request.POST['fname']
        lastname = request.POST['lname']
        student_id = request.POST['sid']
        bday = request.POST['bday']
        htown = request.POST['htown']
        skill = request.POST['class']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        gender = request.POST['gender']
        # question = request.POST['question'] 
        username = lastname +' ' +firstname 

        if password == cpassword:
            if User.objects.filter(username = username).exists():
                messages.info(request, "Username Taken")
                return redirect('/register/student')
            else:
                user = User.objects.create_user(username=username, first_name=firstname, last_name=lastname, password=password)
                user.save()
                profile = UsersDetail.objects.create(Name=username, Gender=gender, Student_id= student_id , birth_date= bday, Hometown=htown, Class= skill, position = "student", start_date=now.strftime("%Y-%m-%d"))
                profile.save()
                return redirect('/')
            messages.info(request, "Password mismatch")
            return redirect('vote:logins')

    return render(request, 'register.html')

@login_required(login_url='/')
def logout(request):
    auth.logout(request)
    return redirect('/')







@login_required(login_url='/')
def election(request):
    list_latest_question = Question.objects.order_by('vote_date')[:5]
    data = Image.objects.all()
    context = {
        'list_latest_question': list_latest_question,
        'data': data,
    }
    return render(request, 'index.html', context)


#show specific question and choice, so if you vote now is been clicked it loop through to print on the next page
@login_required(login_url='/')
def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except:
        raise Http404("Question does not exist ")
    list_latest_question = Question.objects.order_by('vote_date')[:5]
    context = {'list_latest_question': list_latest_question}
    return  render(request,'vnow_result.html', context)

@login_required(login_url='/')
def display(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "results.html", {"question": question})




@login_required(login_url='/') 
def votes(request, question_id):

    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request,'vnow_result.html', {'question': question, 'error_message': "You didn't select a choice."}  
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("vote:display", args=(question.id,)))
  

@login_required(login_url='/')
def index(request):
    data = Image.objects.all()
    context = {
        'data' : data
    }
    return render(request,"index.html", context)


@login_required(login_url='/')
def profile(request):
    user = User.objects.get(username=request.user.username)
    new = UsersDetail.objects.filter(Name = user).first()
    if new is not None:
        return render(request, 'mainIndex.html', {'name':new.Name, 'bday':new.birth_date, 'add':new.Street, 'skill': new.Class,  'role':new.position})
    else:
        print("sorry")
    return render(request, 'mainIndex.html')

def pop(request):
    return render(request, "bing.html")

# def test(request):
#     # passin in data to loop through and show the Question. i was able to acess something from the database using this
    
#     #research

#     return  render(request,'mainIndex.html')





















# def images(request):
#     question = Question.objects.all()
#     context = {'question': question}
#     return render(request, 'index.html', context)


# def image_upload(request):

#     images = UploadImage.objects.all()
#     context = {
#         'form': form,
#         'images': images,
#     }
#     return render(request, 'index.html', context)



# # image upload section field 
# # def image_request(request):  
# #     if request.method == 'POST':  
# #         form = UserImage(request.POST, request.FILES)  
# #         if form.is_valid():  
# #             form.save()  
  
# #             # Getting the current instance object to display in the template  
# #             img_object = form.instance  
              
# #             return (request, 'index.html', {'form': form, 'img_obj': img_object})  
# #     else:  
# #        form = UserImage()  
  
# #     return render(request, 'index.html', {'form': form})  
# # # Create your views here.