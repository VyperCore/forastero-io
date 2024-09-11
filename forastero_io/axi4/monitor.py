# SPDX-License-Identifier: MIT
# Copyright (c) 2023-2024 Vypercore. All Rights Reserved

from cocotb.triggers import RisingEdge
from forastero.monitor import BaseMonitor

from .common import Arcache, Awcache, Burst, Prot, Resp, Size
from .transaction import (
    AXI4ReadAddress,
    AXI4ReadResponse,
    AXI4WriteAddress,
    AXI4WriteData,
    AXI4WriteResponse,
)


class AXI4WriteAddressMonitor(BaseMonitor):
    async def monitor(self, capture):
        while True:
            await RisingEdge(self.clk)
            if self.rst.value == 1:
                continue
            if self.io.get("awvalid") and self.io.get("awready"):
                capture(
                    AXI4WriteAddress(
                        axid=self.io.get("awid", 0),
                        address=self.io.get("awaddr", 0),
                        length=self.io.get("awlen", 0),
                        size=Size._pt_cast(self.io.get("awsize", 0)),
                        burst=Burst._pt_cast(self.io.get("awburst", 0)),
                        cache=Awcache._pt_cast(self.io.get("awcache", 0)),
                        protection=Prot._pt_cast(self.io.get("awprot", 0)),
                        qos=self.io.get("awqos", 0),
                        region=self.io.get("awregion", 0),
                        user=self.io.get("awuser", 0),
                        valid=1,
                    )
                )


class AXI4WriteDataMonitor(BaseMonitor):
    async def monitor(self, capture):
        index = 0
        while True:
            await RisingEdge(self.clk)
            if self.rst.value == 1:
                index = 0
                continue
            if self.io.get("wvalid") and self.io.get("wready"):
                capture(
                    AXI4WriteData(
                        index=index,
                        data=self.io.get("wdata", 0),
                        strobe=self.io.get("wstrb", 0),
                        last=self.io.get("wlast", 0),
                        user=self.io.get("wuser", 0),
                        valid=1,
                    )
                )
                if self.io.get("wlast", 1):
                    index = 0
                else:
                    index += 1


class AXI4WriteResponseMonitor(BaseMonitor):
    async def monitor(self, capture):
        while True:
            await RisingEdge(self.clk)
            if self.rst.value == 1:
                continue
            if self.io.get("bvalid") and self.io.get("bready"):
                capture(
                    AXI4WriteResponse(
                        axid=self.io.get("bid", 0),
                        response=Resp._pt_cast(self.io.get("bresp", 0)),
                        user=self.io.get("buser", 0),
                        valid=1,
                    )
                )


class AXI4ReadAddressMonitor(BaseMonitor):
    async def monitor(self, capture):
        while True:
            await RisingEdge(self.clk)
            if self.rst.value == 1:
                continue
            if self.io.get("arvalid") and self.io.get("arready"):
                capture(
                    AXI4ReadAddress(
                        axid=self.io.get("arid", 0),
                        address=self.io.get("araddr", 0),
                        length=self.io.get("arlen", 0),
                        size=Size._pt_cast(self.io.get("arsize", 0)),
                        burst=Burst._pt_cast(self.io.get("arburst", 0)),
                        cache=Arcache._pt_cast(self.io.get("arcache", 0)),
                        protection=Prot._pt_cast(self.io.get("arprot", 0)),
                        qos=self.io.get("arqos", 0),
                        region=self.io.get("arregion", 0),
                        user=self.io.get("aruser", 0),
                        valid=1,
                    )
                )


class AXI4ReadResponseMonitor(BaseMonitor):
    async def monitor(self, capture):
        index = 0
        while True:
            await RisingEdge(self.clk)
            if self.rst.value == 1:
                index = 0
                continue
            if self.io.get("rvalid") and self.io.get("rready"):
                capture(
                    AXI4ReadResponse(
                        index=index,
                        axid=self.io.get("rid", 0),
                        data=self.io.get("rdata", 0),
                        response=Resp._pt_cast(self.io.get("rresp", 0)),
                        last=self.io.get("rlast", 0),
                        user=self.io.get("ruser", 0),
                        valid=1,
                    )
                )
                if self.io.get("rlast", 1):
                    index = 0
                else:
                    index += 1
