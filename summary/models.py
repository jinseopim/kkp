
from django.db import models
from django.utils import timezone


class Summary(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    date = models.DateTimeField()
    thumbnail = models.ImageField(u'썸네일',
                        upload_to='%Y/%m/%d', blank=True, null=True)
    join_users = models.ManyToManyField('auth.User',
                        verbose_name=u'참석', blank=True,
                        related_name='join_moim')
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        Summary.objects.filter(date__lte=timezone.now())\
                    .order_by('created_date')
        return self.title

