from dataclasses import dataclass

@dataclass
class Vehicle:
    vehicle_id: int
    driver_name: str
    vehicle_type: str
    capacity: int
    status: str
    latitude: float
    longitude: float