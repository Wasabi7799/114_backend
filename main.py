# from http.server import HTTPServer, SimpleHTTPRequestHandler
# import threading
from typing import Annotated, List, Union
from fastapi import FastAPI, Path, Body, Cookie, Form
from pydantic import BaseModel, Field

class Item(BaseModel):
    name:str
    description:str | None = Field(
        default = None, title = "The description of the item", max_length = 300
    )
    price: float = Field(gt = 0, description = "The price must be greater than zero")
    tax: Union[float, None] = None
    tags: List[str] = []

app = FastAPI()

@app.post("/login")
async def login(
    username: Annotated[str, Form()],
    password: Annotated[str, Form()]
):
    return {"username": username}

@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}

@app.get("/")
async def root():
    return{"message": "Hello World!"}

'''
@app.get("/tiems/")
async def read_item(skip: int = 0,limit: int = 10):
    return fake_items_db[skip: skip + limit]


fake_items_db = [
    {"item_name": "Foo"},
    {"item_name": "Bar"},
    {"item_name": "Baz"}
]
'''

@app.get("/items/")
async def read_items(ads_id: Annotated[str | None, Cookie()]):
    return {"ads_id": ads_id}

@app.post("/items/")
async def create_item(item: Item):
    item_dict = item.model_dump() #dict()
    if item_dict is not None:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax" : price_with_tax})
    return item_dict

'''
@app.put("/items/{items_id}")
async def update_item(
    item_id: Annotated[int, Path(title = "The ID of the item to get", ge = 0, le = 1000)], 
    item: Item, 
    q: str | None = None
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q}) 
    if item:
        results.update({"item": item})
    return results
'''

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Annotated[Item, Body(embed = True)]):
    results = {"item_id": item_id, "item": item}
    return results



#------------------server test
# class MyHandler(SimpleHTTPRequestHandler):
#     def __init__(self, *args, **kwargs):
#         # 指定服務的目錄為 'public'
#         super().__init__(*args, directory='public', **kwargs)
#     def do_GET(self):
#         # 如果請求的路徑是根目錄 '/'
#         if self.path == '/':
#             # 將路徑變更為 'mainpage.html'
#             self.path = 'main_page.html'
        
#         # 執行父類別的 GET 方法來處理請求
#         return super().do_GET()

# # Define the server address and port
# HOST = '0.0.0.0'
# PORT = 8000

# # Create a handler to manage requests
# #Handler = SimpleHTTPRequestHandler

# # Create the server object
# httpd = HTTPServer((HOST, PORT), MyHandler)

# # Function to run the server
# def run_server():
#     print(f"Serving HTTP on {HOST} port {PORT} (http://localhost:{PORT}/) ...")
#     print("Type 'stop' to shut down the server...")
#     httpd.serve_forever()

# # Create and start the server in a separate thread
# server_thread = threading.Thread(target=run_server)
# server_thread.daemon = True  # This allows the main program to exit even if the thread is still running
# server_thread.start()

# # Main thread waits for user input
# try:
#     while True:
#         command = input()
#         if command.lower() == 'stop':
#             print("Shutting down the server...")
#             httpd.shutdown()  # This method shuts down the server
#             break
#         else:
#             print("unknown command...")
# except KeyboardInterrupt:
#     print("Shutting down the server...")
#     httpd.shutdown()