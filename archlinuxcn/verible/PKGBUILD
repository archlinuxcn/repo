# Maintainer: poscat

_gittag="v0.0-4051-g9fdb4057"
_tardir="verible-${_gittag/v/}"

pkgname=verible
pkgver="$(echo ${_gittag} | sed 's/\([^-]*-g\)/r\1/;s/-/./g;s/v//g')"
pkgrel=2
pkgdesc="Suite of SystemVerilog developer tools. Including a style-linter, indexer, formatter, and language server"
arch=('x86_64' 'aarch64')
url='https://github.com/chipsalliance/verible'
license=('Apache 2.0')
depends=('bash')
makedepends=('python' 'bazelisk' 'git' 'm4' 'flex' 'bison')
provides=('verible')
conflicts=('verible-git' 'verible-bin')
source=(
  "verible-${pkgver}.tar.gz::https://github.com/chipsalliance/verible/archive/refs/tags/${_gittag}.tar.gz"
)
sha256sums=('001dd2cfe434d18e4229f43abc3988cbefd0804cdc8574f342b4ddc46dd510cb')

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
