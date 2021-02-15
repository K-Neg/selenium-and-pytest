from fastapi import FastAPI
from .routes.gallon import gallon_routes
#from .login import rotlog
from fastapi.middleware.cors import CORSMiddleware


api = FastAPI()

origins = [  
  "http://localhost:5000",
]

api.add_middleware(
  CORSMiddleware,
  allow_origins=origins,
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)

api.include_router(gallon_routes)

@api.on_event("startup")
async def startup_event():
  pass