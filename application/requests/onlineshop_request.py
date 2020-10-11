from flask import request
from random import randint

class OnlineshopRequest:
    def __init__(self, details):
        self.id = randint(10000, 20000)
        self.administrative = details['administrative']
        self.administrative_duration = details['administrative_duration']
        self.informational = details['informational']
        self.informational_duration = details['informational_duration']
        self.productrelated = details['productrelated']
        self.productrelated_duration = details['productrelated_duration']
        self.bouncesrates = details['bouncerates']
        self.exitrates = details['exitrates']
        self.pagevalues = details['pagevalues']
        self.specialday = details['specialday']
        self.month = details['month']
        self.operatingsystems = details['operatingsystems']
        self.browser = details['browser']
        self.region = details['region']
        self.traffictype = details['traffictype']
        self.visitortype = details['visitortype']
        self.weekend = details['weekend']
        self.revenue = details['revenue']