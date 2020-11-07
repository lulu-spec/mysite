from django.db import models
from django.utils import timezone
import datetime
# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200, verbose_name='Pregunta')
    pub_date = models.DateTimeField(verbose_name='fecha de publicacion')

    def __str__(self):
        return self.question_text
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    class Meta:
        verbose_name='Pregunta'
        verbose_name_plural='Encuesta'
        
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200, verbose_name='Elija una respuesta')
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
    
 