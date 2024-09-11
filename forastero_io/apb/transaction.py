# SPDX-License-Identifier: MIT
# Copyright (c) 2023-2024 Vypercore. All Rights Reserved

from dataclasses import dataclass
from enum import IntEnum, auto

from forastero import BaseTransaction

from .common import Pprot


class ApbAccess(IntEnum):
    READ = auto()
    WRITE = auto()


@dataclass(kw_only=True)
class ApbRequest(BaseTransaction):
    address: int = 0
    protection: Pprot = Pprot.DEFAULT
    mode: ApbAccess = ApbAccess.READ
    data: int = 0
    strobe: int = 0
    select: int = 1
    enable: int = 1


@dataclass(kw_only=True)
class ApbResponse(BaseTransaction):
    data: int = 0
    slverr: int = 0
    ready: int = 1
