# SPDX-License-Identifier: MIT
# Copyright (c) 2023-2024 Vypercore. All Rights Reserved

from cocotb.triggers import RisingEdge
from forastero.driver import BaseDriver
from forastero.monitor import BaseMonitor

from .transaction import ApbAccess, ApbRequest, ApbResponse


class ApbInitiatorDriver(BaseDriver):
    """Drive the APB initiator's request"""

    async def drive(self, transaction: ApbRequest):
        # Setup the transaction - PSEL high, PENABLE low
        is_write = transaction.mode is ApbAccess.WRITE
        self.io.set("paddr", transaction.address)
        self.io.set("pprot", int(transaction.protection))
        self.io.set("psel", transaction.select)
        self.io.set("penable", 0)
        self.io.set("pwrite", is_write)
        self.io.set("pwdata", transaction.data if is_write else 0)
        self.io.set("pstrb", transaction.strobe if is_write else 0)
        # On the next cycle set PENABLE
        await RisingEdge(self.clk)
        self.io.set("penable", transaction.enable)
        # Wait for transaction to be accepted
        while self.io.get("pready") == 0:
            await RisingEdge(self.clk)
        # Clear the enable and select
        self.io.set("penable", 0)
        self.io.set("psel", 0)


class ApbInitiatorMonitor(BaseMonitor):
    """Capture the APB initiator's response"""

    async def monitor(self, capture):
        while True:
            await RisingEdge(self.clk)
            if self.rst.value == 1:
                continue
            # If PSEL is low, loop
            if not self.io.get("psel"):
                continue
            # Check PENABLE is low, then wait one cycle
            assert self.io.get("penable") == 0, "Out of sync with APB (PENABLE != 0)"
            await RisingEdge(self.clk)
            # Check PENABLE is high
            assert self.io.get("penable") == 1, "Out of sync with APB (PENABLE != 1)"
            # Wait for PREADY
            while self.io.get("pready") == 0:
                assert self.io.get("penable") == 1, "PENABLE fell early"
                await RisingEdge(self.clk)
            # Determine if this is a write transaction
            is_write = self.io.get("pwrite") == 1
            # Capture the response
            capture(
                ApbResponse(
                    data=0 if is_write else self.io.get("prdata"),
                    slverr=self.io.get("pslverr"),
                    ready=1,
                )
            )
