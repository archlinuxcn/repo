# Maintainer: Bjoern Franke <bjo+aur@schafweide.org>
# Contributor: Levente Polyak <anthraxx[at]archlinux[dot]org>

_gemname=jekyll-sass-converter
pkgname=ruby-${_gemname}-1
pkgver=1.5.2
pkgrel=3
pkgdesc='Sass converter for Jekyll (1.x)'
conflicts=('ruby-jekyll-sass-converter')
url='https://github.com/jekyll/jekyll-sass-converter'
arch=('any')
license=('MIT')
depends=('ruby' 'ruby-rdoc' 'ruby-sass')
options=('!emptydirs')
source=(${pkgname}-${pkgver}.tar.gz::https://github.com/jekyll/jekyll-sass-converter/archive/v${pkgver}.tar.gz)
sha256sums=('9e3959e62b0285418cba6625cf3f130c337f3286456c12d6542fc69ecd43d88f')
sha512sums=('370ac6bd150a51afc766e4eb065b55d8965e7c39070fd133ea5422db1c559d4bf84d59bd601a3565792fd90a99c32ea1ccb5ecbed0cc8e1a3a343e7923250cb2')
provides=(ruby-jekyll-sass-converter=$pkgver)
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
  local _gemdir="$(gem env gemdir)"
  gem install --ignore-dependencies --no-user-install -i "${pkgdir}${_gemdir}" -n "${pkgdir}/usr/bin" ${_gemname}-${pkgver}.gem
  install -Dm 644 README.md -t "${pkgdir}/usr/share/doc/${pkgname}"
  install -Dm 644 LICENSE.txt -t "${pkgdir}/usr/share/licenses/${pkgname}"
  rm "${pkgdir}/${_gemdir}/cache/${_gemname}-${pkgver}.gem"
}

# vim: ts=2 sw=2 et:
