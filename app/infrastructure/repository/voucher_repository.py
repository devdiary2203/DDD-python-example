from app.domain.interface.ivoucher_repository import IVoucherRepository
from app.domain.entity.voucher import Voucher


class VoucherRepository(IVoucherRepository):

    def save(self, voucher: Voucher):
        ...

    def retrieve(self, voucher_id: int):
        ...

