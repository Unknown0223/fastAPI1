from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
from enum import Enum
app = FastAPI()

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

class Item(BaseModel):
    name: str
    price: float
    is_offer: Optional[bool] = None


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name == ModelName.alexnet:
        return {"model_name":model_name, "message": "DeepAlex"}
    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "DeepLenet"}

    return {"model_name": model_name, "message": "DeepResnet"}


@app.put("/itms/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}
