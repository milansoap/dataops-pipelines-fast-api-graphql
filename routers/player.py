import strawberry
from strawberry.fastapi import GraphQLRouter
from schemas import Players

# Define the GraphQL schema
schema = strawberry.Schema(query=Players)

# Create a GraphQL router
player_router = GraphQLRouter(schema=schema)