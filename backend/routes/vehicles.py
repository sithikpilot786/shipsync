from fastapi import APIRouter, HTTPException
from backend.models.vehicle import Vehicle
from backend.schemas.vehicle_schema import VehicleSchema
from backend.services.vehicle_service import VehicleService

router = APIRouter(
    prefix="/vehicles",
    tags=["Vehicles"]
)

vehicle_service = VehicleService()


@router.get("/")
def get_all_vehicles():
    return vehicle_service.get_all_vehicles()


@router.get("/{vehicle_id}")
def get_vehicle(vehicle_id: int):
    vehicle = vehicle_service.get_vehicle_by_id(vehicle_id)

    if vehicle is None:
        raise HTTPException(
            status_code=404,
            detail="Vehicle not found"
        )

    return vehicle


@router.post("/")
def add_vehicle(vehicle: VehicleSchema):
    new_vehicle = Vehicle(
        vehicle_id=vehicle.vehicle_id,
        driver_name=vehicle.driver_name,
        vehicle_type=vehicle.vehicle_type,
        capacity=vehicle.capacity,
        status=vehicle.status,
        latitude=vehicle.latitude,
        longitude=vehicle.longitude,
    )

    return vehicle_service.add_vehicle(new_vehicle)


@router.put("/{vehicle_id}")
def update_vehicle(vehicle_id: int, vehicle: VehicleSchema):
    updated_vehicle = Vehicle(
        vehicle_id=vehicle_id,
        driver_name=vehicle.driver_name,
        vehicle_type=vehicle.vehicle_type,
        capacity=vehicle.capacity,
        status=vehicle.status,
        latitude=vehicle.latitude,
        longitude=vehicle.longitude,
    )

    result = vehicle_service.update_vehicle(vehicle_id, updated_vehicle)

    if result is None:
        raise HTTPException(
            status_code=404,
            detail="Vehicle not found"
        )

    return result

@router.delete("/{vehicle_id}")
def delete_vehicle(vehicle_id: int):
    result = vehicle_service.delete_vehicle(vehicle_id)

    if result is None:
        raise HTTPException(
            status_code=404,
            detail="Vehicle not found"
        )

    return {
        "message": "Vehicle deleted successfully",
        "deleted_vehicle": result
    }