# SPDX-License-Identifier: MIT
# Copyright (c) 2023-2024 Vypercore. All Rights Reserved

from .io import MappedRequestIO, MappedResponseIO
from .request import (
    MappedRequestInitiator,
    MappedRequestMonitor,
    MappedRequestResponder,
)
from .response import (
    MappedResponseInitiator,
    MappedResponseMonitor,
    MappedResponseResponder,
)
from .sequences import (
    mapped_delayed_response_seq,
    mapped_random_reads_seq,
    mapped_random_writes_seq,
    mapped_req_backpressure_seq,
    mapped_req_no_backpressure_seq,
    mapped_rsp_backpressure_seq,
    mapped_rsp_no_backpressure_seq,
)
from .transaction import MappedAccess, MappedBackpressure, MappedRequest, MappedResponse

# Import guard
assert all(
    (
        # Classes
        MappedAccess,
        MappedBackpressure,
        MappedRequest,
        MappedRequestInitiator,
        MappedRequestIO,
        MappedRequestMonitor,
        MappedRequestResponder,
        MappedResponse,
        MappedResponseInitiator,
        MappedResponseIO,
        MappedResponseMonitor,
        MappedResponseResponder,
        # Sequences
        mapped_delayed_response_seq,
        mapped_random_reads_seq,
        mapped_random_writes_seq,
        mapped_req_backpressure_seq,
        mapped_rsp_backpressure_seq,
        mapped_req_no_backpressure_seq,
        mapped_rsp_no_backpressure_seq,
    )
)
