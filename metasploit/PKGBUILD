# Maintainer: Levente Polyak <anthraxx[at]archlinux[dot]org>
# Contributor: Sabart Otto - Seberm <seberm[at]seberm[dot]com>
# Contributor: Tobias Veit - nIcE <m.on.key.tobi[at]gmail[dot]com>

pkgname=metasploit
pkgver=4.11.11
pkgrel=1
pkgdesc="An advanced open-source platform for developing, testing, and using exploit code"
url="https://www.metasploit.com/"
arch=('any')
license=('BSD')
depends=('ruby' 'libpcap' 'postgresql-libs' 'ruby-bundler' 'sqlite' 'git')
optdepends=(
  'java-runtime: msfgui support'
  'ruby-pg: database support'
)
options=('!strip')
install="${pkgname}.install"
source=(${pkgname}-${pkgver}.tar.gz::https://github.com/rapid7/metasploit-framework/archive/${pkgver}.tar.gz)
sha512sums=('cc0a508945672c77ec1ad6bcb176c4aa9d51641ea27f7fe70cd2d3cc40a2e1889c7136bbbe930c77d6deaadb61fd0945b3ad15c925feefde57881b8ef61c4565')

package() {
  cd ${pkgname}-framework-${pkgver}

  mkdir -p "${pkgdir}/opt/${pkgname}" "${pkgdir}/usr/bin"
  cp -r . "${pkgdir}/opt/${pkgname}"

  for f in "${pkgdir}"/opt/${pkgname}/msf*; do
    local _msffile="${pkgdir}/usr/bin/`basename "${f}"`"
    echo "BUNDLE_GEMFILE=/opt/${pkgname}/Gemfile bundle exec ruby /opt/${pkgname}/`basename "${f}"` \"\$@\"" > ${_msffile}
    chmod 755 ${_msffile}
  done

  install -Dm 644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
  install -Dm 644 COPYING "${pkgdir}/usr/share/licenses/${pkgname}/COPYING"
}

# vim: ts=2 sw=2 et:
