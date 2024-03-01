from abc import ABC, abstractmethod


class IThirdPartyService(ABC):

    @abstractmethod
    async def get_data(self, endpoint: str):
        ...
