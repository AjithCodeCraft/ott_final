from django.db import models

class Register(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=100)  # You should use a more secure way to store passwords
    DoB = models.DateField()
    phonenumber = models.CharField(max_length=15)
    joining_date = models.DateField(null=True, blank=True)
    expiry_date = models.DateField(null=True, blank=True)

    def activate_subscription(self, duration_months=1):
        from datetime import datetime, timedelta
        today = datetime.now().date()
        self.joining_date = today
        self.expiry_date = today + timedelta(days=30 * duration_months)
        self.save()

    def is_subscription_active(self):
        from datetime import datetime
        today = datetime.now().date()
        return self.expiry_date is not None and self.expiry_date >= today

    def __str__(self):
        return self.username
