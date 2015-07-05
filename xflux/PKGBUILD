# Maintainer: Limao Luo <luolimao+AUR@gmail.com>
# Contributor: Gadget3000 <gadget3000@msn.com>
# Contributor: CaptainShanks <captainshanks@archlinux.us>

pkgname=xflux
pkgver=20130901
pkgrel=2
pkgdesc="(f.lux for X) Changes monitor color temperature adaptively to ease eye strain (command-line version)"
arch=(i686 x86_64)
url=http://www.stereopsis.com/flux/
license=(custom)
depends=(gcc-libs libxxf86vm x-server)
if [[ $CARCH == "i686" ]]; then
    _source=xflux-pre
    sha256sums=('fda5d10c3ca16ba38eddc5fbdecebeccd607c4c95787b4379d1ab372760877b4')
    sha512sums=('c35003b9cc6bc95f6ce98efc2e69ea94c99ed31671ec5d1f5919294edd7e504d23aa1df29ec0f1d1c68c4ceafbcd386e1207ef4c9957d7a5079ce96c2ac6d924')
else
    _source=xflux64
    sha256sums=('cc50158fabaeee58c331f006cc1c08fd2940a126e99d37b76c8e878ef20c2021')
    sha512sums=('6204558b8fa1063ee19fe444f740ab4ddfdbc412459b2f5cea94ddbf11818e0c9bff7e066a4958c1ab5c160b1aedcd18fa7fc4cd800a67c5d51ad1206f203e52')
fi

source=(https://justgetflux.com/linux/$_source.tgz
    COPYING)
sha256sums+=('1ae33693bd6865ee48656b4a4fe6ebbbd3bf588b9130d6fc38b162fed7e7b925')
sha512sums+=('7db40fa261c6d8eda20dd638518d889f3628b8a0a6973ab272a81a2f201213d62d6929c7f293da8b7755a08d61dad4c07722d0e5c0800ca9f021e28a51c144c1')

package() {
    install -Dm775 $pkgname "$pkgdir"/usr/bin/$pkgname
    install -Dm644 COPYING "$pkgdir"/usr/share/licenses/$pkgname/COPYING
}
