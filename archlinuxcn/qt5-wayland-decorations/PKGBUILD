# Maintainer: Mark Wagie <mark dot wagie at proton dot me>
# Contributor: coolingtool <coolingtool-backup@outlook.com>
# Contributor: Felix Yan <felixonmars@archlinux.org>
# Contributor: Andrea Scarpino <andrea@archlinux.org>

pkgname=qt5-wayland-decorations
_basever=5.15.14
pkgver=5.15.14+kde+r58
pkgrel=1
_commit=11e099c6b7fbec0e198bffaf8016676ef430cfba
arch=('x86_64')
url='https://www.qt.io'
license=('GPL3' 'LGPL3' 'FDL' 'custom')
pkgdesc='Provides APIs for Wayland - using QAdwaitaDecorations'
depends=('qt5-declarative' 'libxcomposite')
makedepends=('vulkan-headers' 'git')
provides=('qt5-wayland')
conflicts=('qt5-wayland')

# Fedora patches: https://src.fedoraproject.org/rpms/qt5-qtwayland/tree
_frepourl="https://src.fedoraproject.org/rpms/qt5-qtwayland"
_frepobranch=rawhide
_fcommit=c0ca8c9d633f93c5f65c61ba7fe220ddb7641866
_fpatchfile100='qtwayland-use-adwaita-decorations-by-default.patch'
_fpatchfile101='qtwayland-decoration-support-backports-from-qt6.patch'
_fpatchfile102='qtwayland-client-fix-window-margin-calculation.patch'

source=("git+https://invent.kde.org/qt/qt/qtwayland#commit=${_commit}"
        "${_fpatchfile100}-${_fcommit}::${_frepourl}/raw/${_fcommit}/f/${_fpatchfile100}"
        "${_fpatchfile101}-${_fcommit}::${_frepourl}/raw/${_fcommit}/f/${_fpatchfile101}"
        "${_fpatchfile102}-${_fcommit}::${_frepourl}/raw/${_fcommit}/f/${_fpatchfile102}")
sha256sums=('e659f4b1e029866c7475822837b3db019a5821ffcb8a85d72e7edec9ef42a6d6'
            '5b606c5526b44c0db9f5f7fd4be91c95bcb73bd06af304589c9f8c1922607fca'
            '4d8c5d686666cbaae7550ec3defee66ea56ca624152c56c51ff945693706c29d'
            '569ae734860335b72a0fc04e3418bc87086f574baf8db22c0dc5ba0846e22d4f')

pkgver() {
  cd qtwayland
  echo "${_basever}+kde+r$(git rev-list --count v${_basever}-lts-lgpl..${_commit})" | sed -e 's|+kde+r0||'
}

prepare() {
  mkdir -p build

  cd qtwayland

  # Use QAdwaitaDecorations by default
  patch -p1 -i "../${_fpatchfile100}-${_fcommit}"
  patch -p1 -i "../${_fpatchfile101}-${_fcommit}"
  patch -p1 -i "../${_fpatchfile102}-${_fcommit}"
}

build() {
  cd build

  qmake ../qtwayland
  make
}

package() {
  cd build

  make INSTALL_ROOT="$pkgdir" install

  # Drop QMAKE_PRL_BUILD_DIR because reference the build dir
  find "$pkgdir/usr/lib" -type f -name '*.prl' \
    -exec sed -i -e '/^QMAKE_PRL_BUILD_DIR/d' {} \;

  install -d "$pkgdir"/usr/share/licenses
  ln -s /usr/share/licenses/qt5-base "$pkgdir/usr/share/licenses/$pkgname"
}
