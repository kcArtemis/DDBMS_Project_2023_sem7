import json
DIC = {
"SITES": [{
    "idSite":1,
    "User":"user",
    "ip":"10.3.5.211",
    "password" : "iiit123",
    "HostName" : "CP5"
},{
    "idSite":2,
    "User":"user",
    "ip":"10.3.5.208",
    "password" : "iiit123",
    "HostName" : "CP6"
},{
    "idSite":3,
    "User":"user",
    "ip":"10.3.5.204",
    "password" : "iiit123",
    "HostName" : "CP7"
},{
    "idSite":4,
    "User":"user",
    "ip":"10.3.5.205",
    "password" : "iiit123",
    "HostName" : "CP8"
}] 
,
"RELATIONS" : [
    {
        "idTable":0,
        "TableName":"Restaurant",
        "ColumnsNo":4,
        "FragCount":4,
        "FragmentationType":"H",
    },
    {
        "idTable":1,
        "TableName":"Menu",
        "ColumnsNo":5,
        "FragCount":4,
        "FragmentationType":"DH",
    },
    {
        "idTable":2,
        "TableName":"Users",
        "ColumnsNo":6,
        "FragCount":4,
        "FragmentationType":"V",
    },
    {
        "idTable":3,
        "TableName":"Orderr",
        "ColumnsNo":4,
        "FragCount":1,
        "FragmentationType":"None",
    },
    {
        "idTable":4,
        "TableName":"OrderItem",
        "ColumnsNo":4,
        "FragCount":1,
        "FragmentationType":"None",
    }
],
"FRAGMENTATION" : [
    {
        "FragmentationID":1,
        "FragmentationCondition":"zone=NORTH",
        "SiteId":1,
        "RelationId":1
    },
    {
        "FragmentationID":2,
        "FragmentationCondition":"zone=SOUTH",
        "SiteId":2,
        "RelationId":1
    },
    {
        "FragmentationID":3,
        "FragmentationCondition":"zone=EAST",
        "SiteId":3,
        "RelationId":1        
    },
    {
        "FragmentationID":4,
        "FragmentationCondition":"zone=WEST",
        "SiteId":4,
        "RelationId":1      
    },
    {
        "FragmentationID":5,
        "FragmentationCondition":"Restaurant,zone=NORTH",
        "SiteId":1,
        "RelationId":2
    },
    {
        "FragmentationID":6,
        "FragmentationCondition":"Restaurant,zone=SOUTH",
        "SiteId":2,
        "RelationId":2
    },
    {
        "FragmentationID":7,
        "FragmentationCondition":"Restaurant,zone=EAST",
        "SiteId":3,
        "RelationId":2
    },
    {
        "FragmentationID":8,
        "FragmentationCondition":"Restaurant,zone=WEST",
        "SiteId":4,
        "RelationId":2
    },
    {
        "FragmentationID":9,
        "FragmentationCondition":"9,11,10",
        "SiteId":1,
        "RelationId":3   
    },
    {
        "FragmentationID":10,
        "FragmentationCondition":"9,12,14",
        "SiteId":2,
        "RelationId":3
    },
    {
        "FragmentationID":11,
        "FragmentationCondition":"9,13",
        "SiteId":3,
        "RelationId":3   
    },
    {
        "FragmentationID":11,
        "FragmentationCondition":"None",
        "SiteId":4,
        "RelationId":4 
    },
    {        
        "FragmentationID":11,
        "FragmentationCondition":"None",
        "SiteId":4,
        "RelationId":5
    }

],
"COLUMNS":[
    {
        "ColumnID":0,
        "ColumnType":"int",
        "ColumnName":"RestaurantID",
        "TableID":1
    }, 
    {
        "ColumnID":1,
        "ColumnType":"varchar(50)",
        "ColumnName":"RestaurantName",
        "TableID":1        
    }, 
    {
        "ColumnID":2,
        "ColumnType":"varchar(50)",
        "ColumnName":"Zone",
        "TableID":1        
    }, 
    {
        "ColumnID":3,
        "ColumnType":"varchar(50)",
        "ColumnName":"FragmentType",
        "TableID":1
    },
    {
        "ColumnID":4,
        "ColumnType":"int",
        "ColumnName":"MenuID",
        "TableID":2  
    },
    {
        "ColumnID":5,
        "ColumnType":"int",
        "ColumnName":"RestaurantID",
        "TableID":2        
    },
    {
        "ColumnID":6,
        "ColumnType":"varchar(50)",
        "ColumnName":"Name",
        "TableID":2    
    },
    {
        "ColumnID":7,
        "ColumnType":"varchar(50)",
        "ColumnName":"Description",
        "TableID":2        
    },
    {
        "ColumnID":8,
        "ColumnType":"varchar(50)",
        "ColumnName":"Cuisine",
        "TableID":2        
    },
    {
        "ColumnID":9,
        "ColumnType":"int",
        "ColumnName":"idUsers",
        "TableID":3            
    },
    {
        "ColumnID":10,
        "ColumnType":"varchar(50)",
        "ColumnName":"Address",
        "TableID":3
    },
    {
        "ColumnID":11,
        "ColumnType":"varchar(50)",
        "ColumnName":"Name",
        "TableID":3        
    },
    {
        "ColumnID":12,
        "ColumnType":"int",
        "ColumnName":"Number",
        "TableID":3        
    },
    {
        "ColumnID":13,
        "ColumnType":"varchar(50)",
        "ColumnName":"Gender",
        "TableID":3        
    },
    {
        "ColumnID":14,
        "ColumnType":"varchar(50)",
        "ColumnName":"emailid",
        "TableID":3
    },
    {
        "ColumnID":15,
        "ColumnType":"int",
        "ColumnName":"OrderID",
        "TableID":4
    },
    {
        "ColumnID":16,
        "ColumnType":"int",
        "ColumnName":"UserID",
        "TableID":4    
    },
    {
        "ColumnID":17,
        "ColumnType":"varchar(50)",
        "ColumnName":"Status",
        "TableID":4         
    },
    {
        "ColumnID":18,
        "ColumnType":"datetime",
        "ColumnName":"Time",
        "TableID":4    
    },
    {
        "ColumnID":19,
        "ColumnType":"int",
        "ColumnName":"ItemID",
        "TableID":5
    },
    {
        "ColumnID":20,
        "ColumnType":"int",
        "ColumnName":"MenuID",
        "TableID":5      
    },
    {
        "ColumnID":21,
        "ColumnType":"int",
        "ColumnName":"OrderID",
        "TableID":5
    },
    {
        "ColumnID":22,
        "ColumnType":"int",
        "ColumnName":"Quantity",
        "TableID":5
    }]
}

with open("../schema.json", "w") as f:
    json.dump(DIC, f, indent=4)


SCHEMA = {
    "SITES": 
    {
            "idSite":"int",
            "User":"varchar(50)",
            "ip":"varchar(50)",
            "password" : "varchar(50)",
            "HostName" : "varchar(50)"
    },
    "RELATIONS" : 
        {
            "idTable":"int",
            "TableName":"varchar(50)",
            "ColumnsNo":"int",
            "FragCount":"int",
            "FragmentationType":"varchar(50)",
        },
    "FRAGMENTATION" :
        {
            "FragmentationID":"int",
            "FragmentationCondition":"varchar(50)",
            "SiteId":"int",
            "RelationId":"int"
        },
    "COLUMNS":
        {
            "ColumnID":"int",
            "ColumnType":"varchar(50)",
            "ColumnName":"varchar(50)",
            "TableID":"int"
        }
}

with open("../schema_type.json", "w") as f:
    json.dump(SCHEMA, f, indent=4)