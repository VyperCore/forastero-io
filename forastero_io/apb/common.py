# SPDX-License-Identifier: MIT
# Copyright (c) 2023-2024 Vypercore. All Rights Reserved

from enum import IntEnum


class Pprot(IntEnum):
    """Protection type"""

    DEFAULT = 0b000
    PRIVILEGE = 0b001
    SECURE = 0b010
    INSTRUCTION = 0b100
