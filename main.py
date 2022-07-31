from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from config.db import get_db
from models.cars import Car
from schemas.schema_car import Data


app = FastAPI()

@app.get('/')
def root():
    return "{message:'car_details'}"

@app.get("/api/cars")
def display( db: Session = Depends(get_db)):
    return db.query(Car).all()


@app.post('/api/cars')
def insert( obj:Data,db: Session = Depends(get_db)):


     data = db.query(Car).filter(Car.registration_no == obj.registration_no).first()

     if data is not None:
         return "registration_no already found!!!"

    

     data1 = Car(
        registration_no=obj.registration_no,
        car_name=obj.car_name,
        model=obj.model,
        price=obj.price
        )

     db.add(data1)
     db.commit()

     return db.query(Car).all()


@app.put('/api/cars/{registration_no}')
def update(registration_no:str,obj:Data,db: Session = Depends(get_db)):
    data1=db.query(Car).filter(Car.registration_no == registration_no).first()

    if data1 is None:
        return "no details with this registration number"

    data1.car_name=obj.car_name
    data1.price=obj.price

    db.commit()

    return db.query(Car).all()


@app.delete('/api/cars/{registration_no}')
def delete(registration_no: str,db: Session = Depends(get_db)):
    data1 = db.query(Car).filter(Car.registration_no == registration_no).first()

    if data1 is None:
        return "no details with this registration number"

    db.delete(data1)
    db.commit()

    return db.query(Car).all()