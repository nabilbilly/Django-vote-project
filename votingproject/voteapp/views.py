from django.template import loader
from django.shortcuts import redirect, render 
from django.http import HttpResponse, HttpResponseRedirect
from voteapp.models import Question,choice,name,Image
from django.shortcuts import get_object_or_404
from django.urls import reverse
 # i added this because of the image uplaods
# from .forms import ImageForm  
# from .models import UploadImage  




# Create your views here.
#Get question displayed 
# def election(request):
#     # passin in data to loop through and show the Question. i was able to acess something from the database using this
#     list_latest_question = Question.objects.order_by('vote_date')[:5]
#     context = {'list_latest_question': list_latest_question}
#     #research
#     data = Image.objects.all()
#     context = {
#         'data' : data
#     }
#     return render(request,"display.html", context)

#     return  render(request,'index.html', context)
def election(request):
    list_latest_question = Question.objects.order_by('vote_date')[:5]
    data = Image.objects.all()
    context = {
        'list_latest_question': list_latest_question,
        'data': data,
    }
    return render(request, 'index.html', context)


#show specific question and choice, so if you vote now is been clicked it loop through to print on the next page
def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except:
        raise Http404("Question does not exist ")
    list_latest_question = Question.objects.order_by('vote_date')[:5]
    context = {'list_latest_question': list_latest_question}
    return  render(request,'vnow_result.html', context)


def display(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "results.html", {"question": question})




  
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
  


def index(request):
    data = Image.objects.all()
    context = {
        'data' : data
    }
    return render(request,"index.html", context)

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