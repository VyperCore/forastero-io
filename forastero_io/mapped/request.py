# SPDX-License-Identifier: MIT
# Copyright (c) 2023-2024 Vypercore. All Rights Reserved

import math

from cocotb.triggers import ClockCycles, RisingEdge
from forastero.driver import BaseDriver
from forastero.monitor import BaseMonitor

from .transaction import MappedAccess, MappedBackpressure, MappedRequest


class MappedRequestInitiator(BaseDriver):
    async def drive(self, transaction: MappedRequest):
        # Setup the transaction
        await ClockCycles(self.clk, transaction.cycles)
        is_write = transaction.mode is MappedAccess.WRITE
        self.io.set("id", transaction.ident)
        self.io.set("addr", transaction.address)
        self.io.set("data", transaction.data if is_write else 0)
        self.io.set("strobe", transaction.strobe)
        self.io.set("write", is_write)
        self.io.set("valid", 1)
        # Wait for transaction to be accepted
        while True:
            await RisingEdge(self.clk)
            if self.io.get("ready"):
                break
        # Clear the valid
        self.io.set("valid", 0)


class MappedRequestResponder(BaseDriver):
    async def drive(self, transaction: MappedBackpressure):
        # Setup the transaction
        self.io.set("ready", transaction.ready)
        # Wait for the required number of cycles
        await ClockCycles(self.clk, transaction.cycles)


class MappedRequestMonitor(BaseMonitor):
    """
    Monitor for mapped transaction request interfaces, generates MappedRequest
    objects on each request.

    :param always_strobe: When set to True strobes will be captured on all
                          transactions, when False strobes will only be captured
                          on write transactions
    """

    def __init__(self, *args, always_strobe: bool = False, **kwds) -> None:
        super().__init__(*args, **kwds)
        self.always_strobe = always_strobe

    async def monitor(self, capture):
        strb_default = (1 << math.ceil(self.io.width("data") / 8)) - 1
        while True:
            await RisingEdge(self.clk)
            if self.rst.value == 1:
                continue
            if self.io.get("valid") and self.io.get("ready"):
                is_write = self.io.get("write") == 1
                wr_data = self.io.get("data") if is_write else 0
                strobe = self.io.get("strobe", strb_default)
                if not self.always_strobe and not is_write:
                    strobe = 0
                capture(
                    MappedRequest(
                        ident=self.io.get("id", 0),
                        address=self.io.get("addr"),
                        mode=[MappedAccess.READ, MappedAccess.WRITE][is_write],
                        data=wr_data,
                        strobe=strobe,
                    )
                )
