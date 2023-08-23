from django.db import models

# Create your models here.

class Market(models.Model):
    market_name = models.CharField(max_length=25,default='')
    market_type = models.CharField(max_length=25, default='')
    def __str__(self) -> str:
        return self.market_name, self.market_type
    
    class Meta:
        db_table = 'polls_Market'