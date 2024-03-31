# Maintainer: pingplug < aur at pingplug dot me >

pkgname=ccache-ext
pkgver=3
pkgrel=1
pkgdesc='pacman hook for adding more compiler links to ccache'
arch=('any')
license=('custom')
depends=('ccache')
source=('update-ccache-links.sh'
        'update-ccache-links.hook')
sha256sums=('152d8d3cbe25c9c8380f98846f3f80e9b36fe375d4c2c182a9ab3e02ad757146'
            'e7c0cb74b47371162262e1ad57590cbd41a3fdeaa4988370fde98ae19c75703c')
install=$pkgname.install

package() {
  install -d "${pkgdir}/usr/lib/ccache/bin"
  install -d "${pkgdir}/usr/bin"
  install -Dm755 update-ccache-links.sh "${pkgdir}/usr/bin/update-ccache-links"
  install -d "${pkgdir}/usr/share/libalpm/hooks"
  install -Dm644 update-ccache-links.hook "${pkgdir}/usr/share/libalpm/hooks/"
}

# vim: ts=2 sw=2 et:
