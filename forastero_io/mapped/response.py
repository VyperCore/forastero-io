# SPDX-License-Identifier: MIT
# Copyright (c) 2023-2024 Vypercore. All Rights Reserved


from cocotb.triggers import ClockCycles, RisingEdge
from forastero.driver import BaseDriver
from forastero.monitor import BaseMonitor

from .transaction import MappedBackpressure, MappedResponse


class MappedResponseInitiator(BaseDriver):
    async def drive(self, transaction: MappedResponse):
        # Setup the transaction
        self.io.set("id", transaction.ident)
        self.io.set("data", transaction.data)
        self.io.set("error", transaction.error)
        # Drive valid (after delay if set)
        if transaction.valid_delay:
            await ClockCycles(self.clk, transaction.valid_delay)
        self.io.set("valid", transaction.valid)
        # Wait for value to be accepted
        while True:
            await RisingEdge(self.clk)
            if self.io.get("ready"):
                break
        self.io.set("valid", 0)


class MappedResponseResponder(BaseDriver):
    async def drive(self, transaction: MappedBackpressure):
        # Setup the transaction
        self.io.set("ready", transaction.ready)
        # Wait for the required number of cycles
        await ClockCycles(self.clk, transaction.cycles)


class MappedResponseMonitor(BaseMonitor):
    async def monitor(self, capture):
        while True:
            await RisingEdge(self.clk)
            if self.rst.value == 1:
                await RisingEdge(self.clk)
                continue
            if self.io.get("valid") and self.io.get("ready"):
                tran = MappedResponse(
                    ident=self.io.get("id", 0),
                    data=self.io.get("data", 0),
                    error=self.io.get("error", 0),
                )
                capture(tran)
