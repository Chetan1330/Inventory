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

# models.py
from import_export import resources

class StockResource(resources.ModelResource):

    class Meta:
        model = Stock
        import_id_fields = ["name", "SSN"]
        skip_unchanged = True
        use_bulk = True