# Maintainer: Patrick Lühne <patrick-arch@luehne.de>

_gemname=liquid
pkgname=ruby-$_gemname
pkgver=4.0.1
pkgrel=1
pkgdesc='Liquid markup language. Safe, customer facing template language for flexible web apps'
url='https://shopify.github.io/liquid/'
arch=('any')
license=('MIT')
makedepends=('ruby-rdoc')
depends=('ruby')
options=('!emptydirs')
source=(${pkgname}-${pkgver}.tar.gz::https://github.com/Shopify/${_gemname}/archive/v${pkgver}.tar.gz)
sha512sums=('6d8a792ea2fa5cd723e826dc9dd26be60179ab3405e9f74bc47a068b863aa0233e3a570faff65c19e669663c4f30201cb4144d2ab4ed23176d695c3d7f0553d0')

prepare() {
  cd ${_gemname}-${pkgver}
  sed -r 's|~>|>=|g' -i ${_gemname}.gemspec # don't give a fuck about rubys bla bla
  sed 's|git ls-files -z|find -type f -print0\|sed "s,\\\\./,,g"|' -i ${_gemname}.gemspec
}

build() {
  cd ${_gemname}-${pkgver}
  gem build ${_gemname}.gemspec
}

package() {
  cd ${_gemname}-${pkgver}
  local _gemdir="$(ruby -e'puts Gem.default_dir')"
  gem install --ignore-dependencies --no-user-install -i "${pkgdir}${_gemdir}" -n "${pkgdir}/usr/bin" ${_gemname}-${pkgver}.gem
  install -Dm 644 README.md -t "${pkgdir}/usr/share/doc/${pkgname}"
  install -Dm 644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
  rm "${pkgdir}/${_gemdir}/cache/${_gemname}-${pkgver}.gem"
}
