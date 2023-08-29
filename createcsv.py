import csv

with open('newinv3.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    field = ['Name', 'Serial number', 'Class', 'DNUSAN', 'Short description', 'Category', 'Subcategory', 'Manufacturer', 'Model',
            'Status(hardware_status)', 'Substatus', 'Type', 'Count', 'Program', 'Project', 'PO number', 'PO line number', 'Assigned to', 'Owned by', 'Managed by', 'Home Location',
            'Location', 'Location Details', 'Created', 'Created by', 'Updated', 'Updgted by', 'Cost center', 
            'Comments', 'Finance Type', 'Hardware Support Group', 'Hardware Support Service', 'Lot Number', 'Etag']
    writer.writerow(field)

    for i in range(0,40):
        writer.writerow([str(i)+"name" + "Netadapter", str(i) + "Netadapter", "Net Adapter-Lab", 'JVF', '', 'Net Adapter-Lab - vfg', '', 'Mellanox Technologies', 'ConnectX-6 VPI Adapter Card - MCX653106A-ECAT-SP',
                         'In Stock', 'Available', 'Serialwise', 1, 'EGS-R', 'JKL_RASP', '', '', '', '', '', '', '',
                         '', '', '', '', '', '', '', '', '', '', '', ''])
        
        writer.writerow([str(i)+"name" + "Memory", str(i) + "Memory", "Memory", 'JVF', '', 'Memory - vfg', '', 'Memory2.4', 'abcd Optane Memory',
                         'In Stock', 'Available', 'Serialwise', 1, 'EGS-R', 'JKL_RASP', '', '', '', '', '', '', '',
                         '', '', '', '', '', '', '', '', '', '', '', ''])
        
        # writer.writerow([str(i) + 'Memory', str(i)+"name" + "Memory", str(i) + "Memory", "Memory", 'Memory - vfg', 'Memory2.4', 'abcd Optane Memory',
        #                  'In Stock', 'Available', 'Serialwise'])
        
        # stock=Stock.objects.create(name=str(i) + "Power Supply", Name =str(i)+"name" + "Power Supply", SSN = str(i) + "Power Supply", Class= "Power Supply",
        #                 Category='Power - vfg', Manufacturer='DONGGUAN GUANGSHU ELECTRICAL TECHNOLOGY CO.,LTD',
        #                 Model='SERVER SMPS;SERVER,I1600W,1600W,2CH,90Vac~264Vac,+12 - G36234-019', Status='In Stock', Substatus='Available', Type='Serialwise'
        #                 )
        
        # stock.save()
        
        # stock=Stock.objects.create(name=str(i) + "MassStorage", Name =str(i)+"name" + "MassStorage", SSN = str(i) + "MassStorage", Class= "Mass Storage Device",
        #                 Category='MassStorage - vfg', Manufacturer='abcd2',
        #                 Model='abcd Optane M.2 Nvme SSD 118GB P1600X Series; MM# 99AGG3 - Mike', Status='In Stock', Substatus='Available', Type='Serialwise'
        #                 )
        
        # stock.save()
        
        # stock=Stock.objects.create(name=str(i) + "Memory", Name =str(i)+"name" + "Memory", SSN = str(i) + "Memory", Class= "Memory",
        #                 Category='Memory - vfg', Manufacturer='Memory2.4',
        #                 Model='abcd Optane Memory', Status='In Stock', Substatus='Available', Type='Serialwise'
        #                 )
        
        # stock.save()