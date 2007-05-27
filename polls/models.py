from django.db import models

class Poll(models.Model):
    question = models.CharField(maxlength=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question
    class Admin:
        pass

class Choice(models.Model):
    poll = models.ForeignKey(Poll)
    choice = models.CharField(maxlength=200)
    votes = models.IntegerField()
    def __str__(self):
        return self.choice
    class Admin:
        pass
