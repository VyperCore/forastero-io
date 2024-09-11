# SPDX-License-Identifier: MIT
# Copyright (c) 2023-2024 Vypercore. All Rights Reserved

# Common sequences used by testcases in mapped

import forastero
from cocotb.triggers import ClockCycles
from forastero.driver import DriverEvent
from forastero.sequence import SeqContext, SeqProxy

from .request import MappedRequestInitiator, MappedRequestResponder
from .response import MappedResponseInitiator, MappedResponseResponder
from .transaction import MappedAccess, MappedBackpressure, MappedRequest, MappedResponse


@forastero.sequence()
@forastero.requires("driver", MappedRequestResponder)
async def mapped_req_backpressure_seq(
    ctx: SeqContext, driver: SeqProxy[MappedRequestResponder]
):
    while True:
        async with ctx.lock(driver):
            driver.enqueue(
                MappedBackpressure(
                    ready=ctx.random.choice((True, False)),
                    cycles=ctx.random.randint(1, 10),
                )
            )
        await driver.wait_for(DriverEvent.PRE_DRIVE)


@forastero.sequence(auto_lock=True)
@forastero.requires("driver", MappedRequestResponder)
async def mapped_req_no_backpressure_seq(
    ctx: SeqContext, driver: SeqProxy[MappedRequestResponder]
):
    driver.enqueue(MappedBackpressure(ready=True, cycles=1))


@forastero.sequence()
@forastero.requires("driver", MappedResponseResponder)
async def mapped_rsp_backpressure_seq(
    ctx: SeqContext, driver: SeqProxy[MappedResponseResponder]
):
    while True:
        async with ctx.lock(driver):
            driver.enqueue(
                MappedBackpressure(
                    ready=ctx.random.choice((True, False)),
                    cycles=ctx.random.randint(1, 10),
                )
            )
        await driver.wait_for(DriverEvent.PRE_DRIVE)


@forastero.sequence(auto_lock=True)
@forastero.requires("driver", MappedResponseResponder)
async def mapped_rsp_no_backpressure_seq(
    ctx: SeqContext, driver: SeqProxy[MappedResponseResponder]
):
    driver.enqueue(MappedBackpressure(ready=True, cycles=1))


@forastero.sequence()
@forastero.requires("driver", MappedRequestInitiator)
async def mapped_random_reads_seq(
    ctx: SeqContext,
    driver: SeqProxy[MappedRequestInitiator],
    length: int = 1000,
    addresses: list[int] | None = None,
) -> None:
    for _ in range(length):
        async with ctx.lock(driver):
            if addresses:
                address = ctx.random.choice(addresses)
            else:
                address = ctx.random.getrandbits(driver.io.width("addr"))
            driver.enqueue(
                MappedRequest(
                    ident=ctx.random.getrandbits(driver.io.width("id")),
                    address=address,
                    mode=MappedAccess.READ,
                )
            )


@forastero.sequence()
@forastero.requires("driver", MappedRequestInitiator)
async def mapped_random_writes_seq(
    ctx: SeqContext,
    driver: SeqProxy[MappedRequestInitiator],
    length: int = 1000,
    addresses: list[int] | None = None,
) -> None:
    for _ in range(length):
        async with ctx.lock(driver):
            if addresses:
                address = ctx.random.choice(addresses)
            else:
                address = ctx.random.getrandbits(driver.io.width("addr"))
            driver.enqueue(
                MappedRequest(
                    ident=ctx.random.getrandbits(driver.io.width("id")),
                    address=address,
                    mode=MappedAccess.WRITE,
                    data=ctx.random.getrandbits(driver.io.width("data")),
                    strobe=ctx.random.getrandbits(driver.io.width("strobe")),
                )
            )


@forastero.sequence(auto_lock=True)
@forastero.requires("rsp_drv", MappedResponseInitiator)
async def mapped_delayed_response_seq(
    ctx: SeqContext,
    rsp_drv: SeqProxy[MappedResponseInitiator],
    response: MappedResponse,
    min_latency: 0,
    max_latency: 0,
) -> None:
    # Wait for some delay
    await ClockCycles(ctx.clk, ctx.random.randint(min_latency, max_latency))
    # Queue the transaction
    rsp_drv.enqueue(response)
