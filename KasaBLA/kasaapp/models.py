from django.db import models


class unitoperation(models.Model):
    unitoperation_name = models.CharField(max_length=300)

    def __str__(self):
        return self.unitoperation_name

    class Meta:
        db_table = 'kasaapp_unitoperation'


class processparameter(models.Model):
    unitoperation = models.ForeignKey(unitoperation, on_delete=models.CASCADE)
    processparameter_name = models.CharField(max_length=300)
    risk_ranking = models.CharField(max_length=200)

    def __str__(self):
        return self.processparameter_name

    class Meta:
        db_table = 'kasaapp_processparameter'
