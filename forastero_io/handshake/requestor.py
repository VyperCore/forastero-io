# SPDX-License-Identifier: MIT
# Copyright (c) 2023-2024 Vypercore. All Rights Reserved

from cocotb.triggers import RisingEdge
from forastero.driver import BaseDriver
from forastero.monitor import BaseMonitor

from .transaction import HandshakeReq


class HandshakeRequestDriver(BaseDriver):
    async def drive(self, transaction: HandshakeReq):
        # Setup the transaction
        self.io.set("data", transaction.data)
        self.io.set("req", transaction.req)
        # Wait one cycle for setup
        await RisingEdge(self.clk)
        # Wait for the acknowledgement
        while self.io.get("ack") == 0:
            await RisingEdge(self.clk)
        # Clear the request
        self.io.set("req", 0)


class HandshakeRequestMonitor(BaseMonitor):
    async def monitor(self, capture):
        while True:
            await RisingEdge(self.clk)
            if self.rst.value == 1:
                continue
            if self.io.get("req"):
                capture(HandshakeReq(data=self.io.get("data"), req=True))
                while self.io.get("ack") == 0:
                    await RisingEdge(self.clk)
