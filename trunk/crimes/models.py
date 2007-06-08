from django.db import models

import datetime

# mobility classification
MOBILITY = (
    ('WK', 'Walking'),
    ('VE', 'Vehicle'),
)

QUANTITY = (
    ('AL','Alone'),
    ('FO','Folloied'),
)

THIEF = (
    ('ON','One'),
    ('MA','Many'),

)

WEAPON = (    
    ('MW','Melee'),
    ('GN','Guns'),
    ('NN','None'),
)

PERIOD = (
    ('MO','Morning'),
    ('EV','Evening'),
    ('NI','Night'),
)


class Incident (models.Model):
    """An localized crime incident"""

    # general information
    desc = models.TextField()
    lon = models.CharField(maxlength=30)
    lat = models.CharField(maxlength=30)
    when = models.DateTimeField()

    # classification 
    mobility = models.CharField(maxlength=2, choices=MOBILITY)
    quantity = models.CharField(maxlength=2, choices=QUANTITY)
    thief = models.CharField(maxlength=2, choices=THIEF)
    weapon = models.CharField(maxlength=2, choices=WEAPON)
    period = models.CharField(maxlength=2, choices=PERIOD)

    def summary(self):
	"""An short description of the description"""
	cut = 100
	if len(self.desc) > cut:
		return self.desc[:cut]+" ..."
	else:
		return self.desc[:cut]

    def __str__(self):
        """An string representation of the incident object"""
        cut = 10
        if len(self.desc) > cut:
            return str(self.id)+" "+self.desc[:cut]+" ..."
        else:
            return str(self.id)+" "+self.desc[:cut]

    def was_today(self):
        """True if when is current day"""
        return self.when == datetime.date.today()

	# To be visible in the admin interface
    class Admin:
        pass
