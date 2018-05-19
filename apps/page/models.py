# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Language(models.Model):
	name = models.CharField(max_length=30)
	min_name = models.CharField(max_length=2)
	image = models.CharField(max_length=50)

class Info(models.Model):
	language = models.OneToOneField(Language, on_delete=models.CASCADE, primary_key=True)
	title = models.CharField(max_length=20)
	full_title = models.CharField(max_length=70)
	greeting = models.BinaryField()
	min_info = models.CharField(max_length=255)
	description = models.BinaryField()
    
	sign_up = models.CharField(max_length=30)
	login = models.CharField(max_length=30)
	community = models.CharField(max_length=30)
	compiler = models.CharField(max_length=30)
	profile = models.CharField(max_length=30)
	logout = models.CharField(max_length=30)
	my_codes = models.CharField(max_length=30)

	charts = models.CharField(max_length=30)
	chart1_title = models.CharField(max_length=30)
	chart2_title = models.CharField(max_length=30)
	chart3_title = models.CharField(max_length=30, default="No hay titulo")
	chart4_title = models.CharField(max_length=30, default="No hay titulo")


class Community(models.Model):
	language = models.OneToOneField(Language, on_delete=models.CASCADE, primary_key=True)
	greeting = models.CharField(max_length=30)
	info = models.BinaryField()
	btn_try = models.CharField(max_length=10)
	complete_registration = models.CharField(max_length=50)
	message_complete_registration = models.CharField(max_length=255)
	save_data = models.TextField(max_length=20)

class Compiler(models.Model):
	language = models.OneToOneField(Language, on_delete=models.CASCADE, primary_key=True)
	info = models.BinaryField()
	run = models.CharField(max_length=20)
	save_pc = models.CharField(max_length=30)
	save_db = models.CharField(max_length=30)
	log_compilation = models.CharField(max_length=40)
	result_execution = models.CharField(max_length=40)
	go = models.CharField(max_length=30)

class Profile(models.Model):
	language = models.OneToOneField(Language, on_delete=models.CASCADE, primary_key=True)
	n_codes = models.CharField(max_length=20)
	personal_data = models.CharField(max_length=30)
	edit = models.CharField(max_length=30)
	email = models.CharField(max_length=30)
	age = models.CharField(max_length=30)
	city = models.CharField(max_length=30)
	country = models.CharField(max_length=30)
	language_preference = models.CharField(max_length=40)
	options_account = models.CharField(max_length=30)
	password_change = models.CharField(max_length=30)
	change = models.CharField(max_length=30)
	delete_account = models.CharField(max_length=30)
	delete = models.CharField(max_length=30)
	update_data = models.CharField(max_length=30)
	cancel = models.CharField(max_length=30)
	save = models.CharField(max_length=30)
	confirmation_message = models.CharField(max_length=255)