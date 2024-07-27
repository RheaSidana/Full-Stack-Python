from django.db import models

# Create your models here.
all_destinations_list = ['India', 'Dubai', 'Singapore']

#all_destinations_list[0]

# Destination:
#   id
#   name 
#   address:
    #   id
    #   city
    #   state
    #   country:
        #   name
        #   country_code
        #   currency

# Country table
class Country(models.Model):
    name = models.CharField(max_length=100)
    country_code = models.IntegerField(primary_key=True)
    currency = models.CharField(max_length=100)

    def __str__(self):
        return f"Country Name: {self.name}, Country_code: {self.country_code}, Currency: {self.currency} "

class Address(models.Model):
    id = models.IntegerField(primary_key=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return f"ID: {self.id}, City: {self.city}, State: {self.state}, Country: {self.country} "

class Destination(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, Address: {self.address} "
    

class DestiantionWeather(models.Model):
    destination_name = models.CharField(max_length=200)
    weather = models.IntegerField()
    admin_secret = models.CharField(max_length=150)

    def __str__(self) -> str:
        return f'Destination Name: {self.destination_name}, weather: {self.weather}, admin_secret: {self.admin_secret} '

