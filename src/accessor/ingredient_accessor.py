from .accessor import Accessor
from src.model.ingredient_model import Ingredient

class IngredientAccessor(Accessor):
    
    table = 'ingredient'
    model_class = Ingredient