# SPDX-License-Identifier: MIT
# Copyright (c) 2023-2024 Vypercore. All Rights Reserved

from forastero import BaseIO


class HandshakeIO(BaseIO):
    def __init__(self, dut, name, role):
        super().__init__(dut, name, role, ["data", "req"], ["ack"])
