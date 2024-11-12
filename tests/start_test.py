import pytest
from httpx import AsyncClient
from httpx._transports.asgi import ASGITransport  # For simulating requests to the ASGI app
from app.main import app  # Update 'app.main' as necessary to point to your ASGI app

@pytest.mark.asyncio
async def test_generate_qr_success():
    test_data = {
        "url": "https://github.com/saisrinivas194/is601homework8",
        "fill_color": "black",
        "back_color": "white",
        "size": 10
    }
    # Use ASGITransport explicitly
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        response = await ac.post("/generate_qr/", json=test_data)
    assert response.status_code == 200
    response_data = response.json()
    assert 'message' in response_data
    assert response_data['message'] == "QR code generated successfully"

@pytest.mark.asyncio
async def test_generate_qr_invalid_url():
    test_data = {"url": "not-a-valid-url"}
    # Use ASGITransport explicitly
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        response = await ac.post("/generate_qr/", json=test_data)
    assert response.status_code == 422
