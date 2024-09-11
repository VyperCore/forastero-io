# SPDX-License-Identifier: MIT
# Copyright (c) 2023-2024 Vypercore. All Rights Reserved

from forastero.io import BaseIO


class AXI4LiteWriteAddressIO(BaseIO):
    def __init__(self, dut, name, role):
        super().__init__(dut, name, role, ["awaddr", "awprot", "awvalid"], ["awready"])


class AXI4LiteWriteDataIO(BaseIO):
    def __init__(self, dut, name, role):
        super().__init__(dut, name, role, ["wdata", "wstrb", "wvalid"], ["wready"])


class AXI4LiteWriteResponseIO(BaseIO):
    def __init__(self, dut, name, role):
        super().__init__(dut, name, role, ["bresp", "bvalid"], ["bready"])


class AXI4LiteReadAddressIO(BaseIO):
    def __init__(self, dut, name, role):
        super().__init__(dut, name, role, ["araddr", "arprot", "arvalid"], ["arready"])


class AXI4LiteReadResponseIO(BaseIO):
    def __init__(self, dut, name, role):
        super().__init__(dut, name, role, ["rdata", "rresp", "rvalid"], ["rready"])
