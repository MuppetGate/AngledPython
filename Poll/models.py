import datetime
from django.db import models
from django.utils import timezone

# Create your models here.


class Poll(models.Model):
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def convert_to_dict(self):
        #need to get all the choices I guess.
        choices = list(self.choice_set.all())

        return {"question": self.question,
                "publishing_date": self.pub_date.strftime("%Y-%m-%d"),
                "choices": [choice.convert_to_dict() for choice in choices]}

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

class Choice(models.Model):
    poll = models.ForeignKey(Poll)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

    def convert_to_dict(self):
        return {"choiceText": self.choice_text, "votes": self.votes }
