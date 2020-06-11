from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


from django.utils.translation import gettext_lazy as _
from datetime import date
from django.dispatch import receiver

# Create your models here.
class userInfo(models.Model):
	faculty_types = [
	('FASS','Arts and Social Sciences'),
	('BIZ','Business'),
	('COM','Computing'),
	('DEN','Dentistry'),
	('SDE','Design and Environment'),
	('ENG','Engineering'),
	('LAW','Law'),
	('MED','Medicine'),
	('SCI','Science'),
	]

	Campus_Residential = [
    ('TH', 'Temasek Hall'),
    ('EH', 'Eusoff Hall'),
   	('SH', 'Sheares Hall'),
   	('RH', 'Raffles Hall'),
   	('KR', 'Kent Ridge Hall'),
   	('TEM', 'Tembusu'),    	
   	('RVRC', 'Ridge View Residences'),
	('CAPT', 'College of Alice and Peter Tan'),
    ('USP', 'University Scholars Programme'),
    ('RC4', 'Residential College 4'),
    ('NIL', 'Do Not Stay On Campus'),
    ]
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	name = models.CharField('Full Name',max_length=200)
	number = models.IntegerField('Phone Number', unique=True)
	matric = models.CharField('Matric Number',max_length=10,help_text='AXXXXXXXB', unique=True)
	email = models.EmailField('NUS Email', max_length=200, blank=False, unique=True)
	faculty = models.CharField(max_length=50,choices=faculty_types,default='FASS')
	campus_residential_type = models.CharField('Campus Residential Type',
    max_length=100, choices=Campus_Residential,
    default='NIL')
	password = models.CharField(max_length=50)
	image = models.ImageField(upload_to='profile_image', blank=True)

	def __str__(self):
		return self.email

class Image(models.Model):
    name= models.CharField(max_length=500)
    imagefile= models.FileField(upload_to='images/', null=True, verbose_name="")

    def __str__(self):
        return self.name + ": " + str(self.imagefile)

class Post(models.Model):
	title = models.CharField(max_length = 50)
	price = models.CharField(max_length = 10)

	def __str__(selfself):
		return self.title


class Product(models.Model):
	name = models.CharField(max_length=200,null=True)
	price = models.FloatField()
	organisation = models.CharField(max_length=200,null=True)
	form = models.URLField(max_length=200)
	image = models.ImageField(upload_to='image', blank=True)

	def __str__(self):
		return self.name
