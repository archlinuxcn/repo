# Maintainer: Mark Wagie <mark dot wagie at tutanota dot com>
# Contributor: librewish <librewish at gmail dot com>
# Contributor: Chris Severance aur.severach aATt spamgourmet dott com
# Contributor: Jay Garcia <morbidj at gmail dot com>
# Contributor: Doug Newgard <scimmia22 at outlook dot com>
# Contributor: Robert Orzanna <orschiro at gmail dot com>
pkgname=timeshift
pkgver=22.06.5
pkgrel=1
pkgdesc="A system restore utility for Linux"
arch=('i686' 'x86_64' 'armv6h' 'armv7h' 'aarch64')
url="https://github.com/linuxmint/timeshift"
license=('GPL3')
depends=('cronie' 'gtk3' 'libgee' 'libnotify' 'libsoup' 'rsync' 'vte3' 'xapp'
         'xorg-xhost')
makedepends=('git' 'vala')
checkdepends=('appstream-glib' 'desktop-file-utils')
optdepends=('btrfs-progs: BTRFS support'
            'grub-btrfs: BTRFS snapshots in grub')
install="$pkgname.install"
_commit=dad9aeb520554b72763c8f016f213077ee71ba55
source=("git+https://github.com/linuxmint/timeshift.git#commit=$_commit"
#        "read-only-btrfs-snapshot.patch"
        "snapshot-detect.desktop"
        "snapshot-detect")
sha256sums=('SKIP'
            '97b38f4dbd6819542eab0a9217e399f55ec7339af4529432cfab1eb3cff8e0eb'
            'f3c71c6cb42b968c33a24361ff3be1e4cf59000605e74af8e061f0c5679fe315')

pkgver() {
  cd "$srcdir/$pkgname"
  git describe --tags | sed 's/^v//;s/-/+/g'
}

prepare() {
  cd "$srcdir/$pkgname"
  sed -i -e 's/--Xcc="-O3" //g' src/makefile

  # https://github.com/teejee2008/timeshift/pull/685
  #patch -Np1 -i "$srcdir"/read-only-btrfs-snapshot.patch
}

build() {
  export CFLAGS="${CFLAGS} --std=c99"

  cd "$srcdir/$pkgname/src"
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
