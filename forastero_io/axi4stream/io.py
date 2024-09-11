# SPDX-License-Identifier: MIT
# Copyright (c) 2023-2024 Vypercore. All Rights Reserved

from forastero.io import BaseIO


class AXI4StreamIO(BaseIO):
    def __init__(self, dut, name, role):
        super().__init__(
            dut,
            name,
            role,
            [
                "tid",
                "tdata",
                "tstrb",
                "tkeep",
                "tlast",
                "tdest",
                "tuser",
                "tvalid",
            ],
            ["tready"],
        )
