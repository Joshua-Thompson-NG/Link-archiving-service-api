from datetime import datetime

from pydantic import BaseModel, ConfigDict, HttpUrl


class SnapshotBase(BaseModel):
    pass

class SnapshotCreate(SnapshotBase):
    url: HttpUrl

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "url": "https://example.com/",
            }
        }
    )

class SnapshotPublic(SnapshotBase):
    id: str
    original_url: str
    file_path: str
    timestamp: datetime

    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            "example": {
                "id": 1,
                "original_url": "https://example.com/",
                "file_path": "/path/to/file",
                "timestamp": "2026-11-25T15:30:00Z",
            }
        }
    )

