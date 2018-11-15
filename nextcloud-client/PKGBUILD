# Maintainer: Konstantin Shalygin <k0ste@k0ste.ru>
# Contributor: Konstantin Shalygin <k0ste@k0ste.ru>

pkgname='nextcloud-client'
pkgver='2.5.0'
pkgrel='3'
pkgdesc='Nextcloud desktop client'
arch=('i686' 'x86_64')
url='https://nextcloud.com/'
license=('GPL2')
depends=('qt5-webengine' 'qt5-webkit' 'qtkeychain')
makedepends=('extra-cmake-modules' 'python-sphinx' 'qt5-tools' 'doxygen' 'kio')
optdepends=('python2-nautilus: integration with Nautilus'
	    'nemo-python: integration with Nemo'
	    'kio: Resource and network access abstraction (KDE)'
	    'libgnome-keyring: GNOME keyring client')
conflicts=('owncloud-client')
source=("https://github.com/nextcloud/desktop/archive/v${pkgver}.tar.gz")
sha256sums=('4d639f43e49fd4367cd1b99bf21aecb2eac3bd89a7b0d96c7d2a0975baad6528')
backup=('etc/Nextcloud/sync-exclude.lst')

prepare() {
  mkdir -p "${srcdir}/desktop-${pkgver}/build"
}

build() {
  cd "${srcdir}/desktop-${pkgver}/build"

  cmake .. \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_INSTALL_LIBDIR=lib \
    -DCMAKE_INSTALL_PREFIX=/usr
  make
  make doc-man
}

package() {
  cd "${srcdir}/desktop-${pkgver}/build"
  make DESTDIR="${pkgdir}" install
}
