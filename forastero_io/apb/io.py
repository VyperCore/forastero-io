# SPDX-License-Identifier: MIT
# Copyright (c) 2023-2024 Vypercore. All Rights Reserved

from forastero.io import BaseIO


class ApbIO(BaseIO):
    def __init__(self, dut, name, role):
        super().__init__(
            dut,
            name,
            role,
            ["paddr", "pprot", "psel", "penable", "pwrite", "pwdata", "pstrb"],
            ["pready", "prdata", "pslverr"],
        )
