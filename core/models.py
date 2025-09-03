import datetime
from datetime import datetime as dt
from sqlalchemy import Column, ForeignKey, Integer, String, text, Boolean
from sqlalchemy.orm import Mapped, mapped_column
from core.database import Base
from typing import Optional




class Room(Base):
    __tablename__ = "Room"
    id_room: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))

class AddTool(Base):
    __tablename__ = "AddTool"
    id_tool: Mapped[int] = mapped_column(primary_key=True)
    room_id: Mapped[int] = mapped_column(
        ForeignKey("Room.id_room", ondelete="CASCADE")
    )
    type_tool: Mapped[str] = mapped_column(String(50))
    name: Mapped[str| None] = mapped_column(String(50),nullable=True, default=None)
    inventory_number: Mapped[str] = mapped_column(String(20))

class Monitor(Base):
    __tablename__ = "Monitor"
    id_monitor: Mapped[int] = mapped_column(primary_key=True)
    room_id: Mapped[int] = mapped_column(
        ForeignKey("Room.id_room", ondelete="CASCADE")
    )
    premission: Mapped[str] = mapped_column(String(50))
    refresh_rate: Mapped[int]
    name: Mapped[str| None] = mapped_column(String(50),nullable=True, default=None)
    inventory_number: Mapped[str] = mapped_column(String(20))

class Computer(Base):
    __tablename__ = "Computer"
    id_pc: Mapped[int] = mapped_column(primary_key=True)
    room_id: Mapped[int] = mapped_column(
        ForeignKey("Room.id_room", ondelete="CASCADE")
    )
    type_os: Mapped[str] = mapped_column(String(25))
    version_os: Mapped[str] = mapped_column(String(25))
    core: Mapped[int]
    cpu: Mapped[int]
    gpu: Mapped[int]
    ram: Mapped[int]
    name_pc: Mapped[str] = mapped_column(String(50))
    inventory_number: Mapped[str] = mapped_column(String(20))

class Categories(Base):
    __tablename__ = "Categories"
    id_cat: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))

class DistributionPoint(Base):
    __tablename__ = "DistributionPoint"
    id_dis_point: Mapped[int] = mapped_column(primary_key=True)
    cat_id: Mapped[int] = mapped_column(
        ForeignKey("Categories.id_cat", ondelete="CASCADE")
    )
    obj_id: Mapped[int]

class Magszine(Base):
    __tablename__ = "Magszine"
    id_mag: Mapped[int] = mapped_column(primary_key=True)
    date_created: Mapped[datetime.datetime] = mapped_column(
        server_default=text("TIMEZONE('utc', now())")
    )
    date_update: Mapped[datetime.datetime] = mapped_column(
        server_default=text("TIMEZONE('utc', now())"),
        onupdate=datetime.datetime.utcnow,
    )
    dis_point_id: Mapped[int] = mapped_column(
        ForeignKey("DistributionPoint.id_dis_point", ondelete="CASCADE")
    )
    id_room_new: Mapped[int] = mapped_column(
        ForeignKey("Room.id_room", ondelete="CASCADE")
    )
    id_room_old: Mapped[int]
    comments: Mapped[str| None] = mapped_column(String(20), nullable=True, default=None)


# class Token(Base):
#     __tablename__ = "user_tokens"
#     __table_args__ = {"extend_existing": True}

#     id_token: Mapped[int] = mapped_column(primary_key=True)
#     id_profile: Mapped[int] = mapped_column(
#         ForeignKey("Profile.id_profile", ondelete="CASCADE")
#     )
#     access_token: Mapped[str] = mapped_column(String(512), unique=True)
#     refresh_token: Mapped[str] = mapped_column(String(512), unique=True)
#     expires_at: Mapped[datetime.datetime]
#     created_at: Mapped[datetime.datetime] = mapped_column(
#         server_default=text("TIMEZONE('utc', now())")
#     )








