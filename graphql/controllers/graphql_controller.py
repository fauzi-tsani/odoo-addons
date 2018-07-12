# -*- coding: utf-8 -*-
from openerp import http
from graphql import graphql
from ..schema import root_schema

class GraphQLController(http.Controller):

    '''
    '''
    @http.route('/graphql', type='json', auth='user',  methods=['POST'], cors='*')
    def graphql_api(self, **kw):
        query = kw.get('query', None)
        result = graphql(root_schema, '{ %s }' % query)

        data = result.data or {}
        errors = []

        for e in result.errors or []:
            errors.append(e.message)

        return {
            'data': dict(data) or None,
            'errors': errors or None
        }
