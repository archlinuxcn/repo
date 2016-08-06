# Maintainer: Levente Polyak <anthraxx[at]archlinux[dot]org>
# Contributor: Sabart Otto - Seberm <seberm[at]seberm[dot]com>
# Contributor: Tobias Veit - nIcE <m.on.key.tobi[at]gmail[dot]com>

pkgname=metasploit
pkgver=4.12.17
pkgrel=1
pkgdesc='An advanced open-source platform for developing, testing, and using exploit code'
url='https://www.metasploit.com/'
arch=('i686' 'x86_64')
license=('BSD')
depends=('ruby' 'libpcap' 'postgresql-libs' 'ruby-bundler' 'sqlite' 'libxslt' 'git')
optdepends=('java-runtime: msfgui support'
            'ruby-pg: database support')
options=('!strip' '!emptydirs')
source=(${pkgname}-${pkgver}.tar.gz::https://github.com/rapid7/metasploit-framework/archive/${pkgver}.tar.gz)
sha512sums=('40a568652239b8ee5fdeacc8319547f1e6b33a19fd2213cc0184ecb1925c6f096af9c61f8ffd26a5fa509df70463baa2613bf2bb47f828afc65d669084e73226')

prepare() {
  cd ${pkgname}-framework-${pkgver}
  bundle config build.nokogiri --use-system-libraries
  sed 's|git ls-files|find -type f|' -i metasploit-framework.gemspec
}

build() {
  cd ${pkgname}-framework-${pkgver}
  bundle install -j"$(nproc)" --no-cache --deployment
  find vendor/bundle/ruby -exec chmod o+r '{}' \;
}

package() {
  cd ${pkgname}-framework-${pkgver}

  install -d "${pkgdir}/opt/${pkgname}" "${pkgdir}/usr/bin"
  cp -r . "${pkgdir}/opt/${pkgname}"

  for f in "${pkgdir}"/opt/${pkgname}/msf*; do
    local _msffile="${pkgdir}/usr/bin/`basename "${f}"`"
    echo -e "#!/bin/sh\nBUNDLE_GEMFILE=/opt/${pkgname}/Gemfile bundle exec ruby /opt/${pkgname}/`basename "${f}"` \"\$@\"" > ${_msffile}
    chmod 755 ${_msffile}
  done

  install -Dm 644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
  install -Dm 644 COPYING "${pkgdir}/usr/share/licenses/${pkgname}/COPYING"
  install -d "${pkgdir}/usr/share/doc"
  mv "${pkgdir}/opt/${pkgname}/documentation" "${pkgdir}/usr/share/doc/${pkgname}"
  rm "${pkgdir}/usr/bin/msfupdate"
}

# vim: ts=2 sw=2 et:
