import asyncio
import logging
import math
import sys
import traceback
from collections import defaultdict

#from apps.products.models import AddProdBask, NewProduct

if sys.platform == "win32":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

from fastapi import HTTPException

from sqlalchemy import delete, func, join, select, cast, Numeric, nulls_last, case, and_, exists,update

from core.database import get_async_db
from routers.schems import pcPost, toolPost
from core.models import Computer, Room, AddTool
# from apps.user_actions.models import UserAction
session_fabrik = get_async_db


class AddService:


    
    @staticmethod
    async def add_pc(new_pc: pcPost):
        try:
            async for session in session_fabrik():
                db_pc = Computer(
                    room_id = new_pc.room_id,
                    type_os = new_pc.type_os,
                    version_os = new_pc.version_os,
                    core = new_pc.core,
                    cpu = new_pc.cpu ,
                    gpu= new_pc.gpu,
                    ram= new_pc.ram,
                    name_pc= new_pc.name_pc,
                    inventory_number= new_pc.inventory_number,
                )
                session.add(db_pc)
                await session.flush()
                await session.commit()

                return db_pc.id_pc

        except Exception as e:
            logging.error(f"adding pc: {traceback.format_exc()}")

            raise HTTPException(
                status_code=500, detail=f"Ошибка при добавлении пк: {str(e)}"
            )

    @staticmethod
    async def add_room(name_room: str):
        try:
            async for session in session_fabrik():
                db_room = Room(
                    name = name_room,
                )
                session.add(db_room)
                await session.flush()
                await session.commit()

                return db_room.id_room

        except Exception as e:
            logging.error(f"adding room: {traceback.format_exc()}")

            raise HTTPException(
                status_code=500, detail=f"Ошибка при добавлении кабинета: {str(e)}"
            )
        
    @staticmethod
    async def add_tool(new_tool: toolPost):
        try:
            async for session in session_fabrik():
                db_tool= AddTool(
                    room_id= new_tool.room_id,
                    type_tool = new_tool.type_tool,
                    name = new_tool.name,
                    inventory_number = new_tool.inventory_number,
                )
                session.add(db_tool)
                await session.flush()
                await session.commit()

                return db_tool.id_tool

        except Exception as e:
            logging.error(f"adding room: {traceback.format_exc()}")

            raise HTTPException(
                status_code=500, detail=f"Ошибка при добавлении кабинета: {str(e)}"
            )
        
class DellService:

    
    @staticmethod
    async def del_pc(id_pc: int):
        try:
            async for session in session_fabrik():
                
                check_query = select(Computer).where(Computer.id_pc == id_pc)
                result = await session.execute(check_query)
                db_pc = result.scalar_one_or_none()

                if not db_pc:
                    raise HTTPException(
                        status_code=404, detail=f"Продукт с ID {id_pc} не найден"
                    )

                await session.delete(db_pc)
                await session.commit()

                return id_pc

        except Exception as e:
            logging.error(f"del pc: {traceback.format_exc()}")

            raise HTTPException(
                status_code=500, detail=f"Ошибка при удалении пк: {str(e)}"
            )

    @staticmethod
    async def add_room(name_room: str):
        try:
            async for session in session_fabrik():
                db_room = Room(
                    name = name_room,
                )
                session.add(db_room)
                await session.flush()
                await session.commit()

                return db_room.id_room

        except Exception as e:
            logging.error(f"adding room: {traceback.format_exc()}")

            raise HTTPException(
                status_code=500, detail=f"Ошибка при добавлении кабинета: {str(e)}"
            )
        
    @staticmethod
    async def add_tool(new_tool: toolPost):
        try:
            async for session in session_fabrik():
                db_tool= AddTool(
                    room_id= new_tool.room_id,
                    type_tool = new_tool.type_tool,
                    name = new_tool.name,
                    inventory_number = new_tool.inventory_number,
                )
                session.add(db_tool)
                await session.flush()
                await session.commit()

                return db_tool.id_tool

        except Exception as e:
            logging.error(f"adding room: {traceback.format_exc()}")

            raise HTTPException(
                status_code=500, detail=f"Ошибка при добавлении кабинета: {str(e)}"
            )



