from django.db import models


class VoteCounter(models.Model):
    good = models.PositiveIntegerField(default=0)
    satisfactory = models.PositiveIntegerField(default=0)
    bad = models.PositiveIntegerField(default=0)

    def total_votes(self) -> int:
        return self.good + self.satisfactory + self.bad
