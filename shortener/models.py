from django.db import models


# Create your models here.
class URL(models.Model):
    original_url = models.URLField(max_length=200)
    short_code = models.CharField(max_length=8, unique=True)
    click_count = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self: object) -> str:
        return self.original_url
