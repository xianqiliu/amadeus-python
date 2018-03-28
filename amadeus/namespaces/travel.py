from amadeus.client.decorator import Decorator
from ._travel.analytics import Analytics


class Travel(Decorator, object):
    def __init__(self, client):
        Decorator.__init__(self, client)
        self.analytics = Analytics(client)
