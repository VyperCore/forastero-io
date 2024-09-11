# SPDX-License-Identifier: MIT
# Copyright (c) 2023-2024 Vypercore. All Rights Reserved

from dataclasses import dataclass, field
from enum import IntEnum, auto

from forastero import BaseTransaction


class MappedAccess(IntEnum):
    READ = auto()
    WRITE = auto()


@dataclass(kw_only=True)
class MappedRequest(BaseTransaction):
    cycles: int = 0
    ident: int = 0
    address: int = 0
    mode: MappedAccess = MappedAccess.READ
    data: int = 0
    strobe: int = 0


@dataclass(kw_only=True)
class MappedResponse(BaseTransaction):
    ident: int = 0
    data: int = 0
    valid: bool = True
    valid_delay: int = field(compare=False, default=0)
    error: int = 0


@dataclass(kw_only=True)
class MappedBackpressure(BaseTransaction):
    ready: bool = True
    cycles: int = 0
