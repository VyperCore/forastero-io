# SPDX-License-Identifier: MIT
# Copyright (c) 2023-2024 Vypercore. All Rights Reserved

from collections.abc import Callable

from cocotb.handle import HierarchyObject
from forastero.io import BaseIO, IORole


class AXI4LiteWriteAddressIO(BaseIO):
    def __init__(
        self,
        dut: HierarchyObject,
        name: str,
        role: IORole,
        io_style: Callable[[str | None, str, IORole, IORole], str] | None = None,
    ):
        super().__init__(
            dut,
            name,
            role,
            ["awaddr", "awprot", "awvalid"],
            ["awready"],
            io_style=io_style,
        )


class AXI4LiteWriteDataIO(BaseIO):
    def __init__(
        self,
        dut: HierarchyObject,
        name: str,
        role: IORole,
        io_style: Callable[[str | None, str, IORole, IORole], str] | None = None,
    ):
        super().__init__(
            dut,
            name,
            role,
            ["wdata", "wstrb", "wvalid"],
            ["wready"],
            io_style=io_style,
        )


class AXI4LiteWriteResponseIO(BaseIO):
    def __init__(
        self,
        dut: HierarchyObject,
        name: str,
        role: IORole,
        io_style: Callable[[str | None, str, IORole, IORole], str] | None = None,
    ):
        super().__init__(
            dut,
            name,
            role,
            ["bresp", "bvalid"],
            ["bready"],
            io_style=io_style,
        )


class AXI4LiteReadAddressIO(BaseIO):
    def __init__(
        self,
        dut: HierarchyObject,
        name: str,
        role: IORole,
        io_style: Callable[[str | None, str, IORole, IORole], str] | None = None,
    ):
        super().__init__(
            dut,
            name,
            role,
            ["araddr", "arprot", "arvalid"],
            ["arready"],
            io_style=io_style,
        )


class AXI4LiteReadResponseIO(BaseIO):
    def __init__(
        self,
        dut: HierarchyObject,
        name: str,
        role: IORole,
        io_style: Callable[[str | None, str, IORole, IORole], str] | None = None,
    ):
        super().__init__(
            dut,
            name,
            role,
            ["rdata", "rresp", "rvalid"],
            ["rready"],
            io_style=io_style,
        )
