# SPDX-License-Identifier: MIT
# Copyright (c) 2023-2024 Vypercore. All Rights Reserved

from collections.abc import Callable

from cocotb.handle import HierarchyObject
from forastero.io import BaseIO, IORole


class MappedRequestIO(BaseIO):
    def __init__(
        self,
        dut: HierarchyObject,
        name: str | None,
        role: IORole,
        io_style: Callable[[str | None, str, IORole, IORole], str] | None = None,
    ) -> None:
        super().__init__(
            dut=dut,
            name=name,
            role=role,
            init_sigs=["id", "addr", "data", "strobe", "write", "valid"],
            resp_sigs=["ready"],
            io_style=io_style,
        )


class MappedResponseIO(BaseIO):
    def __init__(
        self,
        dut: HierarchyObject,
        name: str | None,
        role: IORole,
        io_style: Callable[[str | None, str, IORole, IORole], str] | None = None,
    ) -> None:
        super().__init__(
            dut=dut,
            name=name,
            role=role,
            init_sigs=["id", "data", "valid", "error"],
            resp_sigs=["ready"],
            io_style=io_style,
        )
