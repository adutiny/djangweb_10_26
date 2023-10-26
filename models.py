from django.db import models





class ContactForm(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name    
    


class Signup(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=100) 
    confirm_password = models.CharField(max_length=100)

class Feedback(models.Model):
    name = models.CharField(max_length=60)
    email = models.EmailField()
    trust = models.TextField(max_length=600)
    concerns = models.TextField(max_length=600)
    accurate = models.IntegerField()
    purchase = models.IntegerField()

class Login(models.Model):
    user_name = models.CharField(max_length=60)
    Password = models.CharField(max_length=100)  


class Prompt(models.Model):
    co_name = models.CharField(max_length=60)
    co_email = models.EmailField()
    co_phone = models.CharField(max_length=12)
    co_website = models.CharField(max_length=100)
    co_address = models.CharField(max_length=100)
    ques_1 = models.TextField(max_length=100)
    ans_1 = models.TextField(max_length=100)
    ques_2 = models.TextField(max_length=100)
    ans_2 = models.TextField(max_length=100)
    ques_3 = models.TextField(max_length=100)
    ans_3 = models.TextField(max_length=100)
    ques_4 = models.TextField(max_length=100)
    ans_4= models.TextField(max_length=100)
    ques_5 = models.TextField(max_length=100)
    ans_5 = models.TextField(max_length=100)
    ques_6 = models.TextField(max_length=100)
    ans_6 = models.TextField(max_length=100)
     



