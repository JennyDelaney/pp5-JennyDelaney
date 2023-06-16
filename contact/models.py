from django.db import models


class Contact(models.Model):
    """
    Users can send message
    """
    topic = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=20)
    message = models.TextField(max_length=1000)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        """
        Set ordering and plural name
        """
        ordering = ['-date_created']
        verbose_name_plural = 'Contact Us'

    def __str__(self):
        return f'Message from {self.name}'

