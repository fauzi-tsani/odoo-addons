# -*- coding: utf-8 -*-
{
    'name': 'HR Payslip Report Extended',
    'description': 'Extend Payslip Report',
    'version': '8.0.0.1',
    'author': 'robert.gauto@gmail.com',
    'depends': [
        'hr_payroll',
        'hr_employee_extra_fields'
    ],
    'data': [
        'reports/hr_payslip_report.xml',
    ],
    'installable': True
}
