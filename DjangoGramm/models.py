from django.db import models


class User(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=128)
    password = models.CharField(max_length=50)


class Profile(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=128)
    e_mail = models.EmailField(max_length=128)
    birthday = models.DateField()
    gender = models.CharField(max_length=10)
    bio = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='images/%Y/%m/%d/')


class Post(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_create = models.DateField()
    info = models.TextField(blank=True)


class Image(models.Model):
    id = models.IntegerField(primary_key=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='images/%Y/%m/%d/')


class Tag(models.Model):
    id = models.IntegerField(primary_key=True)
    tag_name = models.CharField(max_length=128)


class PostTag(models.Model):
    id = models.IntegerField(primary_key=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

# class Friendship(models.Model):
#     user1_id = models.ForeignKey(User, on_delete=models.CASCADE)
#     user2_id = models.ForeignKey(User, on_delete=models.CASCADE)
#     date_make_friend = models.DateField()
