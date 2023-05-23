import asyncio
import json
from aio_pika import Message, connect_robust
from aio_pika.abc import (
    AbstractChannel, AbstractConnection
)


class RequestClient:
    connection: AbstractConnection
    channel: AbstractChannel
    loop: asyncio.AbstractEventLoop

    async def connect(self):
        self.connection = await connect_robust(
            "amqp://guest:guest@localhost/"
        )
        self.channel = await self.connection.channel()
        return self

    async def call_to_project(self, n: dict):

        await self.channel.default_exchange.publish(
            Message(
                body=json.dumps(n).encode('utf-8'),
                content_type="application/json",
            ),
            routing_key="test_queue",
        )
