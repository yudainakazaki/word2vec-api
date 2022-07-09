from django.db import models

class W2V(models.Model):
    word1 = models.CharField(null=True, blank=True, default=None, max_length=256)
    word2 = models.CharField(null=True, blank=True, default=None, max_length=256)
    result = models.FloatField(null=True, blank=True, default=None)

    def __str__(self):
        return "similarity between " + self.word1 + " and " + self.word2 + " are " + str(self.result)