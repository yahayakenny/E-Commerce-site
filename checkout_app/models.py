from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Billing Address Model
class Billing(models.Model):
	# user = models.ForeignKey(User, on_delete=models.CASCADE)
	address = models.CharField(max_length=100)
	email = models.EmailField(default='test@email.com')
	phone = models.IntegerField(default=234099940409)

	def __str__(self):
		return f'{self.user.username} billing address'

	class Meta:
		verbose_name_plural = "Billing Addresses"