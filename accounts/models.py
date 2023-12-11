from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import AbstractUser

class Khoa(models.Model):
    ma_khoa = models.IntegerField(primary_key=True)
    ten_khoa = models.CharField(max_length=50, null=True)
    ma_truong_bo_mon = models.IntegerField(null=True)

    class Meta:
        db_table = 'Khoa'

class SinhVien(models.Model):
    mssv = models.IntegerField(primary_key=True)
    ho_ten = models.CharField(max_length=50, null=True)
    ngay_sinh = models.DateField(null=True)
    gioi_tinh = models.CharField(max_length=30, null=True)
    sdt = models.BigIntegerField(null=True)
    email = models.CharField(max_length=100, null=True)
    trang_thai = models.CharField(max_length=30, null=True)
    ma_khoa = models.ForeignKey(Khoa, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = 'Sinh_vien'

class GiangVien(models.Model):
    mscb = models.IntegerField(primary_key=True)
    ho_ten = models.CharField(max_length=50, null=True)
    ngay_sinh = models.DateField(null=True)
    gioi_tinh = models.CharField(max_length=30, null=True)
    sdt = models.BigIntegerField(null=True)
    email = models.CharField(max_length=100, null=True)
    ma_khoa = models.ForeignKey(Khoa, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = 'Giang_vien'
