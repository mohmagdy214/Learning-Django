from django.db import models

class Login(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)



# ont to one

class Female(models.Model):
    name_female = models.CharField(max_length=50, null=True)
    def __str__(self):
        return self.name_female


class Male(models.Model):
    name_male = models.CharField(max_length=50, null=True)
    girls = models.OneToOneField(Female, on_delete=models.CASCADE)
    def __str__(self):
        return self.name_male
    

# one to many 

class Product(models.Model):
    title = models.CharField(max_length=50, null=True)
    def __str__(self):
        return self.title


class User(models.Model):
    products = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, null=True)
    def __str__(self):
        return self.name


# many to many 

class Video(models.Model):
    title = models.CharField(max_length=50, null=True)
    def __str__(self):
        return self.title


class UserName(models.Model):
    watch = models.ManyToManyField(Video, null=True)
    name = models.CharField(max_length=50, null=True)
    def __str__(self):
        return self.name