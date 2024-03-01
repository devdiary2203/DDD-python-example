from abc import ABC, abstractmethod
from app.domain.entity.voucher import Voucher


class IVoucherRepository(ABC):

    @abstractmethod
    def save(self, voucher: Voucher):
        ...

    @abstractmethod
    def retrieve(self, voucher_id: int):
        ...
