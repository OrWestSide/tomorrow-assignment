from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.infrastructure.framework.fastapi.controllers.DriversController \
    import router as drivers_router
from app.infrastructure.framework.fastapi.controllers.UsersController \
    import router as users_router
from app.infrastructure.framework.fastapi.controllers.SurveysController \
    import router as surveys_router
from app.infrastructure.framework.fastapi.controllers.FeedbackController \
    import router as feedback_router
from app.infrastructure.framework.sqlalchemy import dao
from app.infrastructure.framework.sqlalchemy.operations import engine

dao.Base.metadata.create_all(bind=engine)
app = FastAPI(title='tomorrow-challenge')

app.include_router(drivers_router, prefix="/drivers", tags=["Drivers"])
app.include_router(users_router, prefix="/users", tags=["Users"])
app.include_router(surveys_router, prefix="/surveys", tags=["Surveys"])
app.include_router(feedback_router, prefix="/feedback", tags=["Feedback"])

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
