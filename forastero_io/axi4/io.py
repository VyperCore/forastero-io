# SPDX-License-Identifier: MIT
# Copyright (c) 2023-2024 Vypercore. All Rights Reserved

from forastero.io import BaseIO


class AXI4WriteAddressIO(BaseIO):
    def __init__(self, dut, name, role):
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
        )


class AXI4WriteDataIO(BaseIO):
    def __init__(self, dut, name, role):
        super().__init__(
            dut, name, role, ["wdata", "wstrb", "wlast", "wuser", "wvalid"], ["wready"]
        )


class AXI4WriteResponseIO(BaseIO):
    def __init__(self, dut, name, role):
        super().__init__(
            dut, name, role, ["bid", "bresp", "buser", "bvalid"], ["bready"]
        )


class AXI4ReadAddressIO(BaseIO):
    def __init__(self, dut, name, role):
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
        )


class AXI4ReadResponseIO(BaseIO):
    def __init__(self, dut, name, role):
        super().__init__(
            dut,
            name,
            role,
            ["rid", "rdata", "rresp", "rlast", "ruser", "rvalid"],
            ["rready"],
        )
