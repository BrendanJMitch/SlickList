from dataclasses import dataclass
from .model import Model


@dataclass
class Ingredient(Model):
    id: int
    user_id: int
    name: str
    cost: float 
    add_to_list: bool
    walmart_id: str
    image: str 
    aisle: str
