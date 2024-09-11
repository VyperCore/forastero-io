# SPDX-License-Identifier: MIT
# Copyright (c) 2023-2024 Vypercore. All Rights Reserved

from enum import IntEnum


class Prot(IntEnum):
    """Protection type"""

    DEFAULT = 0b000
    PRIVILEGE = 0b001
    SECURE = 0b010
    INSTRUCTION = 0b100


class Resp(IntEnum):
    """Response type"""

    OKAY = 0b00
    EX_OKAY = 0b01
    SLVERR = 0b10
    DECERR = 0b11


class Size(IntEnum):
    """Transaction atom size"""

    B1 = 0
    B2 = 1
    B4 = 2
    B8 = 3
    B16 = 4
    B32 = 5
    B64 = 6
    B128 = 7


class Burst(IntEnum):
    """Burst behaviour"""

    FIXED = 0
    INCR = 1
    WRAP = 2


class Arcache(IntEnum):
    """Read caching behaviour"""

    DEV_NON_BUF = 0b0000
    DEV_BUF = 0b0001
    NON_CACHE_NON_BUF = 0b0010
    BUF_NON_CACHE = 0b0011
    WT_NO_ALLOC = 0b1010
    WT_RD_ALLOC = 0b1110
    WB_NO_ALLOC = 0b1011
    WB_RD_ALLOC = 0b1111


class Awcache(IntEnum):
    """Write caching behaviour"""

    DEV_NON_BUF = 0b0000
    DEV_BUF = 0b0001
    NON_CACHE_NON_BUF = 0b0010
    BUF_NON_CACHE = 0b0011
    WT_NO_ALLOC = 0b0110
    WT_WR_ALLOC = 0b1110
    WB_NO_ALLOC = 0b0111
    WB_WR_ALLOC = 0b1111
