# routers/matches.py
import strawberry
from strawberry.fastapi import GraphQLRouter
from typing import List, Optional
from mongo.models import Matches

@strawberry.type
class Match:
    match_id: int
    team_home: int
    team_away: int
    events: List[str]

@strawberry.type
class Query:
    @strawberry.field
    def get_match(self, match_id: int) -> Optional[Match]:
        match = Matches.objects(match_id=match_id).first()
        if match:
            return Match(
                match_id=match.match_id,
                team_home=match.team_home,
                team_away=match.team_away,
                events=match.events
            )
        return None

    @strawberry.field
    def get_matches_by_team(self, team_id: int) -> List[Match]:
        matches = Matches.objects.filter(__raw__={'$or': [{'team_home': team_id}, {'team_away': team_id}]})
        return [
            Match(
                match_id=match.match_id,
                team_home=match.team_home,
                team_away=match.team_away,
                events=match.events
            )
            for match in matches
        ]

    @strawberry.field
    def all_matches(self) -> List[Match]:
        matches = Matches.objects.all()
        return [
            Match(
                match_id=match.match_id,
                team_home=match.team_home,
                team_away=match.team_away,
                events=match.events
            )
            for match in matches
        ]

# Define the GraphQL schema
schema = strawberry.Schema(query=Query)

# Create a GraphQL router
matches_router = GraphQLRouter(schema=schema)