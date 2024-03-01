from app.domain.interface.ithird_party_service import IThirdPartyService
import httpx


class ThirdPartyService(IThirdPartyService):

    def __init__(self, base_url: str):
        self.base_url = base_url

    async def get_data(self, endpoint: str):
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{self.base_url}{endpoint}")
            response.raise_for_status()
            return response.json()
