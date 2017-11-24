# Maintainer: Konstantin Shalygin <k0ste@k0ste.ru>
# Contributor: Konstantin Shalygin <k0ste@k0ste.ru>

_next_commit='57bc7918d7b0650c116f3512787f7677d4e5ab17'
pkgname='nextcloud-client'
pkgver='2.3.3'
pkgrel='1'
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
sha256sums=('e3c4393095206648c96980fb23d0520658b3aa8a9a1e31db38b6f59024cb6f8b')
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
