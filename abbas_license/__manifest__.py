# -*- coding: utf-8 -*-
{
    'name': "Abbas_license",

    'summary': """
""",

    'description': """
        
    """,

    'author': "عباس عزالدین",
    'website': "http://www.abbas.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Abbas',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['web_enterprise'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        # 'views/views.xml',
        # 'views/templates.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'abbas_license/static/src/js/enterpriseSubscriptionService.js',
            'abbas_license/static/src/xml/home_menu.xml',
        ],
    },
    'sequence': 1,
    'license': "AGPL-3",
    'installable': True,
    'application': False,

}
