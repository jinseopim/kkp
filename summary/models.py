
from django.db import models
from django.utils import timezone


class Summary(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    section_name = models.CharField(max_length=1000, null=True)
    category_name = models.CharField(max_length=1000, null=True)
    summary_name = models.TextField(null=True)
    url = models.CharField(max_length=4000, null=True)
    date = models.DateTimeField()
    thumbnail = models.ImageField(u'썸네일',
                        upload_to='%Y/%m/%d', blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        Summary.objects.filter(date__lte=timezone.now())\
                    .order_by('created_date')
        return self.summary_name

