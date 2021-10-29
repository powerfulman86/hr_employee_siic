# -*- coding: utf-8 -*-
{
    'name': "Employee SIIC Customization",
    'summary': """  Custom Application for Employee SIIC Customization """,
    'description': """ Employee SIIC Customization  """,
    'author': "SIIC",
    'category': 'Human Resources/Employees',
    'depends': ['base', 'multi_branch', 'hr'],
    'data': [
        # 'security/security.xml',
        # 'security/ir.model.access.csv',
        # 'data/sequence.xml',
        'data/ir_cron.xml',
        'views/hr_employee.xml',
    ],
    'images': ['static/description/icon.png'],
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,
}
