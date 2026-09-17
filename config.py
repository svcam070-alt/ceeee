import os

BOT_TOKEN = os.getenv("BOT_TOKEN", "8725081317:AAGn9G9RD0LU73sQry1RONB0eqJ7J01tejY")
ADMIN_ID = int(os.getenv("ADMIN_ID", "2010030869"))
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://sccc_user:rWG9uB88TCqg875P6tY4SZ58MmAZqRru@dpg-dalr50dbedkc7381e5k0-a.virginia-postgres.render.com/sccc")

# Telethon uchun
API_ID = int(os.getenv("API_ID", "38486800"))
API_HASH = os.getenv("API_HASH", "c5fc7e4d2190b89e5ce8ea01c0369f09")
