from django.db import models

# Create your models here.
class Submit(models.Model):
    name = models.CharField(max_length=40)
    phoneNumber = models.CharField(max_length=15)
    ammount = models.PositiveIntegerField()
    date = models.DateField()
    time = models.TimeField()
    def __str__(self):
        return f"Họ tên: {self.name} - Sđt: {self.phoneNumber} - Số người: {self.ammount} - Ngày đặt bàn: {self.date} - Thời gian: {self.time}"
    