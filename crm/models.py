from django.db import models


class Membership(models.Model):

    MEMBERSHIP_CHOICES = (
        ('s', 'Standard'),
        ('p', 'Premium'),
        ('ux', 'Ultimate Deluxe'),
    )

    name = models.CharField(max_length=500)
    membership_plan = models.CharField(max_length=2,
                                       choices=MEMBERSHIP_CHOICES)
    membership_active = models.BooleanField(default=True)
    unique_code = models.CharField(max_length=250)

    def __str__(self):
        return self.name + ' - record'

    class Meta:
        verbose_name_plural = "Membership"
        verbose_name = 'Member'
        ordering = ['unique_code']


class Client(models.Model):

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=100)
    job_title = models.CharField(max_length=150)
