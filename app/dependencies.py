import ipaddress
import socket
from typing import Annotated
from urllib.parse import urlparse

from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.schemas import SnapshotCreate


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def is_safe_ip(hostname: str):
    try:
        addr_info = socket.getaddrinfo(hostname, None)
        for info in addr_info:
            ip_str = info[4][0]
            ip =    ipaddress.ip_address(ip_str)
            # Block loopback
            if (
                ip.is_private
                or ip.is_loopback
                or ip.is_link_local
                or ip.is_multicast
                or ip.is_reserved
            ):
                return False
        return True
    except socket.gaierror:
        return False

async def validate_safe_url(payload: SnapshotCreate):
    parsed = urlparse(str(payload.url))

    if parsed.scheme not in ("http", "https"):
        raise HTTPException(status_code=400, detail="Bad URL")

    if not parsed.hostname or not is_safe_ip(parsed.hostname):
        raise HTTPException(status_code=400, detail="Bad URL")

    return payload
SessionDep = Annotated[Session, Depends(get_db)]
ValidateDep = Annotated[SnapshotCreate, Depends(validate_safe_url)]


