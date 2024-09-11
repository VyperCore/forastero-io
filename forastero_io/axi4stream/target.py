# SPDX-License-Identifier: MIT
# Copyright (c) 2023-2024 Vypercore. All Rights Reserved

from cocotb.triggers import ClockCycles
from forastero.driver import BaseDriver

from .transaction import AXI4StreamBackpressure


class AXI4StreamTarget(BaseDriver):
    async def drive(self, transaction: AXI4StreamBackpressure):
        self.io.set("tready", transaction.ready)
        await ClockCycles(self.clk, transaction.cycles)
