# Maintainer: Levente Polyak <anthraxx[at]archlinux[dot]org>
# Contributor: Sabart Otto - Seberm <seberm[at]seberm[dot]com>
# Contributor: Tobias Veit - nIcE <m.on.key.tobi[at]gmail[dot]com>

pkgname=metasploit
pkgver=4.11.15
pkgrel=1
pkgdesc="An advanced open-source platform for developing, testing, and using exploit code"
url="https://www.metasploit.com/"
arch=('i686' 'x86_64')
license=('BSD')
depends=('ruby' 'libpcap' 'postgresql-libs' 'ruby-bundler' 'sqlite' 'git')
optdepends=(
  'java-runtime: msfgui support'
  'ruby-pg: database support'
)
options=('!strip')
source=(${pkgname}-${pkgver}.tar.gz::https://github.com/rapid7/metasploit-framework/archive/${pkgver}.tar.gz)
sha512sums=('2af1a5e653f43ac700fe999b4f6dde0dbf354cbbbd2de0949cad0cb718eabccad8d96269fca3f63fb5ea4c60368802cdbfce2e78b9e46ef442706353543e2f60')

build() {
  cd ${pkgname}-framework-${pkgver}
  bundle install -j"$(nproc)" --no-cache --deployment
  find vendor/bundle/ruby/*/gems/robots-* -exec chmod o+r '{}' \;
}

package() {
  cd ${pkgname}-framework-${pkgver}

  mkdir -p "${pkgdir}/opt/${pkgname}" "${pkgdir}/usr/bin"
  cp -r . "${pkgdir}/opt/${pkgname}"

  for f in "${pkgdir}"/opt/${pkgname}/msf*; do
    local _msffile="${pkgdir}/usr/bin/`basename "${f}"`"
    echo -e "#!/bin/sh\nBUNDLE_GEMFILE=/opt/${pkgname}/Gemfile bundle exec ruby /opt/${pkgname}/`basename "${f}"` \"\$@\"" > ${_msffile}
    chmod 755 ${_msffile}
  done

  install -Dm 644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
  install -Dm 644 COPYING "${pkgdir}/usr/share/licenses/${pkgname}/COPYING"
}

# vim: ts=2 sw=2 et:
