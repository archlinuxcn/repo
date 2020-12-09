# Maintainer: justforlxz <justforlxz@gmail.com>

pkgname=deepin-desktop-base-git
pkgver=2020.11.04.r2.ge439cbc
pkgrel=1
pkgdesc='Base component for Deepin'
arch=('any')
url="https://github.com/linuxdeepin/deepin-desktop-base"
license=('GPL3')
groups=('deepin-git')
conflicts=('deepin-desktop-base')
provides=('deepin-desktop-base')
groups=('deepin-git')
makedepends=('git')
source=("$pkgname::git://github.com/linuxdeepin/deepin-desktop-base"
        distribution.info)
sha512sums=('SKIP'
            '27625e6d0786b8adacdb7c52806d4faa28d2ab6b319a593b3ea9bcb69f0cc18ea19b258d629e3a0069ef9a69503589b0285289caef39a1e85bbd99e915c7cd7d')

pkgver() {
    cd $pkgname
    git describe --long --tags | sed 's/\([^-]*-g\)/r\1/;s/-/./g'
}

build() {
  cd $pkgname
  make
}

package() {
  cd $pkgname
  make DESTDIR="$pkgdir" install

  install -Dm644 "$srcdir"/distribution.info -t "$pkgdir"/usr/share/deepin/

  # Remove Deepin distro's lsb-release
  rm "$pkgdir"/etc/lsb-release

  # Don't override systemd timeouts
  rm -r "$pkgdir"/etc/systemd

  # Make a symlink for deepin-version
  ln -s ../usr/lib/deepin/desktop-version "$pkgdir"/etc/deepin-version

  # Remove UOS logo
  rm "$pkgdir"/usr/share/deepin/uos_logo.svg

  # Remove apt-specific templates
  rm -r "$pkgdir"/usr/share/python-apt
}
