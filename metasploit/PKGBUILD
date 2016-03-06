# Maintainer: Levente Polyak <anthraxx[at]archlinux[dot]org>
# Contributor: Sabart Otto - Seberm <seberm[at]seberm[dot]com>
# Contributor: Tobias Veit - nIcE <m.on.key.tobi[at]gmail[dot]com>

pkgname=metasploit
pkgver=4.11.14
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
sha512sums=('c0ba5836a794937a42f230aaac132c6a6af781a70fbf978dea7d7fda269a6052e2912cb29e7fa806fba0618ea4370904e4891658f9935d8c587c0967c378b0e7')

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
