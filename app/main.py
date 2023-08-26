from fastapi import FastAPI
import random
import model
from dbconfig import engine
import router

model.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get('/')
async def root():
    return "Welcome Home"

app.include_router(router.router, prefix="/book", tags=["book"])
# return {"Hello": "World", "data": "Just some data", "version": 2}


@app.get('/home')
async def get_home():
    return {"home": "This is the home page"}


@app.get('/random')
async def get_random():
    rn: int = random.randint(0, 50)
    return {"number": rn}


@app.get('/random/{limit}')
async def get_random(limit: int):
    rn: int = random.randint(0, limit)
    return {"number": rn}


# Ignore the below for now this is a multiline comment as well. ---

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
