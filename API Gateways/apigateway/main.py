from fastapi import FastAPI,Request
from proxy import proxy_request

app = FastAPI(title="API Gateway")

@app.api_route("/products/{path:path}", methods=["GET", "POST", "PUT", "DELETE"])
async def product_gateway(path: str, request: Request):
    target_url = f"http://localhost:8001/api/products/{path}"
    return await proxy_request(request, target_url)

@app.api_route("/orders/{path:path}", methods=["GET", "POST", "PUT", "DELETE"])
async def order_gateway(path: str, request: Request):
    target_url = f"http://localhost:8002/api/orders/{path}"
    return await proxy_request(request, target_url)