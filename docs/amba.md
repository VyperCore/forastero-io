# AMBA

Arm's AMBA (Advanced Microcontroller Bus Architecture) is a collection of protocols
used in many ASICs due to its ubiquitous support from IP vendors. The standards
are [openly published](https://developer.arm.com/Architectures/AMBA) on Arm's
website and they encourage their adoption. The definitions of the protocol won't
be discussed here as these are well documented by Arm.

This library includes basic implementations of:

 * AMBA APB version 3 (`from forastero_io import apb`);
 * AMBA AXI version 4 (`from forastero_io import axi4`);
 * AMBA AXI-Lite version 4 (`from forastero_io import axi4lite`);
 * AMBA AXI-Stream version 4 (`from forastero_io import axi4stream`).
