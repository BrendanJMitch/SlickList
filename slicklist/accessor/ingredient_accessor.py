from .accessor import Accessor
from slicklist.model.ingredient_model import Ingredient

class IngredientAccessor(Accessor):
    
    table = 'ingredient'
    model_class = Ingredient