# Maintainer: Nils Czernia <nils at czserver.de>
# Contributor: Severen Redwood <severen@shrike.me>

_gemname="i18n"
pkgname="ruby-${_gemname}"
pkgver=1.6.0
pkgrel=1
pkgdesc="New wave internationalisation support for Ruby"
arch=("any")
license=("MIT")
depends=("rubygems" "ruby-concurrent-ruby")
makedepends=("ruby-rdoc")
options=(!emptydirs)
url="http://rubygems.org/gems/${_gemname}"
source=("https://rubygems.org/downloads/${_gemname}-${pkgver}.gem")
sha256sums=("941b77be3243ae41091349c0c598bc170ba4aeaf893b757b111a05933db5ddc1")
noextract=("${_gemname}-${pkgver}.gem")

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
