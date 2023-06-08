# Maintainer: Mark Wagie <mark dot wagie at proton dot me>
# Contributor: librewish <librewish at gmail dot com>
# Contributor: Chris Severance aur.severach aATt spamgourmet dott com
# Contributor: Jay Garcia <morbidj at gmail dot com>
# Contributor: Doug Newgard <scimmia22 at outlook dot com>
# Contributor: Robert Orzanna <orschiro at gmail dot com>
pkgname=timeshift
pkgver=23.06.2
pkgrel=1
pkgdesc="A system restore utility for Linux"
arch=('i686' 'x86_64' 'armv6h' 'armv7h' 'aarch64')
url="https://github.com/linuxmint/timeshift"
license=('GPL2')
depends=('cronie' 'gtk3' 'libgee' 'libnotify' 'libsoup' 'rsync' 'vte3' 'which'
         'xapp' 'xorg-xhost')
makedepends=('git' 'help2man' 'meson' 'vala')
checkdepends=('appstream-glib')
optdepends=('btrfs-progs: BTRFS support'
            'grub-btrfs: BTRFS snapshots in grub')
install="$pkgname.install"
_commit=863e734ccc345cb18710937afc372cdd03b4a7ff  # tags/23.06.2^0
source=("git+https://github.com/linuxmint/timeshift.git#commit=$_commit"
        'snapshot-detect.desktop'
        'snapshot-detect')
sha256sums=('SKIP'
            '97b38f4dbd6819542eab0a9217e399f55ec7339af4529432cfab1eb3cff8e0eb'
            'f3c71c6cb42b968c33a24361ff3be1e4cf59000605e74af8e061f0c5679fe315')

pkgver() {
  cd "$srcdir/$pkgname"
  git describe --tags --exclude master* | sed 's/^v//;s/-/+/g'
}

build() {
  arch-meson "$pkgname" build
  meson compile -C build
}

check() {
  cd "$srcdir/$pkgname"
  appstream-util validate-relax --nonet "debian/$pkgname.appdata.xml"
  desktop-file-validate "src/$pkgname-gtk.desktop"
}

package() {
  meson install -C build --destdir "$pkgdir"

  install -Dm644 snapshot-detect.desktop -t "$pkgdir/etc/xdg/autostart/"
  install -Dm755 snapshot-detect -t "$pkgdir/usr/bin/"
}
