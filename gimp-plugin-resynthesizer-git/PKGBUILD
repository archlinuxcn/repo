# Maintainer: Lex Black (autumn-wind at web.de)
# Contributor: andre.vmatos

_pkgname=resynthesizer
pkgname=gimp-plugin-$_pkgname-git
pkgver=2.0.r13.g251eedc
pkgrel=2
pkgdesc="Suite of gimp plugins for texture synthesis (like heal-selection). Git-Version"
arch=('i686' 'x86_64')
url="https://github.com/bootchk/resynthesizer"
license=('GPL2')
depends=('gimp')
makedepends=('git' 'intltool')
conflicts=('gimp-resynth' 'gimp-resynth-git')
options=('!emptydirs')
source=('git://github.com/bootchk/resynthesizer#branch=master')
md5sums=('SKIP')


pkgver() {
    cd $_pkgname
    git describe | sed 's/\([^-]*-g\)/r\1/;s/-/./g;s/^v//'
}

prepare() {
    cd $_pkgname
    sed -i 's|/usr/bin/env python|/usr/bin/env python2|' PluginScripts/*.py
    sed -i 's/--enable-maintainer-mode//g' autogen.sh
}

build() {
    cd $_pkgname

    ./autogen.sh --disable-maintainer-mode --prefix=/usr
    make
}

package() {
    cd $_pkgname

    make DESTDIR="$pkgdir/" install
}
