# Maintainer: Vlad M. <vlad@archlinux.net>
# Contributor: Limao Luo <luolimao+AUR@gmail.com>
# Contributor: Gadget3000 <gadget3000@msn.com>
# Contributor: CaptainShanks <captainshanks@archlinux.us>

pkgname=xflux
pkgver=20130901
pkgrel=3
pkgdesc="(f.lux for X) Changes monitor color temperature adaptively to ease eye strain (command-line version)"
arch=('i686' 'x86_64')
url="https://justgetflux.com/"
license=('custom')
depends=('gcc-libs' 'libxxf86vm' 'x-server')
source=(COPYING)
source_i686=('https://justgetflux.com/linux/xflux-pre.tgz')
source_x86_64=('https://justgetflux.com/linux/xflux64.tgz')
sha256sums=('1ae33693bd6865ee48656b4a4fe6ebbbd3bf588b9130d6fc38b162fed7e7b925')
sha256sums_i686=('fda5d10c3ca16ba38eddc5fbdecebeccd607c4c95787b4379d1ab372760877b4')
sha256sums_x86_64=('cc50158fabaeee58c331f006cc1c08fd2940a126e99d37b76c8e878ef20c2021')

package() {
    install -Dm775 $pkgname "$pkgdir"/usr/bin/$pkgname
    install -Dm644 COPYING "$pkgdir"/usr/share/licenses/$pkgname/COPYING
}
