# -*- coding: utf-8 -*-
from graphql import (
    GraphQLSchema,
    GraphQLObjectType,
)

from .queries import welcome_query
from .queries.product_product_query import product_product_query
from .queries.product_template_query import product_template_query

from .types import product_product_type
from .types import product_template_type

root_query = GraphQLObjectType(
    name='root_query',
    fields=lambda: {
        'welcome': welcome_query,
        'product_product': product_product_query,
        'product_template': product_template_query
    }
) 

root_schema = GraphQLSchema(
    query=root_query,
    types=[
        product_product_type,
        product_template_type
    ]
)
