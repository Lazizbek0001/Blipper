from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Meep(models.Model):
    user = models.ForeignKey(
        User, related_name='meeps',
        on_delete=models.DO_NOTHING
    )
    body = models.CharField(max_length=600)
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name="meep_like", blank=True)
    bookmarks = models.ManyToManyField(User, related_name="bookmarks", blank=True)
    
    def number_of_likes(self):
        return self.likes.count()
    
    def __str__(self):
        return f"{self.user} \n({self.created_at:%Y-%m-%d %H:%M})\n{self.body}"

class Comment(models.Model):
    comment = models.CharField(max_length=200)
    meep = models.ForeignKey(Meep,related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name="comment_likes", blank=True)
    
    def number_of_likes(self):
        return self.likes.count()
    
class Notifications(models.Model):
    body = models.CharField(max_length=50)
    user = models.ForeignKey(User, related_name="notifications", on_delete=models.CASCADE)
    requested_user = models.ForeignKey(User, related_name="requested_notifications", on_delete=models.CASCADE, blank=True, null=True)
    post_meep = models.CharField(max_length=40, blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.user.username
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    follows = models.ManyToManyField(
        "self",
        related_name="followed_by",
        symmetrical=False,
        blank=True
    )
    date_modified = models.DateTimeField(auto_now=True)
    profile_image = models.ImageField(upload_to="images/", blank=True, null=True)
    back_image = models.ImageField(upload_to="images/", blank=True, null=True)
    profile_bio = models.CharField(max_length=500, blank=True, null=True)
    homepage_link = models.CharField(max_length=100, blank=True, null=True)
    facebook_link = models.CharField(max_length=100, blank=True, null=True)
    instagram_link = models.CharField(max_length=100, blank=True, null=True)
    linkedln_link = models.CharField(max_length=100, blank=True, null=True)
    born_date = models.DateTimeField("born_date", blank=True, null=True)
    
    def __str__(self):
        return self.user.username
    
    
# @receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()
        user_profile.follows.set([instance.profile.id])  # Assuming you want the user to follow themselves
        user_profile.save()
        
post_save.connect(create_profile, sender=User)


# @receiver(post_save, sender=User)
# def create_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)

# post_save.connect(create_profile, sender=User)


