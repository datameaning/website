from django.db import models


# Create your models here.
class Editeur(models.Model) :
   nomEditeur=models.CharField(max_length=150)
   prenomEditeur=models.CharField(max_length=150)


class Livre(models.Model) :
   titre=models.CharField(max_length=150)
   anneePubli=models.IntegerField()
   editeur=models.ForeignKey(Editeur)


class Auteur(models.Model) :
   nomAuteur=models.CharField(max_length=150)
   prenomAuteur=models.CharField(max_length=150)
   livres=models.ManyToManyField(Livre)


class FrTriple(models.Model) :
    adj=models.CharField(max_length=60)
    noun=models.CharField(max_length=60)
    part=models.BooleanField(blank=True) # si renseigne le subj est cette partie
    pred=models.CharField(max_length=60)
    prep=models.CharField(max_length=60, blank=True)
    obj=models.CharField(max_length=60, blank=True) # self si reflexif
    subjQual=models.CharField(max_length=60,  blank=True)
    predQual=models.CharField(max_length=60,  blank=True)
    objQual=models.CharField(max_length=60,  blank=True)
    circum=models.CharField(max_length=60,  blank=True)
    

    class Admin: pass

    def __str__(self):
        return '%s %s %s' % (self.adj, self.noun, self.prd)

