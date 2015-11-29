# Maintainer: Jameson Pugh <imntreal@gmail.com>
# Contributor: Swift Geek < swift geek Ã¢t gmail dÃ¸t cÃ¸m>

pkgname=lib32-libappindicator-gtk2
pkgver=12.10.0
pkgrel=5
pkgdesc='Allow applications to export a menu into the Unity Menu bar'
arch=('i686' 'x86_64')
url='https://launchpad.net/libappindicator'
license=('LGPL')
depends=('lib32-libdbusmenu-gtk2' 'lib32-libindicator-gtk2')
provides=('lib32-libappindicator')
makedepends=('dbus-glib' 'gobject-introspection'
             'perl-xml-libxml' 'pygtk' 'vala' 'gtk-sharp-2')
options=('!emptydirs')
source=("http://launchpad.net/libappindicator/${pkgver%.*}/${pkgver}/+download/libappindicator-${pkgver}.tar.gz"
        'python-gtfo.patch')
sha256sums=('d5907c1f98084acf28fd19593cb70672caa0ca1cf82d747ba6f4830d4cc3b49f'
            'a10e2bc67fdfed814a8b4d56a0bae7db4a642327a2d08305ca15e806b5f6df83')

prepare() {
  cd libappindicator-${pkgver}

  sed 's|/cli/|/mono/|' -i bindings/mono/{appindicator-sharp-0.1.pc.in,Makefile.in}
  sed 's/example //g' -i Makefile.in

  rm -rf bindings/python
  patch -p1 < "${srcdir}/python-gtfo.patch"
}

build() {
  cd libappindicator-${pkgver}

  export CC='gcc -m32'
  export CXX='g++ -m32'
  export PKG_CONFIG_PATH='/usr/lib32/pkgconfig'
  export CFLAGS="$CFLAGS -Wno-deprecated-declarations"

  ./configure --prefix='/usr' --sysconfdir='/etc' --localstatedir='/var' --libdir=/usr/lib32 \
              --disable-{gtk-doc-html,mono-test,static,tests}
  make CSC=dmcs -j1
}

package() {
  cd libappindicator-${pkgver}

  make CSC=dmcs -j1 DESTDIR="${pkgdir}" install
  make CSC=dmcs -j1 -C bindings/mono DESTDIR="${pkgdir}" uninstall
  rm -rf "${pkgdir}"/usr/share
  rm -rf "${pkgdir}"/usr/include
}

# vim: ts=2 sw=2 et:
