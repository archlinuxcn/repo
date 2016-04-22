# Maintainer: Levente Polyak <anthraxx[at]archlinux[dot]org>
# Contributor: Sabart Otto - Seberm <seberm[at]seberm[dot]com>
# Contributor: Tobias Veit - nIcE <m.on.key.tobi[at]gmail[dot]com>

pkgname=metasploit
pkgver=4.11.21
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
sha512sums=('802e67f6f06e631abcf142b155bea60999051b83ff669cacb011db606f7cca6da46cd08fa08bd170c14ae856919984e4bc6f9a3d04e039d6654375b2dc5bb94d')

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
