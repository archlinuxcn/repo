# Maintainer: Konstantin Shalygin <k0ste@k0ste.ru>
# Contributor: Konstantin Shalygin <k0ste@k0ste.ru>

_next_commit='820899d07102b990b19e8b02121221e41f7fbf06'
pkgname='nextcloud-client'
pkgver='2.3.2'
pkgrel='2'
pkgdesc='Nextcloud desktop client'
arch=('i686' 'x86_64')
url='https://nextcloud.com/'
license=('GPL2')
depends=('qt5-webkit' 'hicolor-icon-theme' 'xdg-utils' 'qtkeychain')
makedepends=('git' 'extra-cmake-modules' 'python-sphinx' 'qt5-tools' 'doxygen' 'qtkeychain')
optdepends=('python2-nautilus: integration with Nautilus'
	    'nemo-python: integration with Nemo'
	    'kio: Resource and network access abstraction (KDE)'
	    'libgnome-keyring: GNOME keyring client')
conflicts=('owncloud-client')
source=("https://github.com/nextcloud/client_theming/archive/v${pkgver}.tar.gz")
sha256sums=('fbebbcfc538654d7a5373062d2165638a9bd9e5dbe62b5f4552a942b0b931617')
backup=('etc/Nextcloud/sync-exclude.lst')

prepare() {
  mkdir -p "${srcdir}/client_theming-${pkgver}/build-linux"
  git clone git://github.com/owncloud/client.git "${srcdir}/client_theming-${pkgver}/client"
  cd "${srcdir}/client_theming-${pkgver}/client"
  git checkout "${_next_commit}"
  git submodule update --init --recursive
}

build() {
  cd "${srcdir}/client_theming-${pkgver}/build-linux"

  cmake -D OEM_THEME_DIR="${srcdir}/client_theming-${pkgver}/nextcloudtheme" ../client \
        -DCMAKE_INSTALL_PREFIX=/usr \
        -DCMAKE_INSTALL_LIBDIR=lib \
        -DCMAKE_BUILD_TYPE=Release \
        -DCMAKE_INSTALL_SYSCONFDIR=/etc/${pkgname}
  make
  make doc-man
}

check() {
  sed -Ei 's|Icon(\[.*\])?=nextcloud|Icon\1=Nextcloud|g' "${srcdir}/client_theming-${pkgver}/build-linux/src/gui/nextcloud.desktop"
}

package() {
  cd "${srcdir}/client_theming-${pkgver}/build-linux"
  make DESTDIR="${pkgdir}" install
}
