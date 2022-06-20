from fastapi import FastAPI

import api
import price_logic
import schedule_price

app = FastAPI()
app.include_router(api.router)

price_logic.update_price()
schedule_price.run_continuously()
