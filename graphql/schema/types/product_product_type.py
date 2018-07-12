# -*- coding: utf-8 -*-
from graphql import (
    GraphQLObjectType,
    GraphQLField,
    GraphQLInt,
    GraphQLString,
    GraphQLFloat,
    GraphQLBoolean
)
import product_template_type
    
product_product_type = GraphQLObjectType(
    name='product_product',
    fields=lambda: {
        'id': GraphQLField(
            type=GraphQLInt
        ),
        'name': GraphQLField(
            type=GraphQLString
        ),
        'display_name': GraphQLField(
            type=GraphQLString
        ),
        'price': GraphQLField(
            type=GraphQLFloat
        ),
        'list_price': GraphQLField(
            type=GraphQLFloat
        ),
        'code': GraphQLField(
            type=GraphQLString
        ),
        'default_code': GraphQLField(
            type=GraphQLString
        ),
        'ean13': GraphQLField(
            type=GraphQLString
        ),
        'image': GraphQLField(
            type=GraphQLString
        ),
        'image_medium': GraphQLField(
            type=GraphQLString
        ),
        'image_small': GraphQLField(
            type=GraphQLString
        ),
        'active': GraphQLField(
            type=GraphQLBoolean
        ),
        'template': GraphQLField(
            type=product_template_type.product_template_type,
            resolver=lambda root, *_: root.product_tmpl_id
        )
    }
)
