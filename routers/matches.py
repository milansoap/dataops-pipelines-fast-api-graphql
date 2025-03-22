import strawberry
from strawberry.fastapi import GraphQLRouter

from services.matches.matches_queries import Query
from services.matches.matches_mutations import Mutation  # Assuming you have this

# Define the GraphQL schema
schema = strawberry.Schema(query=Query, mutation=Mutation)

# Create a GraphQL router
matches_router = GraphQLRouter(schema=schema)