# -*- coding: utf-8 -*-
from openerp import models, fields


class ResPartner(models.Model):
    _inherit = 'res.partner'

    din = fields.Char(string='CIN', size=35)
    ssn = fields.Char(string='IPS', size=35)
    tin = fields.Char(string='RUC', size=35)
    ein = fields.Char(string='EIN', size=35)