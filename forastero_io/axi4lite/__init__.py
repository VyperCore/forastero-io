# SPDX-License-Identifier: MIT
# Copyright (c) 2023-2024 Vypercore. All Rights Reserved

from .initiator import AXI4LiteReadResponseInitiator, AXI4LiteWriteResponseInitiator
from .io import (
    AXI4LiteReadAddressIO,
    AXI4LiteReadResponseIO,
    AXI4LiteWriteAddressIO,
    AXI4LiteWriteDataIO,
    AXI4LiteWriteResponseIO,
)
from .memory import AXI4LiteMemoryModel
from .target import (
    AXI4LiteReadAddressTarget,
    AXI4LiteReadResponseTarget,
    AXI4LiteWriteAddressTarget,
    AXI4LiteWriteDataTarget,
    AXI4LiteWriteResponseTarget,
)
from .transaction import (
    AXI4LiteBackpressure,
    AXI4LiteReadAddress,
    AXI4LiteReadResponse,
    AXI4LiteWriteAddress,
    AXI4LiteWriteData,
    AXI4LiteWriteResponse,
)

# Guard
assert all(
    (
        AXI4LiteWriteResponseInitiator,
        AXI4LiteReadResponseInitiator,
        AXI4LiteWriteAddressIO,
        AXI4LiteWriteDataIO,
        AXI4LiteWriteResponseIO,
        AXI4LiteReadAddressIO,
        AXI4LiteReadResponseIO,
        AXI4LiteWriteAddressTarget,
        AXI4LiteWriteDataTarget,
        AXI4LiteWriteResponseTarget,
        AXI4LiteReadAddressTarget,
        AXI4LiteReadResponseTarget,
        AXI4LiteWriteAddress,
        AXI4LiteWriteData,
        AXI4LiteWriteResponse,
        AXI4LiteReadAddress,
        AXI4LiteReadResponse,
        AXI4LiteBackpressure,
        AXI4LiteMemoryModel,
    )
)
