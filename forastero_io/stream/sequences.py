# SPDX-License-Identifier: MIT
# Copyright (c) 2023-2024 Vypercore. All Rights Reserved

import forastero
from forastero.driver import DriverEvent
from forastero.sequence import SeqContext, SeqProxy

from .responder import StreamResponderDriver
from .transaction import StreamBackpressure


@forastero.sequence()
@forastero.requires("driver", StreamResponderDriver)
async def stream_backpressure_seq(
    ctx: SeqContext, driver: SeqProxy[StreamResponderDriver]
):
    while True:
        async with ctx.lock(driver):
            driver.enqueue(
                StreamBackpressure(
                    ready=ctx.random.choice((True, False)),
                    cycles=ctx.random.randint(1, 10),
                )
            )
        await driver.wait_for(DriverEvent.PRE_DRIVE)
