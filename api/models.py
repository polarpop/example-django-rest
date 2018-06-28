# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import AbstractUser


USER_TYPE_CHOICES = (
	('realtor', 'realtor'),
	('borrower', 'borrower'),
	('loan_officer', 'loan_officer')
)

LOCATION_TYPE_CHOICES = (
	('branch', 'branch'),
	('previous_address', 'previous_address'),
	('current_address', 'current_address')
)


class Location(models.Model):
	street_address = models.CharField(max_length=100)
	city = models.CharField(max_length=40)
	state = models.CharField(max_length=2)
	postal_code = models.PositiveIntegerField(default=85282)
	manager = models.ForeignKey(
		'api.Profile', 
		on_delete=models.CASCADE,
		null=True,
		blank=True
	)
	location_type = models.CharField(
		choices=LOCATION_TYPE_CHOICES,
		max_length=16,
		default='branch'
	)


	def __str__(self):
		return "{street} {city}, {state} {zip}".format(
			street=self.street_address,
			city=self.city,
			state=self.state,
			zip=self.postal_code
		)

	def __unicode__(self):
		return self.pk




class Profile(AbstractUser):
	user_type = models.CharField(
		choices=USER_TYPE_CHOICES,
		default='loan_officer',
		max_length=12
	)
	created_on = models.DateTimeField(auto_now_add=True)
	updated_on = models.DateTimeField(auto_now_add=True)
	branch = models.ForeignKey(
		'api.Location', 
		on_delete=models.CASCADE,
		null=True,
		blank=True
	)
	employee_id = models.PositiveIntegerField(
		blank=True, 
		null=True
	)


	def __str__(self):
		'''
		Always show the full name of the user.
		'''
		return self.full_name

	def __unicode__(self):
		'''
		In the API we want to make sure we see
		the primary key, but on the front end
		interface, we want to see the User's
		full name.
		'''
		return self.pk


	@property
	def full_name(self):
		'''
		This method is used so we do not need to constantly define the first,
		and last name of the user and also to make them capatalized.

		Most of the names in the database should be set to lower before they
		are inserted into our database.

		See signal 'pre_save' in this file below.

		returns {String} - The first and last name capatalized of the user.
		'''
		return "{} {}".format(
			self.first_name.title(),
			self.last_name.title()
		)


	@property
	def is_loan_officer(self):
		'''
		This is a simple way of defining if the user is a Loan officer.

		Since Loan officer's will most likely be using the application
		the most, we want to add a simple helper property instead of
		writing the same logic over and over in code.

		returns {Boolean} - will return True or False depends on if the
		user is a Loan Officer
		'''
		return self.user_type == 'loan_officer'