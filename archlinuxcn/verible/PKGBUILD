# Maintainer: poscat

_gittag="v0.0-4003-gd42da6b9"
_tardir="verible-${_gittag/v/}"

pkgname=verible
pkgver="$(echo ${_gittag} | sed 's/\([^-]*-g\)/r\1/;s/-/./g;s/v//g')"
pkgrel=2
pkgdesc="Suite of SystemVerilog developer tools. Including a style-linter, indexer, formatter, and language server"
arch=('x86_64' 'aarch64')
url='https://github.com/chipsalliance/verible'
license=('Apache 2.0')
depends=('bash')
makedepends=('python' 'bazel' 'git' 'm4' 'flex' 'bison')
provides=('verible')
conflicts=('verible-git' 'verible-bin')
source=(
  "verible-${pkgver}.tar.gz::https://github.com/chipsalliance/verible/archive/refs/tags/${_gittag}.tar.gz"
)
sha256sums=('1bbcf14aa5ff5690fef1b2164dfa9f9f8ed1da0aa568af112c8af0e8e941ca42')

build() {
  cd "${srcdir:?}/${_tardir}" || (
    echo -e "\E[1;31mCan't change working directory to ${srcdir}/verible! Build Failed!\E[0m"
    exit 1
  )

  bazel build -c opt --//bazel:use_local_flex_bison //:install-binaries
}

check() {
  cd "${srcdir:?}/${_tardir}" || (
    echo -e "\E[1;31mCan't change working directory to ${srcdir}/verible! Check Failed!\E[0m"
    exit 1
  )

  bazel test -c opt --//bazel:use_local_flex_bison //...
}

package() {
  cd "${srcdir:?}/${_tardir}" || (
    echo -e "\E[1;31mCan't change working directory to ${srcdir}/verible! Package Failed!\E[0m"
    exit 1
  )

  .github/bin/simple-install.sh "${pkgdir:?}/usr/bin"
}
