# SPDX-License-Identifier: MIT
# Copyright (c) 2023-2024 Vypercore. All Rights Reserved

from cocotb.triggers import RisingEdge
from forastero.driver import BaseDriver

from .transaction import AXI4StreamTransfer


class AXI4StreamInitiator(BaseDriver):
    async def drive(self, transaction: AXI4StreamTransfer):
        self.io.set("tid", transaction.axid)
        self.io.set("tdata", transaction.data)
        self.io.set("tstrb", transaction.strobe)
        self.io.set("tkeep", transaction.keep)
        self.io.set("tlast", transaction.last)
        self.io.set("tdest", transaction.dest)
        self.io.set("tuser", transaction.user)
        self.io.set("tvalid", transaction.valid)
        if transaction.valid:
            while True:
                await RisingEdge(self.clk)
                if self.io.get("tready"):
                    break
            self.io.set("tvalid", 0)
        else:
            await RisingEdge(self.clk)
