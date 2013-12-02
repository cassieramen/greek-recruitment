from django.db import models

class PNM(models.Model):
  firstName = models.CharField(max_length=20)
  lastName = models.CharField(max_length=30)
  year = models.IntegerField() #1 for freshman, 2 for sophomore
  country = models.CharField(max_length=20)
  address = models.CharField(max_length=200)
  city = models.CharField(max_length=200)
  state = models.CharField(max_length=5)
  zip = models.IntegerField()
  highSchool = models.CharField(max_length=200)
  major = models.CharField(max_length=200)
  dorm = models.CharField(max_length=200)
  facebookScore = models.IntegerField()
  preselectScore = models.IntegerField()
  setOneScore = models.IntegerField()
  setTwoScore = models.IntegerField()
  setThreeScore = models.IntegerField()
  setFourScore = models.IntegerField()
  setReleased = models.IntegerField() #If current member, assign 5
  income = models.IntegerField()


  def __unicode__(self):
    return str(self.id)
