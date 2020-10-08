from fastapi import FastAPI
from database.baivarunames import BaivaruNames

app = FastAPI(
    title="Dhivehi Names",
    description="An API for Dhivehi Names",
    version="0.0.1",
)
db = BaivaruNames()

@app.get('/')
async def home():
    return {
        'app': 'BaivaruNames',
        'description': 'Dhivehi Names API',
        'version': '0.0.1',
        'project': 'https://github.com/baivaru/dhivehi-names-http',
        'docs': 'https://dhinames.baiva.ru/docs',
        'available_endpoints': [
            '/random',
            '/random/{count}',
            '/search/{query}',
            '/exact/{query}'
        ]
    }


@app.get("/random")
async def random():
    name = db.get_random()
    
    return name

@app.get("/random/{count}")
async def randoms(count: int):
    names = db.get_randoms(count)
    
    return names

@app.get("/search/{query}")
async def search(query: str):
    names = db.search(query)

    return names

@app.get("/exact/{query}")
async def exact(query: str):
    name = db.exact(query)

    return name
