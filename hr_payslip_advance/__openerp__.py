# -*- coding: utf-8 -*-
{
    'name': 'HR Payslip Advance',
    'description': 'Manage employee payslip advances',
    'version': '8.0.0.1',
    'author': 'robert.gauto@gmail.com',
    'depends': ['account', 'hr'],
    'data': [
        'views/hr_payslip_advance_view.xml',
        'views/hr_contract_view.xml',
        'views/hr_payslip_view.xml',
        'reports/hr_payslip_advance_report.xml',
        'reports/hr_payslip_advance_refund_report.xml'
    ],
    'installable': True
}

