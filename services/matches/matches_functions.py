# services/matches.py
from typing import List, Optional, Any

from mongo.models import Matches

class MatchService:
    @staticmethod
    def get_match(match_id: int) -> Optional[Matches]:
        return Matches.objects(match_id=match_id).first()

    @staticmethod
    def get_matches_by_team(team_id: int) -> List[Matches]:
        return Matches.objects.filter(__raw__={'$or': [{'team_home': team_id}, {'team_away': team_id}]})

    @staticmethod
    def all_matches() -> List[Matches]:
        return Matches.objects.all()

    @staticmethod
    def create_match(match_id: int, team_home: int, team_away: int, events: Any) -> Matches:
        match = Matches(
            match_id=match_id,
            team_home=team_home,
            team_away=team_away,
            events=events
        ).save()
        return match

    @staticmethod
    def add_event_to_match(match_id: int, event: str) -> Optional[Matches]:
        match = Matches.objects(match_id=match_id).first()
        if match:
            match.events.append(event)
            match.save()
            return match
        return None