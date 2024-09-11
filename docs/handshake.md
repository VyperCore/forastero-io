# Handshake Interface

## Timing Diagram

![Signal diagram for handshake interface](images/handshake.svg){ width=100% }

## Summary

This interface is similar to the [stream interface](stream.md) in that it
transfers data between two components, but unlike the [stream interface](stream.md)
it is not intended to support a continuous stream of data transfer but instead
to offer discrete synchronisation points where two components need to co-ordinate
but may be separated by one or more cycles of pipelining.

## Components

The initiator component drives two components of the interface:

 * `DATA` - carries the data that is being transferred between the upstream and
   downstream;
 * `REQ` - indicates that the initiator wishes to enter a synchronisation point
   with the responder.

The responder component drives one component of the interface:

 * `ACK` - acknowledges to the initiator that the responder is ready to enter
   the synchronisation point.

The synchronisation event occurs when both the `REQ` and `ACK` are observed to
be asserted on the subsequent rising clock edge.

The `DATA` component is optional, it is only required when some form of payload
is necessary alongside the synchronisation event.

## Signalling Rules

 * Once `REQ` has been asserted it may not be de-asserted until `ACK` is
   observed high at the subsequent rising clock edge;
 * Once `REQ` has been asserted the `DATA` must be stable until `ACK` is
   observed high at the subsequent rising clock edge;
 * `ACK` must not be driven by combinational logic that involves either the
   `DATA` or `REQ` signals to avoid creating problematic timing paths;
 * The `ACK` signal does **NOT** need to be immediately de-asserted after the
   `REQ` is accepted, this means that the next synchronisation event cannot be
   requested until both `REQ` and `ACK` are low;
 * This interface is NOT inherently safe for clock domain crossings and therefore
   it must be correctly synchronised.

## Naming Convention

Initiator components should use the following naming convention for signals:

 * `DATA` should be carried by `o_<NAME>_data`;
 * `REQ` should be carried by `o_<NAME>_req`;
 * `ACK` should be carried by `i_<NAME>_ack`.

Responder components should use the following naming convention for signals:

 * `DATA` should be carried by `i_<NAME>_data`;
 * `REQ` should be carried by `i_<NAME>_req`;
 * `ACK` should be carried by `o_<NAME>_ack`.

Where `<NAME>` is a unique and consistent name for the interface, for example
`o_sync_data`, `o_sync_req`, `i_sync_ack`.
