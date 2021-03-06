from sqlalchemy import Column, Integer, TIMESTAMP, String, BOOLEAN, ForeignKey
from db_utils import Base as BaseModel
from db_utils import UUID
import datetime
import uuid


class Tracker(BaseModel):
    __tablename__ = 'trackers'
    uuid = Column(UUID, nullable=False, unique=True, primary_key=True)
    name = Column(String, nullable=False)
    owner_id = Column(Integer, nullable=False)
    created_at = Column(TIMESTAMP, nullable=False, default=datetime.datetime.now())


class Request(BaseModel):
    __tablename__ = 'requests'
    uuid = Column(UUID, nullable=False, unique=True, primary_key=True, default=uuid.uuid4())
    ip = Column(String, nullable=False)
    useragent = Column(String, nullable=True)
    from_mask = Column(String, nullable=False)
    mask_owner = Column(String, nullable=False)
    url = Column(String, nullable=True)
    tracker_uuid = Column(UUID, ForeignKey('trackers.uuid'), nullable=False)
    at = Column(TIMESTAMP, nullable=False, default=datetime.datetime.now())


class Notification(BaseModel):
    __tablename__ = 'notifications'
    uuid = Column(UUID, nullable=False, unique=True, primary_key=True, default=uuid.uuid4())
    tracker_uuid = Column(UUID, ForeignKey('trackers.uuid'), nullable=False)
    chat_id = Column(Integer, nullable=False)
    enable = Column(BOOLEAN, default=True)
