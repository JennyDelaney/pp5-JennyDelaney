from django.db import models


class Mailing(models.Model):
    """
    Users can sign up for the Newsletter
    """
    first_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
