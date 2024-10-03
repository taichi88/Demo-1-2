from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=100, default="Name")
    surname = models.CharField(max_length=100, default="Surname")
  
    personal_thoughts = models.TextField()


class Book(models.Model):
    title = models.CharField(max_length=100, default="Title")
    description = models.TextField()
    #author mogvianebit shevqmni rodesac gavaketeb avtoris klass
    #shevqmenit autoris klasi exla ki am filds unda gadavceT pirvel argumentan avtoris klasi
    #rac nishnavs imas rom mand Authoridan unda aigos foreign key, xolo on_delete=CASCADE vutitebt rom TU
    #waishala avtori tavisi cxrilidan anu  avtoris Classis monacemta bazidan, es uzrunvelypfs imas, rom mititebuli avotirs
    #magalitad Oscar Wild-is yvela wigni waishalos monacemTa bazidan.
    #tu Cascade-s magivrad davayenebt SET.NULL -s mashin roca waishelba avtori misi wignebi ar waishleba mara avtoris fildi
    #iqneba NULL-ebi. da ase shemdeg, gaachnia ras Chavwert on_delete-shi.
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    genre = models.CharField(max_length=100, default="Genre")
    release_date = models.DateTimeField()
    personal_thoughts = models.TextField()
