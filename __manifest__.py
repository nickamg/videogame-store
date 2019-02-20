# -*- coding: utf-8 -*-
{
    'name': "Videogame Store",

    'summary': """
        App for managing a videogame store.
    """,

    'description': """
        It has all the necessary components to run and manage a videogame store.
    """,

    'author': "Nicolás Magallón, Guillermo Ye, Óscar Sanclemente",
    'website': "https://www.odoo.com/documentation/12.0/howtos/backend.html",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'App',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'views/views.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],

    'installable': True,
    'auto_install': False,
    'application': True,
}