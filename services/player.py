from sqlalchemy.orm import Session
from postgres.models import Player
# from schemas import PlayerCreate, PlayerUpdate
from typing import List


class PlayerCRUD:
    def __init__(self, db: Session):
        self.db = db

    # def create_player(self, player: PlayerCreate) -> Player:
    #     db_player = Player(**player.dict())
    #     self.db.add(db_player)
    #     self.db.commit()
    #     self.db.refresh(db_player)
    #     return db_player
    #
    # def get_player(self, player_id: int) -> Optional[Player]:
    #     return self.db.query(Player).filter(Player.id == player_id).first()

    def get_players(self, skip: int = 0, limit: int = 100) -> List[Player]:
        return self.db.query(Player).offset(skip).limit(limit).all()

    # def update_player(self, player_id: int, player_update: PlayerUpdate) -> Optional[Player]:
    #     db_player = self.get_player(player_id)
    #     if db_player:
    #         for key, value in player_update.dict(exclude_unset=True).items():
    #             setattr(db_player, key, value)
    #         self.db.commit()
    #         self.db.refresh(db_player)
    #         return db_player
    #     return None
    #
    # def delete_player(self, player_id: int) -> bool:
    #     db_player = self.get_player(player_id)
    #     if db_player:
    #         self.db.delete(db_player)
    #         self.db.commit()
    #         return True
    #     return False