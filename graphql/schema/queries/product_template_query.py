# -*- coding: utf-8 -*-
from graphql import (
    GraphQLUnionType,
    GraphQLField,
    GraphQLArgument,
    GraphQLList,
    GraphQLInt
)
from openerp.http import request
from ..types.product_template_type import product_template_type

def fetch(kwargs):
    domain = []

    if kwargs.get('id', None):
        domain.append(('id', '=', kwargs.get('id')))

    products = request.env['product.template'].search(domain)
    return products

product_template_query = GraphQLField(
    type=GraphQLList(product_template_type),
    args={
        'id': GraphQLArgument(
            type=GraphQLInt
        )
    },
    resolver=lambda *_, **kwargs: fetch(args)
)
