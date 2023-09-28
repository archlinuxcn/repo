
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
pkgver=1.32.6.7557
_pkgsum=1cf77d501
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
sha256sums_x86_64=('6651e875d3b16e3161baeb2989ce421e8ac1c87146f3eb3ccfd81b49dcfdd824')
sha256sums_i686=('e5b53c2191fe4d05820b88ad74d56ef8b4dd6076b3ddd459a8271bedf56769d9')
sha256sums_armv7h=('30f20ae9fcd8dbd43ee0e25151e4f81f35baf78a38ec77ff79429feb9b74aff1')
sha256sums_aarch64=('214ddfc4f5c4b1f882bcfbc7bf0b25ce302b385641267e3f2d94205004d1a27a')

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
