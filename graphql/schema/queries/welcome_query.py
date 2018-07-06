# -*- coding: utf-8 -*-
from graphql import (
    GraphQLField,
    GraphQLString
)

welcome_query = GraphQLField(
    type=GraphQLString,
    resolver=lambda *_: 'Welcome to GraphQL API'
)