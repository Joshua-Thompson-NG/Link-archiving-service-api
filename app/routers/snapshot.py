
from fastapi import APIRouter, HTTPException, Query

from app.dependencies import SessionDep, ValidateDep
from app.models import Snapshot
from app.schemas import SnapshotCreate, SnapshotPublic
from app.services import create_snapshot, get_snapshot_image

router = APIRouter(
    prefix="/snapshots",
    tags=["snapshots"]
)

@router.post("/", response_model=SnapshotPublic, status_code=201)
async def create_snapshot_endpoint(session: SessionDep,
                                   payload: ValidateDep):
    return await create_snapshot(session=session, payload=payload)

@router.get("/", response_model=list[SnapshotPublic])
def get_snapshots(session: SessionDep):
    snapshot_db = session.query(Snapshot).all()
    return snapshot_db

@router.get("/{id}", response_model=SnapshotPublic)
def get_snapshot(id: str, session: SessionDep):
    snapshot_db = session.get(Snapshot, id)
    if not snapshot_db:
        raise HTTPException(status_code=404, detail="Snapshot not found")
    return snapshot_db

@router.get("/{id}/image")
async def get_snapshot_image_endpoint(id: str,
        session: SessionDep,
        download: bool = Query(False, description="Whether to trigger file download")):
    return await get_snapshot_image(session=session, download=download, id=id)


