# class Car:
#     def __init__(self, brand, color):
#         self.brand = brand
#         self.color = color

#     def display(self):
#         print(self.brand, self.color)


# car1 = Car("BMW", "Black")
# car2 = Car("Toyota", "White")

# car1.display()
# car2.display()


from typing import Optional
from pydantic import BaseModel
from fastapi import FastAPI, Body
from fastapi.responses import FileResponse

app = FastAPI()

# --- GET Routes ---

@app.get("/")
def read_root():
    return {"message": "Hello-World"}

@app.get("/new-home")
def read_new_home():
    return FileResponse("index.html")

@app.get("/users")
def read_users():
    return {"message": "This is user page"}

@app.get("/users/{id}")
def read_user_by_id(id: int):
    return {"message": f"This is user {id} page"}

@app.get("/users/{id}/contact")
def read_user_contact(id: int):
    return {"message": f"This is user {id} contact page."}

@app.get("/contact")
def read_contact():
    return FileResponse("contact.html")

@app.get("/blog")
def get_blogs(
    limit: int = 5,
    published: bool = True,
    num_comments: Optional[int] = None,
    sort: Optional[bool] = None,
):
    return {
        "Type": "blog",
        "limit": limit,
        "Published": published,
        "no. Of comments": num_comments,
    }

@app.get("/blog/{id}")
def get_blog_by_id(id: int):
    return {"Type": "blog", "id": id}


class Blog(BaseModel):
  title: str
  body: str
  id: int
  published: Optional[bool] = True


# --- POST Route (Without Class / Pydantic Model) ---
# Body(...) forces FastAPI to expect these fields in the JSON Request Body 
# instead of URL Query Parameters.

'''
@app.post("/blog")
def create_blog(
    title: str = Body(...),
    body: str = Body(...),
    id: int = Body(...),
    published: bool = Body(True),
):
    return {
        "message": "Saved!",
        "blog": {
            "title": title,
            "body": body,
            "id": id,
            "published": published,
        },
    }

    '''

@app.post("/blog")
def create_blog(new_blog: Blog):
    return {

        "message": "Blog successfully created!",
        "blog-id:": new_blog.id,
        "Title_received": new_blog.title
    }
