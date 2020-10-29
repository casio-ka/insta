from django.db import models
from django.contrib.auth.models import User
from .utils import get_random_code
from cloudinary.models import CloudinaryField
from django.template.defaultfilters import slugify

# Create your models here.
#Creating a model for Profile..
class Profile(models.Model):
    first_name =models.TextField(max_length=20, blank=True)
    last_name =models.TextField(max_length=20, blank=True)
    bio = models.TextField(default="no bio..." ,max_length=250)
    photo = CloudinaryField('image' ,blank = True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    email = models.TextField(max_length=200, blank=True)
    following = models.ManyToManyField(User, related_name='following', blank=True)
    slug = models.SlugField(unique=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def profile_posts(self):
        return self.post_set.all()

    def save (self, *args, **kwargs):
        ex = False
        if self.first_name and self.last_name:
            to_slug = slugify(str(self.first_name)+ " "+ str(self.last_name))
            ex = Profile.objects.filter(slug=to_slug).exists()
            while ex:
                to_slug = slugify(to_slug +" "+str(get_random_code()))
                ex = Profile.objects.filter(slug=to_slug).exists()
        else:
            to_slug = str(self.user)
        self.slug = to_slug
        super().save(*args, **kwargs)

    @classmethod
    def search_profile(cls, name):
        profile = Profile.objects.filter(user__username__icontains = name)
        return profile

    @classmethod
    def get_by_id(cls, id):
        profile = Profile.objects.get(user = id)
        return profile

    @classmethod
    def filter_by_id(cls, id):
        profile = Profile.objects.filter(user = id).first()
        return profile

    
    def __str__(self):
        return self.bio

    def __str__(self):
        return str(self.user.username)

    class Meta:
        ordering = ('-created',)


class Image(models.Model):
    name = models.CharField(max_length = 50)
    image = CloudinaryField('image', blank = True)
    caption = models.TextField(max_length=400)
    profile = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()


    @classmethod
    def update_caption(cls, caption):
        update_img = cls.objects.filter(id = id).update(caption = caption)
        return update_img

    @classmethod
    def get_all_images(cls):
        images = cls.objects.all()
        return images

    @classmethod
    def get_image_by_id(cls, id):
        image = cls.objects.filter(id = id).all()
        return image

    @classmethod
    def get_profile_pic(cls, profile):
        images = Image.objects.filter(profile__pk = profile)
        return images

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created',]


class Likes(models.Model):
    image = models.ForeignKey(Image, on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')

    def save_like(self):
        self.save()

    def unlike_like(self):
        self.delete()


    
class Comments(models.Model):
    comment = models.CharField(max_length = 300)
    posted_on = models.DateTimeField(auto_now=True)
    image = models.ForeignKey(Image, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def save_comment(self):
        self.save()

    def delete_comment(self):
        self.delete()

    @classmethod
    def get_comments_by_images(cls, id):
        comments = Comments.objects.filter(image__pk = id)
        return comments