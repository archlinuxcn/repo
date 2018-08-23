# Maintainer: Patrick Lühne <patrick-arch@luehne.de>

_gemname=liquid
pkgname=ruby-$_gemname
pkgver=4.0.0
pkgrel=4
pkgdesc='Liquid markup language. Safe, customer facing template language for flexible web apps'
url='https://shopify.github.io/liquid/'
arch=('any')
license=('MIT')
makedepends=('ruby-rdoc')
depends=('ruby')
options=('!emptydirs')
source=(${pkgname}-${pkgver}.tar.gz::https://github.com/Shopify/${_gemname}/archive/v${pkgver}.tar.gz)
sha512sums=('3aa09813e2c6c3b75b9ab0eb1c11ae83f62e6d3dba19c91d8877bf8162edf867b06fbbc4fc3193116313ff98c1fa964b8a01f0cf58c9fb7ed89338f3bffb9cdb')

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
