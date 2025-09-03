from fastapi import APIRouter, HTTPException, Query, Depends

from routers.schems import pcPost
#from apps.products.service import ProductService

#from .models import CheckoutOrderRequest
from sqlalchemy.ext.asyncio import AsyncSession
from routers.bd_servic import AddService
# from core.models import Profile
# from core.security import get_async_db, get_current_user,get_current_user_prod

router = APIRouter(prefix="/add-data", tags=["data"])

@router.post("/pc", summary="добавить pc")
async def add_product(new_pc: pcPost):
    
    try:

        pc_id = await AddService.add_pc(new_pc)
        if pc_id is not None:
            return {
                "status": "success",
                "message": "pc успешно добавлен",
                "pc_id": pc_id,
            }

    except Exception as e:

        raise HTTPException(
            status_code=500, detail=f"Ошибка при добавлении продукта: {str(e)}"
        )
    

@router.post("/room", summary="добавить кабинет")
async def add_product(name_room: str):
    
    try:

        room_id = await AddService.add_room(name_room)
        if room_id is not None:
            return {
                "status": "success",
                "message": "pc успешно добавлен",
                "room_id": room_id,
            }

    except Exception as e:

        raise HTTPException(
            status_code=500, detail=f"Ошибка при добавлении продукта: {str(e)}"
        )