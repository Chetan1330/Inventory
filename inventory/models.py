from django.db import models
    
class Stock(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=700, unique=False)
    quantity = models.IntegerField(default=1)
    is_deleted = models.BooleanField(default=False)

    SSN = models.CharField(max_length=700, default=False)
    Name = models.CharField(max_length=700, default=False)
    DNUSAN = models.CharField(max_length=700, default=False)
    Shortdesc = models.CharField(max_length=700, default=False)
    Class = models.CharField(max_length=700, default=False)
    Category = models.CharField(max_length=700, default=False)
    Subcategory = models.CharField(max_length=700, default=False)
    Manufacturer = models.CharField(max_length=700, default=False)
    Model = models.CharField(max_length=700, default=False)
    Status = models.CharField(max_length=700, default=False)
    Substatus = models.CharField(max_length=700, default=False)
    Program = models.CharField(max_length=700, default=False)
    Project = models.CharField(max_length=700, default=False)
    PONo = models.CharField(max_length=700, default=False)
    POlineNo = models.CharField(max_length=700, default=False)
    Assignto = models.CharField(max_length=700, default=False)
    Ownedby = models.CharField(max_length=700, default=False)
    Managedby = models.CharField(max_length=700, default=False)
    HomeLoc = models.CharField(max_length=700, default=False)
    Location = models.CharField(max_length=700, default=False)
    LocDetails = models.CharField(max_length=700, default=False)
    Created = models.CharField(max_length=700, default=False)
    Createdby = models.CharField(max_length=700, default=False)
    Updated = models.CharField(max_length=700, default=False)
    Updatedby = models.CharField(max_length=700, default=False)
    Costcent = models.CharField(max_length=700, default=False)
    Comments = models.CharField(max_length=700, default=False)
    FinaType = models.CharField(max_length=700, default=False)
    HardSuppG = models.CharField(max_length=700, default=False)
    HardSuppSer = models.CharField(max_length=700, default=False)
    LotNo = models.CharField(max_length=700, default=False)
    Etag = models.CharField(max_length=700, default=False)

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
    
# models.py
from import_export import resources

class StockResource(resources.ModelResource):

    class Meta:
        model = Stock
        import_id_fields = ["name", "SSN"]
        skip_unchanged = True
        use_bulk = True