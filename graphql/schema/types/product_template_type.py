# -*- coding: utf-8 -*-
from graphql import (
    GraphQLObjectType,
    GraphQLField,
    GraphQLInt,
    GraphQLString,
    GraphQLFloat,
    GraphQLBoolean,
    GraphQLList
)
import product_product_type

product_template_type = GraphQLObjectType(
    name='product_template',
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
        'variants': GraphQLField(
            type=GraphQLList(product_product_type.product_product_type),
            resolver=lambda root, *_: root.product_variant_ids
        )
    }
)
