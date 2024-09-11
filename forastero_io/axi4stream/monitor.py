# SPDX-License-Identifier: MIT
# Copyright (c) 2023-2024 Vypercore. All Rights Reserved

from cocotb.triggers import RisingEdge
from forastero.monitor import BaseMonitor

from .transaction import AXI4StreamTransfer


class AXI4StreamMonitor(BaseMonitor):
    async def monitor(self, capture):
        index = 0
        while True:
            await RisingEdge(self.clk)
            if self.rst.value == 1:
                index = 0
                continue
            if self.io.get("tvalid") and self.io.get("tready"):
                capture(
                    AXI4StreamTransfer(
                        index=index,
                        axid=self.io.get("tid", 0),
                        data=self.io.get("tdata", 0),
                        strobe=self.io.get("tstrb", 0),
                        keep=self.io.get("tkeep", 0),
                        last=self.io.get("tlast", 0),
                        dest=self.io.get("tdest", 0),
                        user=self.io.get("tuser", 0),
                        valid=True,
                    )
                )
                if self.io.get("tlast", 1):
                    index = 0
                else:
                    index += 1
