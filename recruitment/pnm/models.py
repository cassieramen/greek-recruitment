from django.db import models

class PNM(models.Model):
  firstName = models.CharField(max_length=20)
  lastName = models.CharField(max_length=30)
  year = models.IntegerField() #1 for freshman, 2 for sophomore
  facebookScore = models.IntegerField()
  preselectScore = models.IntegerField()
  setOneScore = models.IntegerField()
  setTwoScore = models.IntegerField()
  setThreeScore = models.IntegerField()
  setFourScore = models.IntegerField()
  setReleased = models.IntegerField() #If current member, assign 5

  def __unicode__(self):
    return str(self.id)
