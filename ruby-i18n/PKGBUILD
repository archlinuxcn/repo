# Maintainer: Nils Czernia <nils at czserver.de>
# Contributor: Severen Redwood <severen@shrike.me>

_gemname="i18n"
pkgname="ruby-${_gemname}"
pkgver=1.1.1
pkgrel=3
pkgdesc="New wave internationalisation support for Ruby"
arch=("any")
license=("MIT")
depends=("rubygems" "ruby-concurrent-ruby")
makedepends=("ruby-rdoc")
options=(!emptydirs)
url="http://rubygems.org/gems/${_gemname}"
source=("https://rubygems.org/downloads/${_gemname}-${pkgver}.gem")
sha256sums=('a7b7e411cd9dbbfd0c4e2cfda9353dffbd149940528bef98d7ea3673430d97bd')
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
