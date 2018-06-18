# -*- coding: utf-8 -*-
{
    'name': "Open Academy",
    'summary': """Manage trainings""",
    'description': """
        Open Academy module for managing trainings:
            - training courses
            - training sessions
            - attendees registration
    """,
    'author': "IT KDVN",
    'website': "http://www.kindenvietnam.com.vn",
    
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Demo',
    'version': '0.1',
    
    # any module necessary for this one to work correctly
    'depends': ['base', 'board', 'report'],
    
    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
		#Views
        'views/openacademy_templates.xml',
        'views/openacademy_view.xml',
        'views/session_board_view.xml',
        'views/inherit_partner_view.xml',
		#Wizard
        'wizard/openacademy_wizard.xml',
		'wizard/create_delete_wizard.xml',
        'wizard/import_data_wizard.xml',
		#Report
		'report/openacademy_report.xml',
		'report/paper_format_template.xml',
		'report/template_report.xml',
    ],
    
    # only loaded in demonstration mode
    'demo': [
        'data/demo.xml',
    ],
}