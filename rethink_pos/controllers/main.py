# -*- coding: utf-8 -*-
from openerp import http
from openerp.http import request

from product_product import get_product_product

class RethinkPosController(http.Controller):

    '''
    '''
    def get_data(self):
        return {
            'res_partner': [],
            'product_product': get_product_product()
        }

    '''
        
    '''
    @http.route('/rethink_pos', type='http', auth='user', methods=('GET', 'POST'))
    def pos_route(self, **kwargs):
        if request.METHOD == 'GET':
            return self.get_data()

        if request.METHOD == 'POST':
            pass
