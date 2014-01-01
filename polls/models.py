"""
In this Poll app, there are two models: Poll and Choice. A Poll has a
question and a publication date. A Choice has two fields: the text of the
choice and a vote tally.  Each Choice is associated with a Poll
"""

import datetime
from django.utils import timezone
from django.db import models

# Create your models here.
class Poll(models.Model):
	question = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')
	def __unicode__(self):
		return self.question
	def was_published_recently(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
	poll = models.ForeignKey(Poll)
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)
	
	def __unicode__(self):
		return self.choice_text

	def was_published_recently(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
	
	was_published_recently.admin_order_field = 'pub_date'
	was_published_recently.boolean = True
	was_published_recently = short_description = 'Recently published?'


"""
Activating this files (models.py)
That small bit of model code gives Django a lot of information. With it, Django is able to:
	- Create a database schema (CREATE TABLE statements) for this app.
 	- Create a Python database-access API for accessing Poll and Choice objects.

To see the SQL statement Django will use to create the data schema, type:
$ python manage.py sql polls
"""