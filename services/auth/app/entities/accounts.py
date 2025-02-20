from django.db import models
from common.app.entities.baseEntity import Base

class Accounts(Base):
    username = models.CharField(unique = True, max_length = 100, null = False, blank = False)
    password = models.CharField(max_length = 255, null = False, blank = False)
    email = models.EmailField(unique=True, null=False, blank=False)
    phone = models.CharField(max_length = 11, null = False, blank = False, unique = True)

    def __str__(self):
        return self.id
    class Meta:
        abstract = False
