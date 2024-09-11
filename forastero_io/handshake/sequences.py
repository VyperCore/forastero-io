# SPDX-License-Identifier: MIT
# Copyright (c) 2023-2024 Vypercore. All Rights Reserved

# Common sequences used by testcases in stream
import forastero
from forastero.driver import DriverEvent
from forastero.monitor import MonitorEvent
from forastero.sequence import SeqContext, SeqProxy

from .requestor import HandshakeRequestMonitor
from .responder import HandshakeResponderDriver
from .transaction import HandshakeAck


@forastero.sequence(auto_lock=True)
@forastero.requires("req_mon", HandshakeRequestMonitor)
@forastero.requires("ack_drv", HandshakeResponderDriver)
async def handshake_ack_seq(
    ctx: SeqContext,
    req_mon: SeqProxy[HandshakeRequestMonitor],
    ack_drv: SeqProxy[HandshakeResponderDriver],
    delay_range: tuple[int, int] = (1, 1),
) -> None:
    min_delay, max_delay = min(delay_range), max(delay_range)
    while True:
        await req_mon.wait_for(MonitorEvent.CAPTURE)
        await ack_drv.enqueue(
            HandshakeAck(ack=True, delay=ctx.random.randint(min_delay, max_delay)),
            wait_for=DriverEvent.POST_DRIVE,
        ).wait()
