import uuid
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, UserManager, AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models, IntegrityError
from django.utils import timezone


class CustomUser(AbstractUser):
    date_of_birth = models.DateField(verbose_name="Date of birth", blank=True, null=True)
    aadhar = models.CharField(verbose_name="aadhar", max_length=1024, blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class AxisCompleteDetail(models.Model):
    state = models.CharField(default="", max_length=200, blank=True, null=True)
    final_city = models.CharField(default="", max_length=200, blank=True, null=True)
    account_ref = models.CharField(default="", max_length=200, blank=True, null=True)
    full_name = models.CharField(default="", max_length=200, blank=True, null=True)
    registration = models.CharField(default="", max_length=200, blank=True, null=True)
    manufacturer = models.CharField(default="", max_length=200, blank=True, null=True)
    chasis_number = models.CharField(default="", max_length=2000, blank=True, null=True)
    pos = models.FloatField(default=0, blank=True, null=True)
    bucket = models.CharField(default="", max_length=200, blank=True, null=True)
    address = models.CharField(default="", max_length=2000, blank=True, null=True)
    mobile_numer = models.CharField(default="", max_length=12, blank=True, null=True)
    emi_amount = models.FloatField(default=0, blank=True, null=True)
    final_emi_amount = models.FloatField(default=0, blank=True, null=True)
    emi_charges = models.FloatField(default=0, blank=True, null=True)
    total_overdue = models.FloatField(default=0, blank=True, null=True)
    total_od_charges = models.FloatField(default=0, blank=True, null=True)
    engine_number = models.CharField(default="", max_length=500, blank=True, null=True)
    cm_name = models.CharField(default="", max_length=200, blank=True, null=True)
    acm_name = models.CharField(default="", max_length=200, blank=True, null=True)

    def __str__(self):
        return self.manufacturer + ", reg: " + self.registration + ", name: " + self.full_name


class CompleteDetail(models.Model):
    hpa_no = models.CharField(default="", max_length=200, blank=True, null=True)
    name = models.CharField(default="", max_length=200, blank=True, null=True)
    brndes = models.CharField(default="", max_length=200, blank=True, null=True)
    rgndes = models.CharField(default="", max_length=200, blank=True, null=True)
    state = models.CharField(default="", max_length=200, blank=True, null=True)
    emp_name = models.CharField(default="", max_length=200, blank=True, null=True)
    outstand = models.CharField(default="", max_length=200, blank=True, null=True)
    age = models.CharField(default="", max_length=200, blank=True, null=True)
    bill1 = models.CharField(default="", max_length=200, blank=True, null=True)
    soh = models.CharField(default="", max_length=200, blank=True, null=True)
    assdes = models.CharField(default="", max_length=200, blank=True, null=True)
    status = models.CharField(default="", max_length=20, blank=True, null=True)
    branch = models.CharField(default="", max_length=200, blank=True, null=True)
    regno = models.CharField(default="", max_length=200, blank=True, null=True)
    engno = models.CharField(default="", max_length=200, blank=True, null=True)
    chsno = models.CharField(default="", max_length=200, blank=True, null=True)
    place = models.CharField(default="", max_length=200, blank=True, null=True)
    postoffice = models.CharField(default="", max_length=200, blank=True, null=True)
    road_name = models.CharField(default="", max_length=200, blank=True, null=True)
    landmark = models.CharField(default="", max_length=200, blank=True, null=True)
    city_village = models.CharField(default="", max_length=200, blank=True, null=True)
    state_code = models.CharField(default="", max_length=200, blank=True, null=True)
    district_code = models.CharField(default="", max_length=200, blank=True, null=True)
    taluk = models.CharField(default="", max_length=200, blank=True, null=True)
    website = models.CharField(default="", max_length=200, blank=True, null=True)
    pincode = models.CharField(default="", max_length=200, blank=True, null=True)
    office_phone_no = models.CharField(default="", max_length=200, blank=True, null=True)
    resi_telephone = models.CharField(default="", max_length=200, blank=True, null=True)
    mobile_no = models.CharField(default="", max_length=200, blank=True, null=True)
    pager_no = models.CharField(default="", max_length=200, blank=True, null=True)
    gu_name = models.CharField(default="", max_length=200, blank=True, null=True)
    gu_place = models.CharField(default="", max_length=200, blank=True, null=True)
    gu_postoffice = models.CharField(default="", max_length=200, blank=True, null=True)
    gu_road_name = models.CharField(default="", max_length=200, blank=True, null=True)
    gu_landmark = models.CharField(default="", max_length=200, blank=True, null=True)
    gu_city_village = models.CharField(default="", max_length=200, blank=True, null=True)
    gu_state_des = models.CharField(default="", max_length=200, blank=True, null=True)
    gu_district_des = models.CharField(default="", max_length=200, blank=True, null=True)
    gu_taluk = models.CharField(default="", max_length=200, blank=True, null=True)
    gu_pincode = models.CharField(default="", max_length=200, blank=True, null=True)
    gu_office_phone_no = models.CharField(default="", max_length=200, blank=True, null=True)
    gu_resi_telephone = models.CharField(default="", max_length=200, blank=True, null=True)
    gu_mobile_no = models.CharField(default="", max_length=200, blank=True, null=True)
    cust_fatherName = models.CharField(default="", max_length=200, blank=True, null=True)
    priority_tag = models.CharField(default="", max_length=200, blank=True, null=True)
    october_handling_vertical_name = models.CharField(default="", max_length=200, blank=True, null=True)
    acct_no = models.CharField(default="", max_length=200, blank=True, null=True)
    pdt1 = models.CharField(default="", max_length=200, blank=True, null=True)
    emi_amount = models.CharField(default="", max_length=200, blank=True, null=True)
    pos = models.CharField(default="", max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name
