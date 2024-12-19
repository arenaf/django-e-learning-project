from django.db import models
from django.contrib.auth.models import User
from subject.models import Subject


# Save only the last avatar
def custom_avatar(instance, filename):
    old_avatar = Profile.objects.get(pk=instance.pk)
    old_avatar.avatar.delete()
    return 'profiles/' + filename


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to=custom_avatar, null=True, blank=True, verbose_name="Avatar")
    subjects = models.ManyToManyField(Subject, blank=True, related_name="subject")
    students = models.ManyToManyField("self", symmetrical=False, blank=True)
    is_teacher = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username

    class Meta:
        ordering = ['user__username']
