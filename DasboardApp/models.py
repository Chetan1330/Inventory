from django.db import models
from datetime import datetime

class Stock(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=700, unique=False)
    quantity = models.IntegerField(default=1)
    is_deleted = models.BooleanField(default=False)

    SSN = models.CharField(max_length=700, default=False , null=True, blank=True)
    Name = models.CharField(max_length=700, default=False , null=True, blank=True)
    DNUSAN = models.CharField(max_length=700, default=False, null=True, blank=True)
    Shortdesc = models.CharField(max_length=700, default=False, null=True, blank=True)
    Class = models.CharField(max_length=700, default=False, null=True, blank=True)
    Category = models.CharField(max_length=700, default=False, null=True, blank=True)
    Subcategory = models.CharField(max_length=700, default=False, null=True, blank=True)
    Manufacturer = models.CharField(max_length=700, default=False, null=True, blank=True)
    Model = models.CharField(max_length=700, default=False, null=True, blank=True)
    Status = models.CharField(max_length=700, default=False, null=True, blank=True)
    Substatus = models.CharField(max_length=700, default=False, null=True, blank=True)
    Reservedby = models.CharField(max_length=700, null=True, blank=True)
    Reserved_at = models.DateTimeField(default=datetime.now)
    Configname = models.CharField(max_length=700, null=True, blank=True)
    Program = models.CharField(max_length=700, default=False, null=True, blank=True)
    Project = models.CharField(max_length=700, default=False, null=True, blank=True)
    PONo = models.CharField(max_length=700, default=False, null=True, blank=True)
    POlineNo = models.CharField(max_length=700, default=False, null=True, blank=True)
    Assignto = models.CharField(max_length=700, default=False, null=True, blank=True)
    Assigned_at = models.DateTimeField(default=datetime.now, blank=True)
    warranty_date = models.CharField(max_length=700, default='20/12/24', null=True, blank=True)
    Type = models.CharField(max_length=700, default=False, null=True, blank=True)
    Count = models.CharField(max_length=700, default=1, null=True, blank=True)
    item_img = models.CharField(max_length=700, default=False, null=True, blank=True)
    vendor_id = models.CharField(max_length=700, default=False, null=True, blank=True)
    Ownedby = models.CharField(max_length=700, default=False, null=True, blank=True)
    Managedby = models.CharField(max_length=700, default=False, null=True, blank=True)
    HomeLoc = models.CharField(max_length=700, default=False, null=True, blank=True)
    Location = models.CharField(max_length=700, default=False, null=True, blank=True)
    LocDetails = models.CharField(max_length=700, default=False, null=True, blank=True)
    Created = models.CharField(max_length=700, default=False, null=True, blank=True)
    Createdby = models.CharField(max_length=700, default=False, null=True, blank=True)
    Updated = models.CharField(max_length=700, default=False, null=True, blank=True)
    Updatedby = models.CharField(max_length=700, default=False, null=True, blank=True)
    Costcent = models.CharField(max_length=700, default=False, null=True, blank=True)
    Comments = models.CharField(max_length=700, default=False, null=True, blank=True)
    FinaType = models.CharField(max_length=700, default=False, null=True, blank=True)
    HardSuppG = models.CharField(max_length=700, default=False, null=True, blank=True)
    HardSuppSer = models.CharField(max_length=700, default=False, null=True, blank=True)
    LotNo = models.CharField(max_length=700, default=False, null=True, blank=True)
    Etag = models.CharField(max_length=700, default=False, null=True, blank=True)

    def __str__(self):
	    return self.name

class Class1(models.Model):
  class_name = models.CharField(max_length=255, unique=True)

  def __str__(self):
    return self.class_name


class Category(models.Model):
  category_name = models.CharField(max_length=255, unique=True)
  class_name = models.ForeignKey(Class1, related_name='Categories', on_delete=models.CASCADE)
#   manufacturer_name = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, default=None)
  def __str__(self):
    return self.category_name


class Subcategory(models.Model):
  subcategory_name = models.CharField(max_length=255, unique=True)
  category_name = models.ForeignKey(Category, on_delete=models.CASCADE)

  def __str__(self):
    return self.subcategory_name


class Manufacturer(models.Model):
  manufacturer_name = models.CharField(max_length=255, unique=True)
  class_name = models.ForeignKey(Class1, on_delete=models.CASCADE, default=None)
  subcat_name = models.ForeignKey(Category, related_name='manufacturer', on_delete=models.CASCADE)
  def __str__(self):
    return self.manufacturer_name


class Model(models.Model):
  model_name = models.CharField(max_length=255, unique=True)
  class_name = models.ForeignKey(Class1, on_delete=models.CASCADE, default=None)
  subcat_name = models.ForeignKey(Category, on_delete=models.CASCADE, default=None)
  manufacturer_name = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, default=None)

  def __str__(self):
    return self.model_name
  
class ConfigName(models.Model):
    name = models.CharField(max_length=700, unique=True)
    
    def __str__(self):
	    return self.name
    
class Config(models.Model):
    name = models.ForeignKey(ConfigName, related_name="configname", on_delete=models.CASCADE, default=None)
    Class = models.CharField(max_length=700, unique=False)
    Category = models.CharField(max_length=700, unique=False, default=False)
    Manufacturer = models.CharField(max_length=700, unique=False, default=False)
    Model = models.CharField(max_length=700, unique=False, default=False)
    quantity = models.CharField(max_length=700, unique=False, default=False)

    def __str__(self):
	    return self.Class
    
