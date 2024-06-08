from fastapi import FastAPI

app = FastAPI()


@app.get("/v1/pokemon/{pokemon_id}")
async def get_pokemon(pokemon_id):
    return {"pokemon_id": pokemon_id}

