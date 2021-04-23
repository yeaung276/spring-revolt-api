from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import routers.events as Events
import routers.timelines as Timelines
import routers.tags as Tags
import routers.users as Users
import routers.date as Dates
import routers.content as Contents
from database import Base, engine
from models import models

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(Events.eventRouter)
app.include_router(Timelines.timelineRouter)
app.include_router(Tags.tagRouter)
app.include_router(Users.userRouter)
app.include_router(Dates.dateRouter)
app.include_router(Contents.contentRouter)

@app.get('/')
def hello():
    about = 'This api is wirtten for the website to remember the fallen heros who lost their lives during spring revolution myanmar 2021. "What we can do is to remember our heros and our enemyes."'
    return about

