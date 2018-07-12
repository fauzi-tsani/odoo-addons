# -*- coding: utf-8 -*-
from graphql import (
    GraphQLUnionType,
    GraphQLField,
    GraphQLArgument,
    GraphQLList,
    GraphQLInt
)
from openerp.http import request
from ..types.product_product_type import product_product_type

def fetch(kwargs):
    domain = []

    if kwargs.get('id', None):
        domain.append(('id', '=', kwargs.get('id')))

    products = request.env['product.product'].search(domain)
    return products

product_product_query = GraphQLField(
    type=GraphQLList(product_product_type),
    args={
        'id': GraphQLArgument(
            type=GraphQLInt
        )
    },
    resolver=lambda *_, **kwargs: fetch(kwargs)
)
