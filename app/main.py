from fastapi import FastAPI

from app.application.voucher_service import VoucherService
from app.domain.entity.voucher import Voucher
from app.domain.model.money import Money
from app.infrastructure.repository.voucher_repository import VoucherRepository
from app.infrastructure.service.third_party_service import ThirdPartyService

import uvicorn

app = FastAPI()

# Dependency injection
voucher_repo = VoucherRepository()
third_party_service = ThirdPartyService(base_url="localhost")
voucher_service = VoucherService(voucher_repo, third_party_service)


@app.post("/voucher")
async def create_voucher(title: str, start_date: str, end_date: str, initial_bid: Money):
    voucher = Voucher(title, start_date, end_date, initial_bid)
    await voucher_service.create_voucher(voucher)
    # save voucher to the repository
    return {"message": "Voucher created successfully!", "voucher": voucher.__dict__}


# Start application using unicorn
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
