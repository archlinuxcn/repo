# Maintainer: Alexander F. Rødseth <xyproto@archlinux.org>
# Contributor: Daniel Landau <aur@landau.fi>
# Contributor: Justin Coffman <jcoffman at datasecu dot red>
# Contributor: Sibren Vasse <arch at sibrenvasse dot nl>
# Contributor: oozyslug <oozyslug at gmail dot com>
# Contributor: Justin Coffman <jcoffman at datasecu dot red>

pkgname=byobu
pkgver=7.19
pkgrel=1
pkgdesc='Enhanced tmux'
arch=(any)
url='https://byobu.org/'
license=(GPL-3.0-only)
depends=(libnewt python tmux)
makedepends=(gettext git setconf)
source=("git+https://github.com/dustinkirkland/byobu#tag=$pkgver")
b2sums=('d0a2d96413f8769b4be6b6363301db97577fdd9c3098f81e55814b0167d1c6a6e7064b96b84769fda8ce55b0550e5431500ab66bf5b2f2acb5ea5312f00343dd')

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
