# SPDX-License-Identifier: MIT
# Copyright (c) 2023-2024 Vypercore. All Rights Reserved

from cocotb.triggers import ClockCycles
from forastero.driver import BaseDriver

from .transaction import AXI4LiteBackpressure


class AXI4LiteWriteAddressTarget(BaseDriver):
    async def drive(self, transaction: AXI4LiteBackpressure):
        self.io.set("awready", transaction.ready)
        await ClockCycles(self.clk, transaction.cycles)


class AXI4LiteWriteDataTarget(BaseDriver):
    async def drive(self, transaction: AXI4LiteBackpressure):
        self.io.set("wready", transaction.ready)
        await ClockCycles(self.clk, transaction.cycles)


class AXI4LiteWriteResponseTarget(BaseDriver):
    async def drive(self, transaction: AXI4LiteBackpressure):
        self.io.set("bready", transaction.ready)
        await ClockCycles(self.clk, transaction.cycles)


class AXI4LiteReadAddressTarget(BaseDriver):
    async def drive(self, transaction: AXI4LiteBackpressure):
        self.io.set("arready", transaction.ready)
        await ClockCycles(self.clk, transaction.cycles)


class AXI4LiteReadResponseTarget(BaseDriver):
    async def drive(self, transaction: AXI4LiteBackpressure):
        self.io.set("rready", transaction.ready)
        await ClockCycles(self.clk, transaction.cycles)
