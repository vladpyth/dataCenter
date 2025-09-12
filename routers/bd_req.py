from fastapi import APIRouter, HTTPException, Query, Depends

from routers.schems import pcPost, toolPost
#from apps.products.service import ProductService

#from .models import CheckoutOrderRequest
from sqlalchemy.ext.asyncio import AsyncSession
from routers.bd_servic import AddService, DellService
# from core.models import Profile
# from core.security import get_async_db, get_current_user,get_current_user_prod

router = APIRouter(prefix="/add-data", tags=["data"])
router_del = APIRouter(prefix="/del-data", tags=["del"])

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
    

@router.post("/rooms", summary="добавить кабинет")
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
    

@router.post("/tools", summary="добавить компанент")
async def add_product(new_tool: toolPost):
    
    try:

        tool_id = await AddService.add_tool(new_tool)
        if tool_id is not None:
            return {
                "status": "success",
                "message": "компанент успешно добавлен",
                "room_id": tool_id,
            }

    except Exception as e:

        raise HTTPException(
            status_code=500, detail=f"Ошибка при добавлении продукта: {str(e)}"
        )
    
@router_del.delete("/pc", summary="удалить pc")
async def add_product(id_pc: int): 
    try:
        pc_id = await DellService.del_pc(id_pc)
        if pc_id is not None:
            return {
                "status": "success",
                "message": "пк успешно удален",
                "room_id": pc_id,
            }
    except Exception as e:
         raise HTTPException(
            status_code=500, detail=f"Ошибка при добавлении продукта: {str(e)}"
        )
