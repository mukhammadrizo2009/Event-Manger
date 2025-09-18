from fastapi import APIRouter , Depends , HTTPException , status
from sqlalchemy.orm import Session
from ..dependencies import get_db
from ..models.orders import Orders
from ..schemas.orders import OrdersOut, OrderCreate, OrderUpdate

router = APIRouter(
    prefix="/orders",
    tags=["Orders"]
)

@router.get("/")
async def get_orderss(db: Session = Depends(get_db)):
    orders = db.query(Orders).all()
    return [OrdersOut.from_orm(order) for order in orders]

@router.post("/", response_model=OrdersOut)
async def create_order(event: OrderCreate, db: Session = Depends(get_db)):
    db_event = Orders(
        name = event.name,
        description = event.description,
        event_type = event.event_type,
        status = event.status,
        start_date = event.start_date,
        end_date = event.end_date,
        address = event.address,
        venue_id = event.venue_id,
        organizer_id = event.organizer_id
    )
    db.add(db_event)
    db.commit()
    db.refresh(db_event)
    
    return Orders.from_orm(db_event)

@router.put("/{event_id}", response_model=OrdersOut)
async def update_event(event_id: int, updated_event: OrderUpdate, db: Session = Depends(get_db)):
    event = db.query(Orders).filter(Orders.id == event_id).first()
    if not event:
           raise HTTPException(
               status_code=status.HTTP_404_NOT_FOUND,
               detail="Event not found"
           ) 
    event.name = update_event.name
    event.description = update_event.description
    event.event_type = update_event.event_type
    event.status = update_event.status
    
    db.commit()
    db.refresh(event)
    return OrdersOut.from_orm(event)

@router.delete("/{event_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_event(event_id: int, db: Session = Depends(get_db)):
    event = db.query(Orders).filter(Orders.id == event_id).first()
    if not event:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Event not found"
        )
        
    db.delete(event)
    db.commit()
    return None