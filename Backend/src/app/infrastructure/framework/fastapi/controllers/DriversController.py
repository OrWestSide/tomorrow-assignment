import random
from typing import List

from fastapi import APIRouter
from starlette import status

from app.application.use_cases.GetDriversUseCase import GetDriversUseCase
from app.infrastructure.framework.fastapi.responses.Driver import \
    Driver
from app.infrastructure.framework.sqlalchemy.operations import SessionLocal
from app.infrastructure.repositories.DriversRepository import DriversRepository

router = APIRouter()


@router.get("",
            summary="Get drivers",
            operation_id="getDrivers",
            description="Get all available drives",
            response_model=List[Driver],
            status_code=status.HTTP_200_OK,
            responses={
                200: {"model": List[Driver]}
            })
def get_drivers() -> List[Driver]:
    driver_repo = DriversRepository(SessionLocal())

    uc = GetDriversUseCase(driver_repo)
    drivers = uc.handle()

    return [
        Driver(**driver.dict()) for driver in drivers
    ]


@router.get("/random",
            summary="Get random driver",
            operation_id="getRandomDriver",
            description="Get a random drives",
            response_model=Driver,
            status_code=status.HTTP_200_OK,
            responses={
                200: {"model": Driver}
            })
def get_drivers() -> Driver:
    driver_repo = DriversRepository(SessionLocal())

    uc = GetDriversUseCase(driver_repo)
    drivers = uc.handle()

    return Driver(**random.choice(drivers).dict())
