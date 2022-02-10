from django.shortcuts import render
from django.views import View
from .models import *
import openpyxl


def cardshower(request):
    return render(request, 'viewcards/main.html',{'title':'Карточки из документа'})



class Upload(View):
    def get(self, request):
        return render(request, 'viewcards/upload.html')
    
    def post(self, request):
        excel_file = request.FILES['files']
        # response = HttpResponse(
        #     content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
        # )
        # response['Content-Disposition'] = 'attachment; filename={date}-{id}.xlsx'.format(
        #     date=datetime.datetime.now().strftime('%Y-%m-%d'), id=randint(1,10000000)
        # )

        # wb2 = openpyxl.Workbook()
        # ws = wb2.active
        wb = openpyxl.load_workbook(excel_file)
        worksheet = wb.active
        for i in range(0, worksheet.max_row):
            post = WordsContainer(
                rus_word = worksheet['A'+str(i+1)].value,
                end_word = worksheet['B'+str(i+1)].value,
                words_category = WordsCategory.objects.get(words_category='Из документа')
            )
            post.save()



        # wb2.save(response)
        wb.close()
        return render(request, 'viewcards/base.html')
