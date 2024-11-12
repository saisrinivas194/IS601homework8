from pydantic import BaseModel, HttpUrl

class QRCodeRequest(BaseModel):
    url: HttpUrl
    fill_color: str = "black"
    back_color: str = "white"
    size: int = 10
