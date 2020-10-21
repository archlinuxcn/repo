# Maintainer: DDoSolitary <DDoSolitary@gmail.com>
# Contributor: Carsten Feuls <archlinux@carstenfeuls.de>

_gemname=net-http-persistent
pkgname=ruby-${_gemname}
pkgver=4.0.0
pkgrel=1
pkgdesc="Manages persistent connections using Net::HTTP plus a speed fix for Ruby 1.8"
arch=('any')
url="https://github.com/drbrain/net-http-persistent"
license=('MIT')
depends=(ruby ruby-connection_pool)
makedepends=('ruby-rdoc')
options=(!emptydirs)
noextract=(${_gemname}-${pkgver}.gem)
source=("https://rubygems.org/downloads/${_gemname}-${pkgver}.gem")
sha512sums=('eccc6cacfdd1dfb99bd0dcb7fe1c13cb1c21eae0104357156888bd0a5b2ee0b0d8ed5687860670c2dc54ccc1cfc7a090592bee160458427f44c255c1b99938d2')

package() {
  local _gemdir="$(ruby -e'puts Gem.default_dir')"
  gem install --ignore-dependencies --no-user-install -i "${pkgdir}/${_gemdir}" -n "${pkgdir}/usr/bin" ${_gemname}-${pkgver}.gem
  rm "${pkgdir}/${_gemdir}/cache/${_gemname}-${pkgver}.gem"
}
