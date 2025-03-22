import strawberry
from typing import List
from dependencies import player_crud_service
from postgres.models import Player
from sqlalchemy_to_pydantic import sqlalchemy_to_pydantic

PlayerPydantic = sqlalchemy_to_pydantic(Player)

@strawberry.experimental.pydantic.type(model=PlayerPydantic, all_fields=True)
class PlayerResults:
    """GraphQL type representing user query results."""
    pass

@strawberry.type
class Players:
    """GraphQL root query type."""

    @strawberry.field
    async def get_players(self, limit: int = 10) -> List[PlayerResults]:
        """Fetches a list of users with pagination."""
        players = player_crud_service.get_players(limit=limit)
        results = [PlayerResults.from_pydantic(player) for player in players]
        return results