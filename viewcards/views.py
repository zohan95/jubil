from unicodedata import category
from django.shortcuts import render
from django.views import View
from .models import *
import openpyxl


# def cardshower(request):
#     courses = CourseJubil.objects.all()
#     categorys = WordsCategory.objects.all()
#     tmp = {}
#     for i in courses:
#         tmp1 = []
#         tmp_obj = WordsCategory.objects.filter(course_jubil=i.id)
#         tmp1 = [k.words_category for k in tmp_obj]
#         #print(tmp1)
#         tmp[i.course_jubil]=tmp1
#     #print(tmp)
#     return render(request, 'viewcards/main.html',{'title':'Карточки из документа', 'courses': courses, 'categorys':categorys,'catdict':tmp})

def mainmenu(request):
    courses = CourseJubil.objects.all()
    categorys = WordsCategory.objects.all()
    tmp = {}
    theory = {}
    for i in courses:
        tmp1 = []
        tmp_obj = WordsCategory.objects.filter(course_jubil=i.id)
        tmp1 = [k.words_category for k in tmp_obj]
        #print(tmp1)
        tmp[i.course_jubil]=tmp1
        tmp_obj = Theory.objects.filter(course_jubil=i.id)
        if tmp_obj:
            for k in tmp_obj:
                theory[str(k.id)] = k.name
    print(theory)
    #print(tmp)
    return render(request, 'viewcards/base.html',{'title':'Карточки из документа', 'courses': courses, 'categorys':categorys,'catdict':tmp,'theory':theory})


class ShowTheory(View):
    def get(self, request, pk):
        body = Theory.objects.get(id=pk)
        return render(request, 'viewcards/theory.html', {'theorybody':body})



class Upload(View):
    def get(self, request):
        courses = CourseJubil.objects.all()
        categorys = WordsCategory.objects.all()
        return render(request, 'viewcards/upload.html',{'course':courses, 'category':categorys})
    
    def post(self, request):
        excel_file = request.FILES['files']
        interest = request.POST.get('course')
        toto = request.POST.get('category')

        wb = openpyxl.load_workbook(excel_file)
        worksheet = wb.active
        for i in range(0, worksheet.max_row):
            post = WordsContainer(
                rus_word = worksheet['A'+str(i+1)].value,
                end_word = worksheet['B'+str(i+1)].value,
                words_category = WordsCategory.objects.get(words_category=toto)
            )
            post.save()

        
        #print(interest, toto)

        
        wb.close()
        return render(request, 'viewcards/base.html')


class ViewById(View):
    def get(self, request, course, category):
        courses = CourseJubil.objects.all()
        categorys = WordsCategory.objects.all()
        tmp2 = {}
        for i in courses:
            tmp1 = []
            tmp_obj = WordsCategory.objects.filter(course_jubil=i.id)
            tmp1 = [k.words_category for k in tmp_obj]
            #print(tmp1)
            tmp2[i.course_jubil]=tmp1
        #request.GET.get('course')
        print(category)
        lol = WordsCategory.objects.get(words_category=category)
        tmp = WordsContainer.objects.filter(words_category=lol)
        tmp_dict = []
        for i in tmp:
            tmp_dict.append([i.rus_word, i.end_word])
        tmp_words = [i.rus_word for i in tmp]
        return render(request, 'viewcards/main.html', {'words':tmp_words,'translates':tmp_dict,'title':category, 'courses': courses, 'categorys':categorys,'catdict':tmp2})