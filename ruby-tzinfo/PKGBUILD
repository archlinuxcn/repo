# Maintainer: Christoph Scholz <christoph.scholz@gmail.com>
# Contributor: Severen Redwood <severen@shrike.me>
# Contributor: José Augusto <joseaugusto.881@outlook.com>

_gemname='tzinfo'
pkgname="ruby-${_gemname}"
pkgver='1.2.5'
pkgrel=1
pkgdesc='Daylight savings aware transformations between times in different time zones'
arch=('any')
license=('MIT')
depends=('rubygems' 'ruby-rdoc')
options=(!emptydirs)
url="http://rubygems.org/gems/${_gemname}"
source=("https://rubygems.org/downloads/${_gemname}-${pkgver}.gem")
sha256sums=('7f144179fa25bd3ac21f3b532e0925f148cc911a7456de699bf3f623864c5dba')
noextract=("${_gemname}-${pkgver}.gem")

package() {
  cd "${srcdir}"
  local _gemdir=$(ruby -e 'puts Gem.default_dir')
  gem install --ignore-dependencies --no-user-install -i "${pkgdir}${_gemdir}" \
    -n "${pkgdir}/usr/bin" "${_gemname}-${pkgver}.gem"
  rm "${pkgdir}/${_gemdir}/cache/${_gemname}-${pkgver}.gem"

  install -D -m644 \
    "${pkgdir}/${_gemdir}/gems/${_gemname}-${pkgver}/LICENSE" \
    "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}

# vim:set ts=2 sw=2 et:
