# Forastero IO

This repository offers a collection of standard interface components for use with
[Forastero](https://forastero.intuity.io) testbenches, this includes:

 * [Arm AMBA](https://developer.arm.com/Architectures/AMBA) APB, AXI4, AXI4-Lite,
   and AXI4-Stream interfaces;
 * Simple handshake (request-acknowledge) interface;
 * Simple stream (valid-ready) interface;
 * Simple mapped access interface (with separate request and response streams).

Documentation is provided in [docs/index.md](docs/index.md) or can be built
locally using [Mkdocs](http://mkdocs.org) (`poetry run mkdocs serve`).

## Support

This library is being actively built, and is expected to change while it matures
and key features are added. We are not providing external support for use of
this library, however we are aiming to make it as easy to use as possible.

As per the licence:

> THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
> IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
> FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
> AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
> LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
> OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
> SOFTWARE.

## Contributions

We will be introducing a contributor licence agreement in the near future. In
the meantime, if you want to contribute please get in touch.

Please feel free to contribute to the project, following these guidelines:

 * Please contribute by creating a fork and submitting a pull request.
 * Pull requests should be as small as possible to resolve the issue they are
   trying to address.
 * Pull requests must respect the goals of the library, as stated in the
   documentation.
 * Pull requests should take care not to make performance worse except for cases
   which require bug fixes.
 * Pull requests should update the documentation for any added/changed
   functionality.
