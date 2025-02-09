from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100, verbose_name="Student Name")
    email = models.EmailField(max_length=277, verbose_name="Student Email")

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    # banner_img = models.ImageField(upload_to='banners/',null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# class Comment(models.Model):
#     post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name='comments')
#     name = models.CharField(max_length=100)
#     email = models.EmailField()
#     content = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)
