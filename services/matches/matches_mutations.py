import strawberry
from strawberry.fastapi import GraphQLRouter
from typing import List, Optional, Any
from mongo.models import Matches
from services.matches.matches_functions import MatchService
from services.matches.matches_queries import Match


@strawberry.input
class CreateMatchInput:
    match_id: int
    team_home: int
    team_away: int
    events: List[str]

@strawberry.input
class AddEventInput:
    match_id: int
    event: str


@strawberry.type
class Mutation:
    @strawberry.mutation
    def create_match(self, input: CreateMatchInput) -> Match:
        match_model = MatchService.create_match(
            match_id=input.match_id,
            team_home=input.team_home,
            team_away=input.team_away,
            events=input.events,
        )
        return Match(
            match_id=match_model.match_id,
            team_home=match_model.team_home,
            team_away=match_model.team_away,
            events=match_model.events
        )

    @strawberry.mutation
    def add_event_to_match(self, input: AddEventInput) -> Optional[Match]:
        match_model = MatchService.add_event_to_match(input.match_id, input.event)
        if match_model:
            return Match(
                id=strawberry.ID(str(match_model._id)),
                match_id=match_model.match_id,
                team_home=match_model.team_home,
                team_away=match_model.team_away,
                events=match_model.events
            )
        return None
