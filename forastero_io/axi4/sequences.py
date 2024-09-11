# SPDX-License-Identifier: MIT
# Copyright (c) 2023-2024 Vypercore. All Rights Reserved

import forastero
from forastero.driver import BaseDriver, DriverEvent
from forastero.sequence import SeqContext, SeqProxy

from .target import (
    AXI4ReadAddressTarget,
    AXI4ReadResponseTarget,
    AXI4WriteAddressTarget,
    AXI4WriteDataTarget,
    AXI4WriteResponseTarget,
)
from .transaction import AXI4Backpressure


async def axi4_backpressure(
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
            AXI4Backpressure(
                ready=ctx.random.choices(
                    (True, False), weights=(1.0 - backpressure, backpressure), k=1
                )[0],
                cycles=ctx.random.randint(min_interval, max_interval),
            )
        )
        await driver.wait_for(DriverEvent.PRE_DRIVE)


@forastero.sequence(auto_lock=True)
@forastero.requires("driver", AXI4WriteAddressTarget)
async def axi4_aw_backpressure(
    ctx: SeqContext,
    driver: SeqProxy[AXI4WriteAddressTarget],
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
    await axi4_backpressure(ctx, driver, min_interval, max_interval, backpressure)


@forastero.sequence(auto_lock=True)
@forastero.requires("driver", AXI4WriteDataTarget)
async def axi4_w_backpressure(
    ctx: SeqContext,
    driver: SeqProxy[AXI4WriteDataTarget],
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
    await axi4_backpressure(ctx, driver, min_interval, max_interval, backpressure)


@forastero.sequence(auto_lock=True)
@forastero.requires("driver", AXI4ReadAddressTarget)
async def axi4_ar_backpressure(
    ctx: SeqContext,
    driver: SeqProxy[AXI4ReadAddressTarget],
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
    await axi4_backpressure(ctx, driver, min_interval, max_interval, backpressure)


@forastero.sequence(auto_lock=True)
@forastero.requires("driver", AXI4WriteResponseTarget)
async def axi4_b_backpressure(
    ctx: SeqContext,
    driver: SeqProxy[AXI4WriteResponseTarget],
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
    await axi4_backpressure(ctx, driver, min_interval, max_interval, backpressure)


@forastero.sequence(auto_lock=True)
@forastero.requires("driver", AXI4ReadResponseTarget)
async def axi4_r_backpressure(
    ctx: SeqContext,
    driver: SeqProxy[AXI4ReadResponseTarget],
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
    await axi4_backpressure(ctx, driver, min_interval, max_interval, backpressure)
