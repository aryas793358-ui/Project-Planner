
# Create your models here.
from django.db import models

# Create your models here.
from django .contrib.auth.models import AbstractUser

class RoleChoices(models.TextChoices):

    DEVELOPER='Developer','Developer'

    ADMIN='Admin','Admin'

    PROJECT_COORDINATOR='Project Coordinator','Project Coordinator'

class TechChoices(models.TextChoices):

     FRONTEND='Frontend Developer','Frontend Developer'
     BACKEND='Backend Developer','Backend Developer'
     FULLSTACK='Full Stack Developer','Full Stack Developer'
     UIUX='UI/UX Designer','UI/UX Designer'
     TESTER='Software Tester','Software Tester'

class Profile(AbstractUser):

    role=models.CharField(max_length=20,choices=RoleChoices.choices)

    tech=models.CharField(max_length=20,choices=TechChoices.choices,null=True,blank=True)

    class Meta:

        verbose_name='profiles'

        verbose_name_plural='profiles'

    def __str__(self):

            return f'{self.username}-{self.role}-{self.tech}'
