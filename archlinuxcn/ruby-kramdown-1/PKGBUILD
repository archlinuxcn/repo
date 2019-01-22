# Maintainer: Bjoern Franke <bjo@nord-west.org>
# Co-Maintainer: Bert Peters <bert@bertptrs.nl>
# Contributor: Levente Polyak <anthraxx[at]archlinux[dot]org>

_gemname=kramdown
pkgname=ruby-kramdown-1
pkgver=1.17.0
pkgrel=3
pkgdesc='Fast, pure Ruby Markdown superset converter, using a strict syntax definition'
url='https://kramdown.gettalong.org/'
arch=('any')
license=('MIT')
depends=('ruby')
makedepends=('ruby-rdoc' 'ruby-rake')
options=('!emptydirs')
provides=(ruby-$_gemname=$pkgver)
source=(ruby-${_gemname}-${pkgver}.tar.gz::https://github.com/gettalong/kramdown/archive/REL_${pkgver//./_}.tar.gz)
sha256sums=('3f2071848a0cf2283ed52e346061f05d3fca9cfec513bef5d73bdeb3bc7b97d9')
sha512sums=('bf9ab87c1245cd0b920aa22b3107d595b4f55ff44f364076a3da86d3d830e895344270b457c6c38bdf3eaaef88e11ac895d9570e58f5c582e74b8f2288e390d7')

prepare() {
  cd ${_gemname}-REL_${pkgver//./_}
  rake gemspec
  sed -r 's|~>|>=|g' -i ${_gemname}.gemspec # don't give a fuck about rubys bla bla
}

build() {
  cd ${_gemname}-REL_${pkgver//./_}
  gem build ${_gemname}.gemspec
}

package() {
  cd ${_gemname}-REL_${pkgver//./_}
  local _gemdir="$(ruby -e'puts Gem.default_dir')"
  gem install --ignore-dependencies --no-user-install -i "${pkgdir}${_gemdir}" -n "${pkgdir}/usr/bin" ${_gemname}-${pkgver}.gem
  install -Dm 644 README.md -t "${pkgdir}/usr/share/doc/${pkgname}"
  install -Dm 644 COPYING -t "${pkgdir}/usr/share/licenses/${pkgname}"
  # Don't install man to prevent conflicting the actual package.
  # install -d "${pkgdir}/usr/share/man/man1"
  # mv "${pkgdir}/${_gemdir}/gems/kramdown-${pkgver}/man/man1/kramdown.1" "${pkgdir}/usr/share/man/man1"
  rm "${pkgdir}/${_gemdir}/cache/${_gemname}-${pkgver}.gem"
  rm -r "${pkgdir}/${_gemdir}/gems/kramdown-${pkgver}/test"

  # Remove binary to prevent conflict.
  rm "${pkgdir}/usr/bin/${_gemname}"
}

# vim: ts=2 sw=2 et:
