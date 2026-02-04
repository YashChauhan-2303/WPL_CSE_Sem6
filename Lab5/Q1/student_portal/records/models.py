from django.db import models


class StudentRecord(models.Model):
	name = models.CharField(max_length=200)
	dob = models.DateField()
	address = models.TextField(blank=True)
	contact = models.CharField(max_length=20, blank=True)
	email = models.EmailField(blank=True)
	maths = models.IntegerField(default=0)
	physics = models.IntegerField(default=0)
	chemistry = models.IntegerField(default=0)
	created_at = models.DateTimeField(auto_now_add=True)

	def total(self):
		return (self.maths or 0) + (self.physics or 0) + (self.chemistry or 0)

	def percentage(self):
		return round(self.total() / 300.0 * 100.0, 2)

	def __str__(self):
		return f"{self.name} ({self.email})"
