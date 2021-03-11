from django.db import models

# Create your models here.
class stock_db(models.Model):
    #the column to save
    ticker = models.CharField(max_length=10)

    def __str__(self):
        return self.ticker


#create a migration
# /usr/bin/python3 /home/siriux/Documents/Project/'Stock Market'/Websites/Tradee/myequityindia/manage.py makemigrations

#push into database migration
#/usr/bin/python3 /home/siriux/Documents/Project/'Stock Market'/Websites/Tradee/myequityindia/manage.py migrate

#go register the models in admin.py