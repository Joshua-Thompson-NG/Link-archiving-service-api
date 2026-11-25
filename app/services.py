"""
Business Logic
"""
from datetime import datetime
from pathlib import Path
from uuid import uuid4

from fastapi import HTTPException
from playwright.async_api import Error, async_playwright
from sqlalchemy.orm import Session

from app.models import Snapshot
from app.schemas import SnapshotCreate

SNAPSHOT = Path("snapshot")
SNAPSHOT.mkdir(exist_ok=True)

async def create_snapshot(session: Session, payload: SnapshotCreate):
    snapshot_id = uuid4().hex
    path = SNAPSHOT / f"{snapshot_id}.png"

    async with async_playwright() as p:
        browser = await p.chromium.launch()
        try:
            page = await browser.new_page()
            await page.goto(str(payload.url), timeout=10000,
                            wait_until="domcontentloaded")
            await page.screenshot(path=str(path), full_page=True)
        except Error as e:
            raise HTTPException(  # noqa: B904
                status_code=400,
                detail=f"Failed to capture snapshot from URL: {e.message}")
        finally:
            await browser.close()



    snapshot_db = Snapshot(id=snapshot_id,
                           original_url=str(payload.url),
                           file_path=str(path),
                           )
    session.add(snapshot_db)
    session.commit()
    session.refresh(snapshot_db)
    return snapshot_db


