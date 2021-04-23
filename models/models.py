from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Timeline(Base):
    __tablename__ = 'Timeline'

    id =  Column(Integer, index=True, primary_key=True)
    datetime = Column(DateTime)
    title = Column(String)
    timeline_type = Column(Integer)
    event_id = Column(Integer,ForeignKey('Event.id'))
    event = relationship('Event',back_populates='timeline')

class Event(Base):
    __tablename__ = 'Event'

    id = Column(Integer, index=True, primary_key=True)
    datetime_id = Column(Integer,ForeignKey('Date.id'))
    title = Column(String)
    title_img = Column(String)
    location = Column(String)
    datetime = relationship('Date',back_populates='event')
    timeline = relationship('Timeline',back_populates='event')
    tags = relationship('TagMapper',back_populates='event')
    contents = relationship('Content',back_populates='event')

class Date(Base):
    __tablename__ = 'Date'
    id = Column(Integer, index=True, primary_key=True)
    datetime = Column(DateTime)
    event = relationship('Event',back_populates='datetime')

class Tag(Base):
    __tablename__ = 'Tag'

    id = Column(Integer, index=True, primary_key=True)
    name = Column(String)
    events = relationship('TagMapper',back_populates='tag')

class User(Base):
    __tablename__ = 'User'
    
    id = Column(Integer, index=True, primary_key=True)
    username = Column(String)
    email = Column(String)
    passwordHash = Column(String)

class TagMapper(Base):
    __tablename__ = 'TagMapper'

    id = Column(Integer, index=True, primary_key=True)
    event_id = Column(Integer, ForeignKey('Event.id'))
    event = relationship('Event',back_populates='tags')
    tag_id = Column(Integer, ForeignKey('Tag.id'))
    tag = relationship('Tag',back_populates='events')

class Content(Base):
    __tablename__ = 'Content'

    id = Column(Integer, index=True, primary_key=True)
    event_id = Column(Integer, ForeignKey('Event.id'))
    content_type = Column(Integer)
    label = Column(String)
    content = Column(String) 
    event = relationship('Event',back_populates='contents')
