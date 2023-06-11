from django.db import models

# in your Rule model
class Rule(models.Model):
    topic = models.CharField(max_length=200)
    rule = models.CharField(max_length=500)
    highlightColor = models.CharField(max_length=7)
    sound = models.URLField()

    def __str__(self):
        return f"{self.topic}" 

# in your Example model
class Example(models.Model):
    rule = models.ForeignKey(Rule, related_name='examples', on_delete=models.CASCADE)
    sentence = models.CharField(max_length=500)
    highlightedIndices = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.sentence[:50]}"  # Returns the first 50 characters of the sentence
