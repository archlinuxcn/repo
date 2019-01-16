# Maintainer: Patrick Lühne <patrick-arch@luehne.de>

_gemname=ruby_dep
pkgname=ruby-$_gemname
pkgver=1.5.0
pkgrel=4
pkgdesc='Automatically helps determine supported Rubies based on .travis.yml file'
url='https://github.com/e2/ruby_dep'
arch=('any')
license=('MIT')
depends=('ruby')
makedepends=('ruby-bundler>=1.11' 'ruby-rdoc')
options=('!emptydirs')
source=(${pkgname}-${pkgver}.tar.gz::https://github.com/e2/${_gemname}/archive/v${pkgver}.tar.gz)
sha512sums=('75baa2bcccdde98ba9440bfc4c578c7efca0287e2a08d850070ab26089fc9256aaf553e9e20281294370c197ddc180a69271f96533680fb2bbbca436583b7d5e')

prepare() {
  cd ${_gemname}-${pkgver}
  sed -r 's|~>|>=|g' -i ${_gemname}.gemspec
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
  install -Dm 644 LICENSE.txt -t "${pkgdir}/usr/share/licenses/${pkgname}"
  rm "${pkgdir}/${_gemdir}/cache/${_gemname}-${pkgver}.gem"
}
