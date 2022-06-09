import asyncio
from fastapi import APIRouter
from src.app.api.recipes import get_reddit_top, get_reddit_top_async
from src.app.api.idea_models import IdeaModel


router = APIRouter()


@router.get(
    "/",
    summary="Fetch ideas synchronous",
    description="Compare the processing time shown below with the asynchronous example",
    response_model=IdeaModel,
)
def fetch_ideas() -> dict:
    data: dict = {}
    get_reddit_top("recipes", data)
    get_reddit_top("easyRecipes", data)
    get_reddit_top("topSecretRecipes", data)

    return data


@router.get(
    "/async",
    summary="Fetch ideas asynchronously",
    description="Compare the processing time shown below with the synchronous example",
    response_model=IdeaModel,
)
async def fetch_ideas_async() -> dict:
    data: dict = {}

    await asyncio.gather(
        get_reddit_top_async("recipes", data),
        get_reddit_top_async("easyRecipes", data),
        get_reddit_top_async("topSecretRecipes", data),
    )

    return data
