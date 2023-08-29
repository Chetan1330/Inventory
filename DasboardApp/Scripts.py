######################  Script 1  ###########################################

with open('Inventory.csv', mode="r", encoding='latin1') as csv_file:
    # csv_reader = csv.DictReader(csv_file)
    for row in csv.DictReader(csv_file):
        if Stock.objects.filter(SSN=row['Serial number'], name=row['Name'], Name=row['Name']).exists():
            # print("count", Stock.objects.filter(SSN=row['Serial number'], name=row['Name'], Name=row['Name']).count())
            pass
        else:
            stock=Stock(name=row['Name'], Name=row['Name'], SSN=row['Serial number'], Class=row['Class'],
                        DNUSAN=row['DNUSAN'], Shortdesc=row['Short description'],Category=row['Category'],Subcategory=row['Subcategory'],Manufacturer=row['Manufacturer'],
                        Model=row['Model'],Status=row['Status(hardware_status)'],Substatus=row['Substatus'],Program=row['Program'],Project=row['Project'],
                        PONo=row['PO number'],POlineNo=row['PO line number'],Assignto=row['Assigned to'],Ownedby=row['Owned by'],Managedby=row['Managed by'],
                        HomeLoc=row['Home Location'],Location=row['Location'],LocDetails=row['Location Details'],Created=row['Created'],Createdby=row['Created by'],
                        Updated=row['Updated'],Updatedby=row['Updgted by'],Costcent=row['Cost center'],Comments=row['Comments'],
                        FinaType=row['Finance Type'],HardSuppG=row['Hardware Support Group'],HardSuppSer=row['Hardware Support Service'],LotNo=row['Lot Number'],
                        Etag=row['Etag'])
            stock.save()

###########################  Script 2  ####################################

with open('Inventory.csv', mode="r", encoding='latin1') as csv_file:
    # csv_reader = csv.DictReader(csv_file)
    for row in csv.DictReader(csv_file):
        if Class1.objects.filter(class_name = row['Class']).exists():
            # print("Yes")
            pass
        elif Manufacturer.objects.filter(manufacturer_name = row['Manufacturer'] ).exists():
            # print("Cat exist")
            pass
        else:
            if row['Class']:
                stock_class=Class1.objects.create(class_name = row['Class'])
                print('Stock class:', stock_class.class_name)
                stock_class.save()
            if row['Category']:
                category = Category.objects.create(category_name = row['Category'], class_name = stock_class )
                category.save()
            if row['Subcategory']:
                subcategory = Category.objects.create(subcategory_name = row['Subcategory'], category_name = category )
                subcategory.save()
            if row['Manufacturer']:
                manufacturer = Manufacturer.objects.create(manufacturer_name = row['Manufacturer'], class_name=stock_class, subcat_name = category )
                manufacturer.save()
            if row['Model']:
                model = Model.objects.create(model_name = row['Model'], class_name=stock_class, subcat_name = category, manufacturer_name = manufacturer )
                model.save()

############################## Script 3  ########################################################

for i in range(0,120):

    stock=Stock.objects.create(name=str(i) + "Netadapter", Name =str(i)+"name" + "Netadapter", SSN = str(i) + "Netadapter", Class= "Net Adapter-Lab",
                    Category='Net Adapter-Lab - vfg', Manufacturer='Mellanox Technologies',
                    Model='ConnectX-6 VPI Adapter Card - MCX653106A-ECAT-SP', Status='In Stock', Substatus='Available', Type='Serialwise',
                    )
    stock.save()
    stock=Stock.objects.create(name=str(i) + "Power Supply", Name =str(i)+"name" + "Power Supply", SSN = str(i) + "Power Supply", Class= "Power Supply",
                    Category='Power - vfg', Manufacturer='DONGGUAN GUANGSHU ELECTRICAL TECHNOLOGY CO.,LTD',
                    Model='SERVER SMPS;SERVER,I1600W,1600W,2CH,90Vac~264Vac,+12 - G36234-019', Status='In Stock', Substatus='Available', Type='Serialwise'
                    )
    
    stock.save()
    
    stock=Stock.objects.create(name=str(i) + "MassStorage", Name =str(i)+"name" + "MassStorage", SSN = str(i) + "MassStorage", Class= "Mass Storage Device",
                    Category='MassStorage - vfg', Manufacturer='abcd2',
                    Model='abcd Optane M.2 Nvme SSD 118GB P1600X Series; MM# 99AGG3 - Mike', Status='In Stock', Substatus='Available', Type='Serialwise'
                    )
    
    stock.save()
    
    stock=Stock.objects.create(name=str(i) + "Memory", Name =str(i)+"name" + "Memory", SSN = str(i) + "Memory", Class= "Memory",
                    Category='Memory - vfg', Manufacturer='Memory2.4',
                    Model='abcd Optane Memory', Status='In Stock', Substatus='Available', Type='Serialwise'
                    )
    
    stock.save()

############################  Script 4  ###########################################################

for i in range(0,1):

    stock=Stock.objects.create(name=str(i) + "Type1Cables", Name =str(i)+"name" + "Type1Cables", SSN = str(i) + "Type1Cables", Class= "Cables",
                    Category='CablesType1 - vfg', Manufacturer='Type1Cables',
                    Model='Type1Cables Optane M.2', Status='In Stock', Substatus='Available', Type='Lotwise', Count='300'
                    )
    
    stock.save()
    stock=Stock.objects.create(name=str(i) + "Type2Cables", Name =str(i)+"name" + "Type2Cables", SSN = str(i) + "Type2Cables", Class= "Cables",
                    Category='CablesType2 - vfg', Manufacturer='Type2Cables',
                    Model='Type2Cables Optane M.2', Status='In Stock', Substatus='Available', Type='Lotwise', Count='440'
                    )
    
    stock.save()
    stock=Stock.objects.create(name=str(i) + "Type3Cables", Name =str(i)+"name" + "Type3Cables", SSN = str(i) + "Type3Cables", Class= "Cables",
                    Category='CablesType3 - vfg', Manufacturer='Type3Cables2',
                    Model='Type3Cables Optane M.2', Status='In Stock', Substatus='Available', Type='Lotwise', Count='120'
                    )
    
    stock.save()