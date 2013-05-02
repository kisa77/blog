from django.db import models

# Create your models here.
class coupon(models.Model):
    cTitle = models.CharField(max_length=20)
    cShopName = models.CharField(max_length=100)
    cid = models.IntegerField(max_length=11)
    sid = models.CharField(max_length=32)

    def __unicode__(self):
         return self.title

    def add_coupon(self) :
        pass
#def add_coupon () :
