# -*- coding: utf-8 -*-
{
    'name': "mm_potranca",

    'summary': """
        Módulo Mit-Mut para personalizaciones Potranca""",

    'description': """
        Módulo Mit-Mut para personalizaciones Potranca
    """,

    'author': "Mit-Mut",
    'website': "https://www.mit-mut.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Mit-Mut',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base_automation', 'hr', 'account', 'odoo_customer_credit_limit', 'stock', 'purchase'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        #'views/views.xml',
        'views/inherit_res_partner.xml',
        'views/inherit_res_company.xml',
        'views/inherit_sele_views.xml',
        'views/inherit_stock_quant_views.xml',
        'views/inherit_stock_inventory.xml',
        'views/inherit_stock_location.xml',
        'views/inherit_stock_move_line_view.xml',
        'data/automated_actions.xml',
    ],
}
