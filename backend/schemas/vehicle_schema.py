from pydantic import BaseModel


class VehicleSchema(BaseModel):
    vehicle_id: int
    driver_name: str
    vehicle_type: str
    capacity: int
    status: str
    latitude: float
    longitude: float