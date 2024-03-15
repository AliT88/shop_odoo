{
    "name" : "Real Estate Advertisments",
    "version" : "1.0",
    "author" : "Ali Taheri",
    "description" : "This is my estate agency online",
    "application" : True,
    "installable" : True,
    "depends" : ['base',],
    "data" : [
        "security/ir.model.access.csv",   

        "views/property_view.xml",
        "views/property_type_view.xml",
        "views/property_tag_view.xml",

        "views/menu_items.xml",
    ]
}