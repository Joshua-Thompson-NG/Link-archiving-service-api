from fastapi import APIRouter, HTTPException

from app.dependencies import SessionDep
from app.models import Snapshot
from app.schemas import SnapshotCreate, SnapshotPublic
from app.services import create_snapshot

router = APIRouter(
    prefix="/snapshots",
    tags=["snapshots"]
)

@router.post("/", response_model=SnapshotPublic, status_code=201)
async def create_snapshot_endpoint(session: SessionDep, payload: SnapshotCreate):
    return await create_snapshot(session=session, payload=payload)

