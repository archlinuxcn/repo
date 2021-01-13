# Maintainer: DDoSolitary <DDoSolitary@gmail.com>
# Contributor: Carsten Feuls <archlinux@carstenfeuls.de>

_gemname=net-http-persistent
pkgname=ruby-${_gemname}
pkgver=4.0.1
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
sha512sums=('d3c86c9c58affac8cde1513dd899527406c0baafd3a620b80011e3babf51a4bfd6fb2bd8998fd9c4696d49aad2d014bdf666b9626e06fe4413cb4010f94e5e91')

package() {
  local _gemdir="$(ruby -e'puts Gem.default_dir')"
  gem install --ignore-dependencies --no-user-install -i "${pkgdir}/${_gemdir}" -n "${pkgdir}/usr/bin" ${_gemname}-${pkgver}.gem
  rm "${pkgdir}/${_gemdir}/cache/${_gemname}-${pkgver}.gem"
}
