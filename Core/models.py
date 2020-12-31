from django.db import models

class Text(models.Model):
    inputfiled = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.pk