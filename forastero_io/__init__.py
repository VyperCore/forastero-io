# SPDX-License-Identifier: MIT
# Copyright (c) 2023-2024 Vypercore. All Rights Reserved

from . import apb, axi4, axi4lite, axi4stream, handshake, mapped, stream

# Guard
assert all(
    (
        apb,
        axi4,
        axi4lite,
        axi4stream,
        handshake,
        mapped,
        stream,
    )
)
