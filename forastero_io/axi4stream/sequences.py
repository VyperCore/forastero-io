# SPDX-License-Identifier: MIT
# Copyright (c) 2023-2024 Vypercore. All Rights Reserved

import forastero
from forastero.driver import DriverEvent
from forastero.sequence import SeqContext, SeqProxy

from .target import AXI4StreamTarget
from .transaction import AXI4StreamBackpressure


@forastero.sequence()
@forastero.requires("driver", AXI4StreamTarget)
async def axi4stream_backpressure_seq(
    ctx: SeqContext, driver: SeqProxy[AXI4StreamTarget]
):
    while True:
        async with ctx.lock(driver):
            driver.enqueue(
                AXI4StreamBackpressure(
                    ready=ctx.random.choice((True, False)),
                    cycles=ctx.random.randint(1, 10),
                )
            )
        await driver.wait_for(DriverEvent.PRE_DRIVE)
