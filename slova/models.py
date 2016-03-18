# coding: utf-8
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, email, password, **kwargs):
        if not email:
            raise ValueError('Email должен быть указан')

        user = self.model(
            email=UserManager.normalize_email(email),
            **kwargs
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **kwargs):
        user = self.create_user(email, password, **kwargs)
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class CustomizedUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField('Электронная почта', max_length=255, unique=True, db_index=True)
    first_name = models.CharField('Имя', max_length=30, blank=True)
    last_name = models.CharField('Фамилия', max_length=30, blank=True)
    verified_email = models.BooleanField(default=False)
    remember_level = models.IntegerField(default=20)
    register_date = models.DateField('Дата регистрации', auto_now_add=True)
    is_active = models.BooleanField('Активен', default=True)
    is_admin = models.BooleanField('Суперпользователь', default=False)
    #is_staff = models.BooleanField('Суперпользователь', default=False)

    # Этот метод обязательно должен быть определён
    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    # Требуется для админки
    @property
    def is_staff(self):
        # "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

    def __str__(self):
        return self.email

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


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