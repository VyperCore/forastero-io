# SPDX-License-Identifier: MIT
# Copyright (c) 2023-2024 Vypercore. All Rights Reserved

from collections.abc import Callable

from cocotb.handle import HierarchyObject
from forastero.io import BaseIO, IORole


class ApbIO(BaseIO):
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
            ["paddr", "pprot", "psel", "penable", "pwrite", "pwdata", "pstrb"],
            ["pready", "prdata", "pslverr"],
            io_style=io_style,
        )
