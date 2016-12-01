# Maintainer: Carsten Feuls <archlinux@carstenfeuls.de>

pkgname=ruby-kramdown
pkgver=1.10.0
pkgrel=1
pkgdesc='A fast, pure-Ruby Markdown-superset converter'
arch=(any)
url='http://kramdown.gettalong.org'
license=('MIT')
depends=('ruby')
source=("https://rubygems.org/downloads/kramdown-${pkgver}.gem")
noextract=("kramdown-${pkgver}.gem")
sha512sums=('fa0c8f1de6ea7306c7ca47a99f0d3e4a2e720e8d7d00f85a811b0ddd7f533960d583f94dee59f1d04900069163dd583c70520bedeeada77d673ff1b3d8b3782e')

package() {
  local _gemdir="$(ruby -e'puts Gem.default_dir')"

  gem install --ignore-dependencies --no-user-install \
    -i "${pkgdir}/${_gemdir}" -n "${pkgdir}/usr/bin" "kramdown-${pkgver}.gem"

  install -D -m644 "${pkgdir}/${_gemdir}/gems/kramdown-${pkgver}/COPYING" \
    "${pkgdir}/usr/share/licenses/${pkgname}/LICENCE"
}
