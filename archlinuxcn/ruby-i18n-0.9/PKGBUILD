# Maintainer: Shengyu Zhang <la@archlinuxcn.org>
# Contributor: Nils Czernia <nils at czserver.de>
# Contributor: Severen Redwood <severen@shrike.me>

_gemname="i18n"
pkgname="ruby-${_gemname}-0.9"
pkgver="0.9.1"
pkgrel=1
pkgdesc="New wave internationalisation support for Ruby, version 0.9.x"
arch=("any")
license=("MIT")
depends=("rubygems" "ruby-concurrent-ruby")
makedepends=("ruby-rdoc")
options=(!emptydirs)
url="http://rubygems.org/gems/${_gemname}"
source=("https://rubygems.org/downloads/${_gemname}-${pkgver}.gem")
sha256sums=("1af5e4f1ed73f2258066503bec3612092c2580d5a58f84d8318a5fd7a35b5c0c")
noextract=("${_gemname}-${pkgver}.gem")
provides=("ruby-i18n=${pkgver}")
conflicts=('ruby-i18n')
replaces=('ruby-i18n')

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
