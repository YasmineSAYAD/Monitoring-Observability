from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session
from typing import List
import datetime

from app.database import get_db
from app.schemas.item import ItemCreate, ItemResponse, ItemUpdate
from app.services.item_service import ItemService
from app.metrics import ( 
    crud_operations_total,
    items_total,
    item_price_distribution,
    http_errors_total
)

router = APIRouter(prefix="/items", tags=["items"])

MAX_ITEMS_PER_PAGE = 1000


@router.get("/", response_model=list[ItemResponse])
def get_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    crud_operations_total.labels(operation="read").inc()
    try:
        return ItemService.get_all(db, skip, limit)
    except Exception:
        http_errors_total.labels(
            route="/items",
            method="GET",
            status="500"
        ).inc()
        raise


@router.get("/{item_id}", response_model=ItemResponse)
def get_item(item_id: int, db: Session = Depends(get_db)):
    crud_operations_total.labels(operation="read").inc()
    try:
        item = ItemService.get_by_id(db, item_id)
        if not item:
            http_errors_total.labels(
                route="/items/{item_id}",
                method="GET",
                status="404"
            ).inc()
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Item with id {item_id} not found",
            )
        return item
    except HTTPException:
        raise
    except Exception:
        http_errors_total.labels(
            route="/items/{item_id}",
            method="GET",
            status="500"
        ).inc()
        raise


@router.post("/", response_model=ItemResponse, status_code=status.HTTP_201_CREATED)
def create_item(item_data, db: Session = Depends(get_db)):
    crud_operations_total.labels(operation="create").inc()
    try:
        item = ItemService.create(db, item_data)
        items_total.inc()  # Gauge : +1
        item_price_distribution.observe(item.price)  # Histogram
        return item
    except Exception:
        http_errors_total.labels(
            route="/items",
            method="POST",
            status="500"
        ).inc()
        raise


@router.put("/{item_id}", response_model=ItemResponse)
def update_item(item_id: int, item_data: ItemUpdate, db: Session = Depends(get_db)):
    crud_operations_total.labels(operation="update").inc()
    try:
        item = ItemService.update(db, item_id, item_data)
        if not item:
            http_errors_total.labels(
                route="/items/{item_id}",
                method="PUT",
                status="404"
            ).inc()
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Item with id {item_id} not found",
            )
        return item
    except HTTPException:
        raise
    except Exception:
        http_errors_total.labels(
            route="/items/{item_id}",
            method="PUT",
            status="500"
        ).inc()
        raise


@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_item(item_id: int, db: Session = Depends(get_db)):
    crud_operations_total.labels(operation="delete").inc()
    try:
        deleted = ItemService.delete(db, item_id)
        if not deleted:
            http_errors_total.labels(
                route="/items/{item_id}",
                method="DELETE",
                status="404"
            ).inc()
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Item with id {item_id} not found",
            )

        items_total.dec()  # Gauge : -1
        return {"status": "deleted"}

    except HTTPException:
        raise

    except Exception:
        http_errors_total.labels(
            route="/items/{item_id}",
            method="DELETE",
            status="500"
        ).inc()
        raise


def _old_helper_function(data):
    """Cette fonction n'est plus utilisée mais n'a pas été supprimée."""
    return data.upper()