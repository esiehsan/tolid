from django.db import models
from django.core.validators import MinValueValidator
from jalali_date import date2jalali



# Create your models here.
class Employee(models.Model):
    employeeId = models.PositiveSmallIntegerField(verbose_name='کد')
    fName = models.CharField(verbose_name='نام', max_length=100)
    lName = models.CharField(verbose_name='نام خانوادگی', max_length=100)

    def __str__(self):
        return str(self.employeeId) + ' ' + self.fName + ' ' + self.lName
    

class Part(models.Model):
    partNumber = models.IntegerField(verbose_name='کد قطعه', validators=[MinValueValidator(0)])
    castDate = models.DateField()
    caster1 = models.ForeignKey(to='Employee', 
                                on_delete=models.PROTECT,
                                related_name='parts_as_caster1',
                                null=True,
                                blank=True)
    
    caster2 = models.ForeignKey(to='Employee',
                                on_delete=models.PROTECT,
                                related_name='parts_as_caster2',
                                null=True, 
                                blank=True)
    
    caster3 = models.ForeignKey(to='Employee',
                                on_delete=models.PROTECT, 
                                related_name='parts_as_caster3', 
                                null=True, 
                                blank=True)
    
    mold_Id = models.PositiveSmallIntegerField(verbose_name='کد قالب', null=True, blank=True)
    
    def __str__(self):
        return f"PartNumber:{self.partNumber} | DateCast:{str(date2jalali(self.castDate))} | caster1:{self.caster1}"
        