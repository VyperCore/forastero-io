# SPDX-License-Identifier: MIT
# Copyright (c) 2023-2024 Vypercore. All Rights Reserved

import forastero
from forastero.driver import BaseDriver, DriverEvent
from forastero.sequence import SeqContext, SeqProxy

from .target import (
    AXI4LiteReadAddressTarget,
    AXI4LiteReadResponseTarget,
    AXI4LiteWriteAddressTarget,
    AXI4LiteWriteDataTarget,
    AXI4LiteWriteResponseTarget,
)
from .transaction import AXI4LiteBackpressure


async def axi4lite_backpressure(
    ctx: SeqContext,
    driver: SeqProxy[BaseDriver],
    min_interval: int = 1,
    max_interval: int = 10,
    backpressure: float = 0.5,
):
    """
    Generate random backpressure using the READY signal of an AXI4 interface,
    with options to tune how often backpressure is applied.

    :param min_interval: Shortest time to hold ready constant
    :param max_interval: Longest time to hold ready constant
    :param backpressure: Weighting proportion for how often ready should be low,
                         i.e. values approaching 1 mean always backpressure,
                         while values approaching 0 mean never backpressure
    """
    while True:
        driver.enqueue(
            AXI4LiteBackpressure(
                ready=ctx.random.choices(
                    (True, False), weights=(1.0 - backpressure, backpressure), k=1
                )[0],
                cycles=ctx.random.randint(min_interval, max_interval),
            )
        )
        await driver.wait_for(DriverEvent.PRE_DRIVE)


@forastero.sequence(auto_lock=True)
@forastero.requires("driver", AXI4LiteWriteAddressTarget)
async def axi4lite_aw_backpressure(
    ctx: SeqContext,
    driver: SeqProxy[AXI4LiteWriteAddressTarget],
    min_interval: int = 1,
    max_interval: int = 10,
    backpressure: float = 0.5,
):
    """
    Generate random backpressure using the READY signal of an AXI4 interface,
    with options to tune how often backpressure is applied.

    :param min_interval: Shortest time to hold ready constant
    :param max_interval: Longest time to hold ready constant
    :param backpressure: Weighting proportion for how often ready should be low,
                         i.e. values approaching 1 mean always backpressure,
                         while values approaching 0 mean never backpressure
    """
    await axi4lite_backpressure(ctx, driver, min_interval, max_interval, backpressure)


@forastero.sequence(auto_lock=True)
@forastero.requires("driver", AXI4LiteWriteDataTarget)
async def axi4lite_w_backpressure(
    ctx: SeqContext,
    driver: SeqProxy[AXI4LiteWriteDataTarget],
    min_interval: int = 1,
    max_interval: int = 10,
    backpressure: float = 0.5,
):
    """
    Generate random backpressure using the READY signal of an AXI4 interface,
    with options to tune how often backpressure is applied.

    :param min_interval: Shortest time to hold ready constant
    :param max_interval: Longest time to hold ready constant
    :param backpressure: Weighting proportion for how often ready should be low,
                         i.e. values approaching 1 mean always backpressure,
                         while values approaching 0 mean never backpressure
    """
    await axi4lite_backpressure(ctx, driver, min_interval, max_interval, backpressure)


@forastero.sequence(auto_lock=True)
@forastero.requires("driver", AXI4LiteReadAddressTarget)
async def axi4lite_ar_backpressure(
    ctx: SeqContext,
    driver: SeqProxy[AXI4LiteReadAddressTarget],
    min_interval: int = 1,
    max_interval: int = 10,
    backpressure: float = 0.5,
):
    """
    Generate random backpressure using the READY signal of an AXI4 interface,
    with options to tune how often backpressure is applied.

    :param min_interval: Shortest time to hold ready constant
    :param max_interval: Longest time to hold ready constant
    :param backpressure: Weighting proportion for how often ready should be low,
                         i.e. values approaching 1 mean always backpressure,
                         while values approaching 0 mean never backpressure
    """
    await axi4lite_backpressure(ctx, driver, min_interval, max_interval, backpressure)


@forastero.sequence(auto_lock=True)
@forastero.requires("driver", AXI4LiteWriteResponseTarget)
async def axi4lite_b_backpressure(
    ctx: SeqContext,
    driver: SeqProxy[AXI4LiteWriteResponseTarget],
    min_interval: int = 1,
    max_interval: int = 10,
    backpressure: float = 0.5,
):
    """
    Generate random backpressure using the READY signal of an AXI4 interface,
    with options to tune how often backpressure is applied.

    :param min_interval: Shortest time to hold ready constant
    :param max_interval: Longest time to hold ready constant
    :param backpressure: Weighting proportion for how often ready should be low,
                         i.e. values approaching 1 mean always backpressure,
                         while values approaching 0 mean never backpressure
    """
    await axi4lite_backpressure(ctx, driver, min_interval, max_interval, backpressure)


@forastero.sequence(auto_lock=True)
@forastero.requires("driver", AXI4LiteReadResponseTarget)
async def axi4lite_r_backpressure(
    ctx: SeqContext,
    driver: SeqProxy[AXI4LiteReadResponseTarget],
    min_interval: int = 1,
    max_interval: int = 10,
    backpressure: float = 0.5,
):
    """
    Generate random backpressure using the READY signal of an AXI4 interface,
    with options to tune how often backpressure is applied.

    :param min_interval: Shortest time to hold ready constant
    :param max_interval: Longest time to hold ready constant
    :param backpressure: Weighting proportion for how often ready should be low,
                         i.e. values approaching 1 mean always backpressure,
                         while values approaching 0 mean never backpressure
    """
    await axi4lite_backpressure(ctx, driver, min_interval, max_interval, backpressure)
