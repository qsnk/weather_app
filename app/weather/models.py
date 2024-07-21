from django.contrib.auth.models import User
from django.db import models


class City(models.Model):
    name = models.CharField(max_length=100, unique=True)
    queries_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

    def increment_queries_count(self):
        self.queries_count += 1


class UserSearchHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_time = models.DateTimeField(auto_now_add=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return f'Search history for {self.user}'