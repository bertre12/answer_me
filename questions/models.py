from django.db import models


# Вопросы.
class Question(models.Model):
    question_text = models.CharField(max_length=255, verbose_name='Вопрос')
    pub_date = models.DateTimeField('дата публикации')

    def __str__(self):
        return self.question_text

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'


# Ответ.
class Choice(models.Model):
    # Связь один к одному.
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=255, verbose_name='Ответ')
    votes = models.IntegerField(default=0, verbose_name='голоса')

    def __str__(self):
        return self.choice_text

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'
