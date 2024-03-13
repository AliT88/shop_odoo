{
    "name" : "shop",
    "depends" : ['base',],
    "version" : "1.0",
    "author" : "Ali Taheri",
    "description" : """
                This is my shop.
    """,
    "data" : [
        'security/ir.model.access.csv',
        'views/category_view.xml',
        'views/user_view.xml',
        'views/order_view.xml',
        'views/order_items_view.xml',
        'views/product_view.xml',
        'views/menu_items.xml',
        'views/coupon_view.xml',
        ],
    "application" : True,
    "installable" : True,
}