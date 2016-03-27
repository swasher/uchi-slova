# coding: utf-8

from django.db import models
from accounts.models import CustomizedUser


class Slova(models.Model):
    eng = models.CharField(max_length=50, verbose_name='По-английски', help_text='')    # по английски
    rus = models.CharField(max_length=150, verbose_name='По-русски', help_text='')      # по русски
    points = models.IntegerField(verbose_name='', default=0)   # сколько раз ответили удачно ("вспомнили"). За удачный ответ
                                                               # +1 очко, за неудачный - минус 2. Слово считается выученным, когда
                                                               # кол-во очков достигнет определенного значения, заданного пользователем.
    user = models.ForeignKey(CustomizedUser)                # ссылка на владельца
    remembered = models.BooleanField(default=False)         # слово уже запомнено

    class Meta:
        verbose_name = 'Слово'
        verbose_name_plural = 'Слова'

    def __unicode__(self):
        return self.name