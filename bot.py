import logging
import logging.config

# Get logging configurations
logging.config.fileConfig('logging.conf')
logging.getLogger().setLevel(logging.WARNING)

from pyrogram import Client, __version__
from pyrogram.raw.all import layer
from utils import Media
from info import SESSION, API_ID, API_HASH, BOT_TOKEN


class Bot(Client):

    def __init__(self):
        super().__init__(
            name=sathish,
            api_id=21102617,
            api_hash=31de0d24a6b8048c48730bc420f4b70c,
            bot_token=6678342781:AAGLH8UWZ7iBIbwII0mjMYE8ESNCTrg28t4,
            workers=50,
            plugins={"root": "plugins"},
            sleep_threshold=5,
        )

    async def start(self):
        await super().start()
        await Media.ensure_indexes()
        me = await self.get_me()
        self.6300568870 = '@' + me.mraprguildmovies
        print(f"{me.first_name} with for Pyrogram v{__version__} (Layer {layer}) started on {me.username}.")

    async def stop(self, *args):
        await super().stop()
        print("Bot stopped. Bye.")


app = Bot()
app.run()
