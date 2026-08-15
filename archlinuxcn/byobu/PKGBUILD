# Maintainer: Alexander F. Rødseth <xyproto@archlinux.org>
# Contributor: Daniel Landau <aur@landau.fi>
# Contributor: Justin Coffman <jcoffman at datasecu dot red>
# Contributor: Sibren Vasse <arch at sibrenvasse dot nl>
# Contributor: oozyslug <oozyslug at gmail dot com>
# Contributor: Justin Coffman <jcoffman at datasecu dot red>

pkgname=byobu
pkgver=7.17
pkgrel=1
pkgdesc='Enhanced tmux'
arch=(any)
url='https://byobu.org/'
license=(GPL-3.0-only)
depends=(libnewt python tmux)
makedepends=(gettext git setconf)
source=("git+https://github.com/dustinkirkland/byobu#tag=$pkgver")
b2sums=('02d274dbf79b9e52e737124c5cdec2bb1dbfaf82ce06c4a6dc894a576a8c0935c4480109f99d492fa7f032f070ae168396b6511388a6dec5b1c52eb2a8449ff9')

prepare() {
  cd $pkgname
  
  
  # Adjust path to SOCKETDIR
  setconf etc/byobu/socketdir SOCKETDIR '"/tmp/screens"'

  # Tweak the two .desktop files that comes with Byobu
  cd usr/share/byobu/desktop
  setconf byobu.desktop Name 'Byobu Gnome Terminal'
  setconf byobu.desktop Icon=/usr/share/byobu/pixmaps/byobu.svg
  setconf byobu.desktop \
    Exec "gnome-terminal --name=us.kirkland.terminals.byobu --class=us.kirkland.terminals.byobu -- byobu"
  setconf byobu.desktop.old Icon=/usr/share/byobu/pixmaps/byobu.svg
}

build() {
  cd $pkgname
  autoreconf -fiv
  ./configure --prefix=/usr --sysconfdir=/etc
  make
}

package() {
  DESTDIR="$pkgdir" make -C "$pkgname" install

  # Move .desktop files to /usr/share/applications
  install -d "$pkgdir/usr/share/applications"
  mv "$pkgdir/usr/share/byobu/desktop/byobu.desktop" \
    "$pkgdir/usr/share/applications/byobu.desktop"
  mv "$pkgdir/usr/share/byobu/desktop/byobu.desktop.old" \
    "$pkgdir/usr/share/applications/byobu_old.desktop"
  rmdir "$pkgdir/usr/share/byobu/desktop"
}
