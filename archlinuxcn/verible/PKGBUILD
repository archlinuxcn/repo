# Maintainer: poscat

_gittag=v0.0-3841-g5eb8aa34
_tardir="verible-${_gittag/v/}"

pkgname=verible
pkgver="$(echo ${_gittag} | sed 's/\([^-]*-g\)/r\1/;s/-/./g;s/v//g')"
pkgrel=1
pkgdesc="Suite of SystemVerilog developer tools. Including a style-linter, indexer, formatter, and language server"
arch=('x86_64')
url='https://github.com/chipsalliance/verible'
license=('Apache 2.0')
depends=('bash')
makedepends=('bazel' 'git' 'm4' 'flex' 'bison')
provides=('verible')
conflicts=('verible-git')
source=(
  "verible.tar.gz::https://github.com/chipsalliance/verible/archive/refs/tags/${_gittag}.tar.gz"
)
sha256sums=('fbc9cb32aa8a64ba60f24dc89e8573c8ea62c45d76113a0f2ab5b73babed5990')

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

  bazel run -c opt --//bazel:use_local_flex_bison //:install -- "${pkgdir:?}/usr/bin"
}
