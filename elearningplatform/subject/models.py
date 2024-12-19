from django.db import models


# Create your models here.
class Subject(models.Model):
    name = models.CharField(max_length=200, verbose_name="Subject")
    image = models.ImageField(null=True, blank=True, upload_to="subject", verbose_name="Image")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Creation Date")
    updated = models.DateTimeField(auto_now=True, verbose_name="Update Date")

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class File(models.Model):
    name = models.CharField(max_length=25, verbose_name="Name")
    description = models.TextField(max_length=200, null=True, blank=True, verbose_name="Description")
    file = models.FileField(upload_to="file", verbose_name="File")
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, verbose_name="Subject")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Creation Date")
    updated = models.DateTimeField(auto_now=True, verbose_name="Update Date")

    class Meta:
        ordering = ["-created"]
