# Maintainer: Mark Wagie <mark dot wagie at tutanota dot com>
# Contributor: librewish <librewish at gmail dot com>
# Contributor: Chris Severance aur.severach aATt spamgourmet dott com
# Contributor: Jay Garcia <morbidj at gmail dot com>
# Contributor: Doug Newgard <scimmia22 at outlook dot com>
# Contributor: Robert Orzanna <orschiro at gmail dot com>
pkgname=timeshift
pkgver=22.11.2
pkgrel=1
pkgdesc="A system restore utility for Linux"
arch=('i686' 'x86_64' 'armv6h' 'armv7h' 'aarch64')
url="https://github.com/linuxmint/timeshift"
license=('GPL3')
depends=('cronie' 'gtk3' 'libgee' 'libnotify' 'libsoup' 'rsync' 'vte3' 'which'
         'xapp' 'xorg-xhost')
makedepends=('git' 'vala')
checkdepends=('appstream-glib' 'desktop-file-utils')
optdepends=('btrfs-progs: BTRFS support'
            'grub-btrfs: BTRFS snapshots in grub')
install="$pkgname.install"
_commit=d29a7ab6bea9b11610478795ae2d160c52834b4c  # tags/22.11.2^0
source=("git+https://github.com/linuxmint/timeshift.git#commit=$_commit"
#        "read-only-btrfs-snapshot.patch"
        "snapshot-detect.desktop"
        "snapshot-detect")
sha256sums=('SKIP'
            '97b38f4dbd6819542eab0a9217e399f55ec7339af4529432cfab1eb3cff8e0eb'
            'f3c71c6cb42b968c33a24361ff3be1e4cf59000605e74af8e061f0c5679fe315')

pkgver() {
  cd "$srcdir/$pkgname"
  git describe --tags --exclude master* | sed 's/^v//;s/-/+/g'
}

prepare() {
  cd "$srcdir/$pkgname"

  # Recursive make commands should always use the variable MAKE, 
  # not the explicit command name make
  # https://real-world-systems.com/docs/make.1.html#SEC59
  sed -i 's/make/$(MAKE)/g' makefile

  # https://github.com/teejee2008/timeshift/pull/685
#  patch -Np1 -i "$srcdir"/read-only-btrfs-snapshot.patch
}

build() {
  export CFLAGS="${CFLAGS} --std=c99"

  cd "$srcdir/$pkgname"
  make app-gtk
  make app-console
}

check() {
  cd "$srcdir/$pkgname"
  appstream-util validate-relax --nonet debian/*.appdata.xml
  desktop-file-validate "src/$pkgname-gtk.desktop"
}

package() {
  cd "$srcdir/$pkgname/src"
  make DESTDIR="$pkgdir" install

  install -Dm644 $srcdir/snapshot-detect.desktop -t "$pkgdir/etc/xdg/autostart/"
  install -Dm755 $srcdir/snapshot-detect -t "$pkgdir/usr/bin/"
}
