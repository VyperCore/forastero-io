# SPDX-License-Identifier: MIT
# Copyright (c) 2023-2024 Vypercore. All Rights Reserved

from cocotb.triggers import ClockCycles, RisingEdge
from forastero.driver import BaseDriver

from .transaction import HandshakeAck


class HandshakeResponderDriver(BaseDriver):
    async def drive(self, transaction: HandshakeAck):
        # Wait for a request to be presented
        while self.io.get("req") == 0:
            await RisingEdge(self.clk)
        # Wait for the required number of cycles
        if transaction.delay > 0:
            await ClockCycles(self.clk, transaction.delay)
        # Drive the acknowledgement
        self.io.set("ack", transaction.ack)
        # Wait a cycle
        await RisingEdge(self.clk)
        # Clear the ack
        self.io.set("ack", 0)
