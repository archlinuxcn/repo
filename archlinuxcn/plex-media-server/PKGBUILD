
# Maintainer: Donald Webster <fryfrog@gmail.com>
# Contributor: Tom Moore <t.moore01@gmail.com>
# Contributor: Mikael Eriksson <mikael_eriksson@miffe.org>
# Contributor: Maxime Gauduin <alucryd@archlinux.org>
# Contributor: Rob Sletten <rsletten@gmail.com>
# Contributor: monty <linksoft@gmx.de>
# Contributor: Jon Wiersma <archaur@jonw.org>
# Contributor: Arthur <arthur.darcet@m4x.org>
# Contributor: Praekon <praekon@googlemail.com>

pkgname=plex-media-server
pkgver=1.29.0.6244
_pkgsum=819d3678c
pkgrel=1
pkgdesc='The back-end media server component of Plex.'
arch=('x86_64' 'i686' 'armv7h' 'aarch64')
url='https://plex.tv/'
license=('custom')
options=('!emptydirs'  '!strip' 'staticlibs')
conflicts=('plex-media-server-plexpass')
backup=('etc/conf.d/plexmediaserver')
install='plex-media-server.install'
source=('plexmediaserver.conf.d'
        'plexmediaserver.service'
        'plexmediaserver.hook'
        'plex.sysusers'
        'plex.tmpfiles'
        'terms.txt')

source_aarch64=("https://downloads.plex.tv/plex-media-server-new/${pkgver}-${_pkgsum}/debian/plexmediaserver_${pkgver}-${_pkgsum}_arm64.deb")
source_armv7h=("https://downloads.plex.tv/plex-media-server-new/${pkgver}-${_pkgsum}/debian/plexmediaserver_${pkgver}-${_pkgsum}_armhf.deb")
source_x86_64=("https://downloads.plex.tv/plex-media-server-new/${pkgver}-${_pkgsum}/redhat/plexmediaserver-${pkgver}-${_pkgsum}.x86_64.rpm")
source_i686=("https://downloads.plex.tv/plex-media-server-new/${pkgver}-${_pkgsum}/redhat/plexmediaserver-${pkgver}-${_pkgsum}.i686.rpm")

sha256sums=('398ba7958598609453f5289b3d5f2389d2756158b340cf28e83c39d9ed60280b'
            'ef09d53d410f92ea5ec3e9549ad9d1ac6136a83a5b60a4ea7c67b67435d752d9'
            'a94c798e3a1b5614020e3dd6ec80d378c0401fa08f411769527ad87a6898e80c'
            'c597bee0bcbb59ed791651555a904e5f7e9d2e82f6c6986b6352e5fc38e5b557'
            'b7ff6525a3c7a8be885edc85bb523095f8e25ddb38873127e2a4e97b28f2c7ad'
            'dbfb5a9a7146a975863c0932f1a68c4b040ec5d7e693361f39ddfbf60885e631')
sha256sums_x86_64=('eefca06cfef57ba1e92300c90ee76065c467b434f5f7f6d91f609ea398c4961d')
sha256sums_i686=('7c5350da750e7ad45ad677fe54af1598a44069c761cc70e395d700341e86a8e1')
sha256sums_armv7h=('7d90d547559f0e82168a54ea9f64e0c4fa0f2c4aacd538a5b70fafa804111e4b')
sha256sums_aarch64=('7fd41168017da84dcda42b7794c590ecc01b7cb23b610688205fdf909a2b5316')

prepare() {
  if [[ $CARCH = armv7h ]] || [[ $CARCH = aarch64 ]]; then
    bsdtar -xf data.tar.xz
  fi
}

package() {
  install -d -m 755 "${pkgdir}/usr/lib/plexmediaserver"
  cp -dr --no-preserve='ownership' "${srcdir}/usr/lib/plexmediaserver" "${pkgdir}/usr/lib/"

  install -D -m 644 "${srcdir}/plexmediaserver.conf.d" "${pkgdir}/etc/conf.d/plexmediaserver"
  install -D -m 644 "${srcdir}/plexmediaserver.service" "${pkgdir}/usr/lib/systemd/system/plexmediaserver.service"
  install -D -m 644 "${srcdir}/plex.sysusers" "${pkgdir}/usr/lib/sysusers.d/plex.conf"
  install -D -m 644 "${srcdir}/plex.tmpfiles" "${pkgdir}/usr/lib/tmpfiles.d/plex.conf"

  install -D -m 644 "${srcdir}/terms.txt" "${pkgdir}/usr/share/licenses/${pkgname}/terms.txt"
  install -D -m 644 "${srcdir}/plexmediaserver.hook" "${pkgdir}/usr/share/doc/${pkgname}/plexmediaserver.hook"
}

# vim: ts=2 sw=2 et:
