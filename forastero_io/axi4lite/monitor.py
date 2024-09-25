# SPDX-License-Identifier: MIT
# Copyright (c) 2023-2024 Vypercore. All Rights Reserved

from cocotb.triggers import RisingEdge
from forastero.monitor import BaseMonitor

from ..axi4.common import Prot, Resp
from .transaction import (
    AXI4LiteReadAddress,
    AXI4LiteReadResponse,
    AXI4LiteWriteAddress,
    AXI4LiteWriteData,
    AXI4LiteWriteResponse,
)


class AXI4LiteWriteAddressMonitor(BaseMonitor):
    async def monitor(self, capture):
        while True:
            await RisingEdge(self.clk)
            if self.rst.value == 1:
                continue
            if self.io.get("awvalid") and self.io.get("awready"):
                capture(
                    AXI4LiteWriteAddress(
                        address=self.io.get("awaddr"),
                        protection=Prot(self.io.get("awprot")),
                        valid=1,
                    )
                )


class AXI4LiteWriteDataMonitor(BaseMonitor):
    async def monitor(self, capture):
        while True:
            await RisingEdge(self.clk)
            if self.rst.value == 1:
                continue
            if self.io.get("wvalid") and self.io.get("wready"):
                capture(
                    AXI4LiteWriteData(
                        data=self.io.get("wdata"), strobe=self.io.get("wstrb"), valid=1
                    )
                )


class AXI4LiteWriteResponseMonitor(BaseMonitor):
    async def monitor(self, capture):
        while True:
            await RisingEdge(self.clk)
            if self.rst.value == 1:
                continue
            if self.io.get("bvalid") and self.io.get("bready"):
                capture(
                    AXI4LiteWriteResponse(
                        response=Resp(self.io.get("bresp", 0)),
                        valid=1,
                    )
                )


class AXI4LiteReadAddressMonitor(BaseMonitor):
    async def monitor(self, capture):
        while True:
            await RisingEdge(self.clk)
            if self.rst.value == 1:
                continue
            if self.io.get("arvalid") and self.io.get("arready"):
                capture(
                    AXI4LiteReadAddress(
                        address=self.io.get("araddr"),
                        protection=Prot(self.io.get("arprot")),
                        valid=1,
                    )
                )


class AXI4LiteReadResponseMonitor(BaseMonitor):
    async def monitor(self, capture):
        while True:
            await RisingEdge(self.clk)
            if self.rst.value == 1:
                continue
            if self.io.get("rvalid") and self.io.get("rready"):
                capture(
                    AXI4LiteReadResponse(
                        data=self.io.get("rdata", 0),
                        response=Resp(self.io.get("rresp", 0)),
                        valid=1,
                    )
                )
