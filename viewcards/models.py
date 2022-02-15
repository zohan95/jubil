from django.db import models
from tinymce.models import HTMLField


class Theory(models.Model):
    name = models.CharField(max_length=511, help_text='Заголовок')
    bodycontent = HTMLField()
    course_jubil = models.ForeignKey('CourseJubil', on_delete=models.CASCADE)

class WordsContainer(models.Model):
    rus_word = models.CharField(max_length=127, help_text='russian word')
    end_word = models.CharField(max_length=127, help_text='eng word')
    words_category = models.ForeignKey('WordsCategory', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.rus_word

class WordsCategory(models.Model):
    words_category = models.CharField(max_length=127)
    course_jubil = models.ForeignKey('CourseJubil', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.words_category



class CourseJubil(models.Model):
    course_jubil = models.IntegerField(default=0)

    def __str__(self) -> str:
        return str(self.course_jubil)

