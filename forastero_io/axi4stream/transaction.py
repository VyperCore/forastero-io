# SPDX-License-Identifier: MIT
# Copyright (c) 2023-2024 Vypercore. All Rights Reserved

from dataclasses import dataclass

from forastero import BaseTransaction


@dataclass(kw_only=True)
class AXI4StreamTransfer(BaseTransaction):
    index: int = 0
    axid: int = 0
    data: int = 0
    strobe: int = 0
    keep: int = 0
    last: bool = False
    dest: int = 0
    user: int = 0
    valid: bool = True


@dataclass(kw_only=True)
class AXI4StreamBackpressure(BaseTransaction):
    ready: bool = True
    cycles: int = 1
