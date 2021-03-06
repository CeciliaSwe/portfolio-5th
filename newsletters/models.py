from django.db import models

# Create your models here.


class NewsletterUser (models.Model):
    """
    Model for newsletter signup
    """
    email = models.EmailField(max_length=254, null=False, blank=False)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
