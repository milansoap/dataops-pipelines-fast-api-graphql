# app/schemas.py

import strawberry
from typing import List

from dependencies import player_crud_service
from models import Player
from sqlalchemy_to_pydantic import sqlalchemy_to_pydantic

# Convert SQLAlchemy User model to Pydantic model
PlayerPydantic = sqlalchemy_to_pydantic(Player)


@strawberry.experimental.pydantic.type(model=PlayerPydantic, all_fields=True)
class PlayerResults:
    """GraphQL type representing user query results."""
    pass


@strawberry.type
class Players:
    """GraphQL root query type."""

    @strawberry.field
    async def get_players(self, limit: int = 10, offset: int = 0) -> List[PlayerResults]:
        """Fetches a list of users with pagination."""
        users = await player_crud_service.get_all_users(limit=limit, offset=offset)
        return users