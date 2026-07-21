from fastapi import APIRouter
from backend.services.vehicle_service import VehicleService

router = APIRouter(
    prefix="/vehicles",
    tags=["Vehicles"]
)

vehicle_service = VehicleService()


@router.get("/")
def get_all_vehicles():
    return vehicle_service.get_all_vehicles()