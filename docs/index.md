# Forastero IO

This library offers a collection of drivers and monitors for common protocols
such as [AMBA APB, AXI4, AXI4-Lite, AXI4-Stream](amba.md) along with some simple
interfaces such as [handshake](handshake.md), [stream](stream.md), and
[mapped](mapped.md).

Each component is constructed in the style recommended by the Forastero
[component documentation](https://forastero.intuity.io/components/) - using the
`BaseIO`, `BaseDriver`, `BaseMonitor` and `BaseTransaction` classes.

## Usage

Install the `forastero_io` package directly from the GitHub repository:

```bash
$> python3 -m pip install git+https://github.com/VyperCore/forastero-io.git
```

Then import the components you want to use into your testbench file:

```python title="testbench.py" linenums="1"

from forastero import BaseBench, IORole
from forastero_io.axi4stream import (
    AXI4StreamIO,
    AXI4StreamInitiator,
    AXI4StreamMonitor,
    AXI4StreamTarget,
)

class Testbench(BaseBench):
    def __init__(self, dut):
        super().__init__(dut, clk=dut.i_clk, rst=dut.i_rst)
        # Wrap inbound stream interface
        inbound_io = AXI4StreamIO(dut, "inbound", IORole.RESPONDER)
        self.register("inbound_drv", AXI4StreamInitiator(
            self, inbound_io, self.clk, self.rst,
        ))
        # Wrap outbound stream interface
        outbound_io = AXI4StreamIO(dut, "outbound", IORole.INITIATOR)
        self.register("outbound_mon", AXI4StreamMonitor(
            self, outbound_io, self.clk, self.rst,
        ))
        self.register("outbound_drv", AXI4StreamTarget(
            self, outbound_io, self.clk, self.rst,
        ))
```

Many of the components also include [sequence](https://forastero.intuity.io/sequences/)
definitions that you can use to drive stimulus:

```python title="testcases/simple.py" linenums="1"
from cocotb.log import SimLog
from forastero_io.axi4stream import (AXI4StreamTransfer,
                                     axi4stream_backpressure_seq)

from ..testbench import Testbench

@Testbench.testcase()
async def simple_test(tb: Testbench, log: SimLog):
    # Drive backpressure on the outbound interface
    tb.schedule(axi4stream_backpressure_seq(driver=tb.outbound_drv))
    # Generate transactions
    for _ in range(4):
        # Generate
        elem = AXI4StreamTransfer(data=tb.random.getrandbits(32))
        # Queue onto the inbound interface
        tb.inbound_drv.enqueue(elem)
        # Queue up expected outputs
        tb.scoreboard.channels["outbound_mon"].push_reference(elem)
```
