{
    'name': 'Odoo Nelson',
    'version': '1.0',
    'author': 'Nelson René Gordillo González',
    'category': 'Tests',
    'summary': 'Odoo Nelson Module',
    'website': 'https://www.odoo.com',
    'description': """
        Odoo Nelson Module for testing purposes
    """,
    'depends': [
        'base',
        'mail'
    ],
    'data':[
        # Security
        'security/security.xml',
        'security/ir.model.access.csv',

        # Views
        'views/main_menu_view.xml',
        'views/configuration/department_view.xml',
        'views/configuration/employee_category_view.xml',
        'views/configuration/request_type_view.xml',
        'views/configuration/employee_view.xml',

        # Data
        'data/department_data.xml',
        'data/employee_category_data.xml',
    ],

    'qweb': [
        
    ],

    'application': True,
    'installable': True,
    'auto_install': False,
}