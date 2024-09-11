# Copyright 2023-2024 Vypercore - All Rights Reserved
# Unauthorized copying of this file in whole or in part, via any medium is
# strictly prohibited. Proprietary and confidential.

from enum import IntEnum


class Pprot(IntEnum):
    """Protection type"""

    DEFAULT = 0b000
    PRIVILEGE = 0b001
    SECURE = 0b010
    INSTRUCTION = 0b100
