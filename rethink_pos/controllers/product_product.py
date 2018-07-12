# -*- coding: utf-8 -*-
from openerp.http import request

_MODEL = 'product.product'
_FIELDS = [
    'id',
    'name',
    'display_name',
    'list_price'
]

'''
'''
def get_product_product():
    domain = [('active', '=', True)]
    product_obj = request.env[_MODEL]
    product_ids = product_obj.search(domain)

    return product_ids.read(_FIELDS)
 
'''
'''
def create_product_product(values):
    pass
