import asyncio


class BaseHandler(object):
    def __init__(self, bot):
        self._bot = bot

    def on_message(self, message):
        pass

    @property
    def api(self):
        return self._bot.api

    @asyncio.coroutine
    def send_text(self, channel, text):
        yield from self._bot.send_text(channel, text)
