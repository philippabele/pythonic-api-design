from typing import List

from pydantic import BaseModel


class IdeaModel(BaseModel):
    recipes: List
    easyRecipes: List
    topSecretRecipes: List
