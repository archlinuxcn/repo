# Maintainer: korjjj <korjjj+aur[at]gmail[dot]com>
# Contributor: TDY <tdy at archlinux dot info>
# Contributor: Adam Ehlers Nyholm Thomsen <adament at gmail dot com>
# Contributor: Nathan Jones <nathanj at insightbb dot com>

pkgname=ledger
pkgver=3.1
pkgrel=2
pkgdesc='A double-entry accounting system with a command-line reporting interface.'
arch=('i686' 'x86_64')
url='http://www.ledger-cli.org'
license=('BSD')
depends=('boost>=1.49' 'mpfr>=2.4.0' 'pcre' 'expat' 'libedit')
makedepends=('cmake' 'git' 'python' 'texinfo' 'texlive-plainextra' 'icu>=55')
options=('!libtool')
install="${pkgname}.install"
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/ledger/${pkgname}/archive/v${pkgver}.tar.gz"
        'ledger_git.diff')
md5sums=('f4389aae3ba96eb5590784db7fa614ca'
         '8b7c6a5727d8ccc0e60851da7df9fbbb')

build() {
  cd "${srcdir}/${pkgname}-${pkgver}"
  git clone --depth=1 https://github.com/${pkgname}/utfcpp.git lib/utfcpp # submodule excluded
  patch -Np1 -i ../ledger_git.diff # https://groups.google.com/forum/#!topic/ledger-cli/BMYK_bupv5Y
  ./acprep --prefix=/usr opt update
  cmake ./ -DCMAKE_INSTALL_LIBDIR=/usr/lib -DBUILD_EMACSLISP:BOOL=ON -DBUILD_DOCS:BOOL=ON
  make doc
}

package() {
  cd ${srcdir}/${pkgname}-${pkgver}
  make DESTDIR=${pkgdir} install
  install -Dm644 ${srcdir}/${pkgname}-${pkgver}/doc/LICENSE ${pkgdir}/usr/share/licenses/${pkgname}/LICENSE
}

# vim:set ts=2 sw=2 et:
