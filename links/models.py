from django.db import models

class Links(models.Model):
    name = models.CharField(max_length=200, unique=True)
    url = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    clicks = models.PositiveIntegerField(default=0)
    def __str__(self):
       return f'{self.name}  {self.url}  {self.slug}'
    def click(self):
        self.clicks += 1
        self.save()
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.name.replace(' ', '-').lower()
            