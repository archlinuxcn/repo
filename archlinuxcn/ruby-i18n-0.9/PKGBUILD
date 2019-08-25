# Maintainer: Shengyu Zhang <la@archlinuxcn.org>
# Contributor: Nils Czernia <nils at czserver.de>
# Contributor: Severen Redwood <severen@shrike.me>

_gemname="i18n"
pkgname="ruby-${_gemname}-0.9"
pkgver="0.9.5"
pkgrel=2
pkgdesc="New wave internationalisation support for Ruby, version 0.9.x"
arch=("any")
license=("MIT")
depends=("rubygems" "ruby-concurrent-ruby")
makedepends=("ruby-rdoc")
options=(!emptydirs)
url="http://rubygems.org/gems/${_gemname}"
source=("https://rubygems.org/downloads/${_gemname}-${pkgver}.gem")
sha256sums=('43a58b55056ef171cae9b35df8aa5dee22d3a782f8a9bdd0ec8e8d36cfdf180d')
noextract=("${_gemname}-${pkgver}.gem")
provides=("ruby-i18n=${pkgver}")

package() {
  cd "${srcdir}"
  local _gemdir=$(ruby -e "puts Gem.default_dir")
  gem install --ignore-dependencies --no-user-install -i "${pkgdir}${_gemdir}" \
    -n "${pkgdir}/usr/bin" "${_gemname}-${pkgver}.gem"
  rm "${pkgdir}/${_gemdir}/cache/${_gemname}-${pkgver}.gem"

  install -D -m644 \
    "${pkgdir}/${_gemdir}/gems/${_gemname}-${pkgver}/MIT-LICENSE" \
    "${pkgdir}/usr/share/licenses/${pkgname}/MIT-LICENSE"
}

# vim:set ts=2 sw=2 et:
