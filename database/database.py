import motor.motor_asyncio
from config import DB_URL, DB_NAME

client = motor.motor_asyncio.AsyncIOMotorClient(DB_URL)
db = client[DB_NAME]
users_col = db["user_settings"]

async def get_user_settings(user_id):
    user_data = await users_col.find_one({"_id": user_id})
    if not user_data:
        # Default settings if user is new
        default_settings = {
            "_id": user_id,
            "rename_mode": "AUTODETECT",
            "main_thumb": False,
            "quality_thumbs": 0,
            "copy_source_thumb": True,
            "caption": "Not set",
            "format": "[S01] [E{episode}] VIRAL HIT [2160p] [@Unrated_coder] [Multi-Audio]"
        }
        await users_col.insert_one(default_settings)
        return default_settings
    return user_data

async def update_user_setting(user_id, key, value):
    await users_col.update_one({"_id": user_id}, {"$set": {key: value}})

