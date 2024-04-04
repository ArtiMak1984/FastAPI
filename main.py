from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()
elements = []

class Element(BaseModel):
    id: int
    name: str
    description: str

@app.post("/elements/", response_model=Element)
def create_element(element: Element):
    elements.append(element)
    return element

@app.get("/elements/", response_model=List[Element])
def read_elements():
    return elements

@app.get("/elements/{element_id}", response_model=Element)
def read_element(element_id: int):
    for element in elements:
        if element.id == element_id:
            return element
    return {"error": "Element not found"}

@app.put("/elements/{element_id}", response_model=Element)
def update_element(element_id: int, element: Element):
    for i, e in enumerate(elements):
        if e.id == element_id:
            elements[i] = element
            return element
    return {"error": "Element not found"}

@app.delete("/elements/{element_id}")
def delete_element(element_id: int):
    for i, element in enumerate(elements):
        if element.id == element_id:
            del elements[i]
            return {"message": "Element deleted"}
    return {"error": "Element not found"}