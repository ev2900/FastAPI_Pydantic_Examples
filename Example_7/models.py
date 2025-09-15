from datetime import date
from enum import Enum
from pydantic import BaseModel, field_validator
from sqlmodel import SQLModel, Field, Relationship

# Genre choice controls
class GenreURLChoices(Enum):
    ROCK = 'rock'
    ELECTRONIC = 'electronic'
    METAL = 'metal'
    HIP_HOP = 'hip-hop' 

class GenreChoices(Enum):
    ROCK = 'Rock'
    ELECTRONIC = 'Electronic'
    METAL = 'Metal'
    HIP_HOP = 'Hip-Hop'

#
# Data model
#

# Album
class AlbumBase(SQLModel):
    title: str
    release_date: date
    band_id: int = Field(foreign_key = "band.id")

class Album(AlbumBase, table = True):
    id: int = Field(default = None, primary_key = True)
    band: "Band" = Relationship(back_populates="albums")

# Band
class BandBase(SQLModel):
    name: str
    genre: GenreChoices

class BandCreate(BandBase):
    albums: list[AlbumBase] | None = None # default to an empty list []

class Band(BandBase, table = True):
    id: int = Field(default = None, primary_key = True)
    albums: list[Album] = Relationship(back_populates = "band")