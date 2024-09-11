# SPDX-License-Identifier: MIT
# Copyright (c) 2023-2024 Vypercore. All Rights Reserved

from dataclasses import dataclass

from forastero import BaseTransaction


@dataclass(kw_only=True)
class HandshakeReq(BaseTransaction):
    data: int = 0
    req: bool = True


@dataclass(kw_only=True)
class HandshakeAck(BaseTransaction):
    ack: bool = True
    delay: int = 1
