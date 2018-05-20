# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Idiom(models.Model):
	name = models.CharField(max_length=30)
	min_name = models.CharField(max_length=2)
	image = models.CharField(max_length=50)

	def __str__(self):
		return self.name


class Info(models.Model):
	idiom = models.OneToOneField(Idiom, on_delete=models.CASCADE, primary_key=True)
	name = models.CharField(max_length=70)
	home = models.CharField(max_length=20)
	greeting = models.CharField(max_length=50)
	min_info = models.CharField(max_length=255)
	description = models.TextField()
    
	sign_up = models.CharField(max_length=30)
	login = models.CharField(max_length=30)
	community = models.CharField(max_length=30)
	compiler = models.CharField(max_length=30)
	profile = models.CharField(max_length=30)
	logout = models.CharField(max_length=30)
	my_codes = models.CharField(max_length=30)

	charts = models.CharField(max_length=50)
	chart1_title = models.CharField(max_length=80)
	chart2_title = models.CharField(max_length=80)
	chart3_title = models.CharField(max_length=80, default="No hay titulo")
	chart4_title = models.CharField(max_length=80, default="No hay titulo")

	def __str__(self):
		return 'Info in {}'.format(self.idiom.name)


class Community(models.Model):
	idiom = models.OneToOneField(Idiom, on_delete=models.CASCADE, primary_key=True)
	greeting = models.CharField(max_length=50)
	info = models.TextField()
	btn_try = models.CharField(max_length=10)
	complete_registration = models.CharField(max_length=50)
	message_complete_registration = models.CharField(max_length=255)
	save_data = models.CharField(max_length=20)

	def __str__(self):
		return 'Community in {}'.format(self.idiom.name)

class Compiler(models.Model):
	idiom = models.OneToOneField(Idiom, on_delete=models.CASCADE, primary_key=True)
	info = models.TextField()
	run = models.CharField(max_length=20)
	save_pc = models.CharField(max_length=30)
	save_db = models.CharField(max_length=30)
	compilation_log = models.CharField(max_length=40)
	execution_result = models.CharField(max_length=40)
	go = models.CharField(max_length=30)

	def __str__(self):
		return 'Compiler in {}'.format(self.idiom.name)

class Profile(models.Model):
	idiom = models.OneToOneField(Idiom, on_delete=models.CASCADE, primary_key=True)
	n_codes = models.CharField(max_length=20)
	personal_data = models.CharField(max_length=30)
	edit = models.CharField(max_length=30)
	email = models.CharField(max_length=30)
	age = models.CharField(max_length=30)
	city = models.CharField(max_length=30)
	country = models.CharField(max_length=30)
	language_preference = models.CharField(max_length=40)
	account_options = models.CharField(max_length=30)
	change_password = models.CharField(max_length=30)
	change = models.CharField(max_length=30)
	delete_account = models.CharField(max_length=30)
	delete = models.CharField(max_length=30)
	update_data = models.CharField(max_length=30)
	cancel = models.CharField(max_length=30)
	btn_save = models.CharField(max_length=30)
	confirmation_message = models.CharField(max_length=255)

	def __str__(self):
		return 'Profile in {}'.format(self.idiom.name)