# SPDX-License-Identifier: MIT
# Copyright (c) 2023-2024 Vypercore. All Rights Reserved

from collections.abc import Callable

from cocotb.handle import HierarchyObject
from forastero.io import BaseIO, IORole


class AXI4WriteAddressIO(BaseIO):
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
            [
                "awid",
                "awaddr",
                "awlen",
                "awsize",
                "awburst",
                "awcache",
                "awprot",
                "awqos",
                "awregion",
                "awuser",
                "awvalid",
            ],
            ["awready"],
            io_style=io_style,
        )


class AXI4WriteDataIO(BaseIO):
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
            ["wdata", "wstrb", "wlast", "wuser", "wvalid"],
            ["wready"],
            io_style=io_style,
        )


class AXI4WriteResponseIO(BaseIO):
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
            ["bid", "bresp", "buser", "bvalid"],
            ["bready"],
            io_style=io_style,
        )


class AXI4ReadAddressIO(BaseIO):
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
            [
                "arid",
                "araddr",
                "arlen",
                "arsize",
                "arburst",
                "arcache",
                "arprot",
                "arregion",
                "aruser",
                "arvalid",
            ],
            ["arready"],
            io_style=io_style,
        )


class AXI4ReadResponseIO(BaseIO):
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
            ["rid", "rdata", "rresp", "rlast", "ruser", "rvalid"],
            ["rready"],
            io_style=io_style,
        )
