from pydantic import BaseModel
from typing import List, Optional

class pcPost(BaseModel):
    room_id: int
    type_os: str
    version_os: str
    core: int
    cpu:int
    gpu: int
    ram: int
    name_pc: str
    inventory_number: str
    
# class UserOrderResponse(BaseModel):
#     id_order_proc: int
#     total_price: int
#     count: int
#     status: str
#     comment: Optional[str]
#     shipping_cost: int
#     adress: Optional[str]
#     products: List[ProductInOrder]

#     class Config:
#         from_attributes = True

