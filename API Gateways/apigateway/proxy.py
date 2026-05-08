import httpx
from fastapi import Request, Response

async def proxy_request(request: Request, target_url: str):
    async with httpx.AsyncClient() as client:
        response = await client.request(
            method=request.method,
            url=target_url,
            headers=request.headers.raw,
            content=await request.body(),
            params=request.query_params
        )
    return Response(
        content=response.content,
        status_code=response.status_code,
        headers=response.headers
        )