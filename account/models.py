from django.conf import settings
from django.db import models
from stdimage import StdImageField


class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    birth_date = models.DateField(blank=True, null=True)
    # avatar = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)
    avatar = StdImageField(upload_to='users/%Y/%m/%d/', blank=True, variations={
        'large': (500, 500),
        'thumbnail': (100, 100, True),
        'medium': (300, 200),
    }, delete_orphans=True)

    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)

    def get_avatar_url(self):
        return self.avatar.large.url
