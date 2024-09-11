# SPDX-License-Identifier: MIT
# Copyright (c) 2023-2024 Vypercore. All Rights Reserved

from cocotb.triggers import ClockCycles
from forastero.driver import BaseDriver

from .transaction import AXI4Backpressure


class AXI4WriteAddressTarget(BaseDriver):
    async def drive(self, transaction: AXI4Backpressure):
        self.io.set("awready", transaction.ready)
        await ClockCycles(self.clk, transaction.cycles)


class AXI4WriteDataTarget(BaseDriver):
    async def drive(self, transaction: AXI4Backpressure):
        self.io.set("wready", transaction.ready)
        await ClockCycles(self.clk, transaction.cycles)


class AXI4WriteResponseTarget(BaseDriver):
    async def drive(self, transaction: AXI4Backpressure):
        self.io.set("bready", transaction.ready)
        await ClockCycles(self.clk, transaction.cycles)


class AXI4ReadAddressTarget(BaseDriver):
    async def drive(self, transaction: AXI4Backpressure):
        self.io.set("arready", transaction.ready)
        await ClockCycles(self.clk, transaction.cycles)


class AXI4ReadResponseTarget(BaseDriver):
    async def drive(self, transaction: AXI4Backpressure):
        self.io.set("rready", transaction.ready)
        await ClockCycles(self.clk, transaction.cycles)
