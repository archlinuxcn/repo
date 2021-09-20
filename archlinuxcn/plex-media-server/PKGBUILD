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
pkgver=1.24.3.5033
_pkgsum=757abe6b4
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
            '348075917da3bac9659d047a45c264c556475e66779ecd84cf00d178a5b7bebf'
            'a94c798e3a1b5614020e3dd6ec80d378c0401fa08f411769527ad87a6898e80c'
            'c597bee0bcbb59ed791651555a904e5f7e9d2e82f6c6986b6352e5fc38e5b557'
            'b7ff6525a3c7a8be885edc85bb523095f8e25ddb38873127e2a4e97b28f2c7ad'
            'dbfb5a9a7146a975863c0932f1a68c4b040ec5d7e693361f39ddfbf60885e631')
sha256sums_x86_64=('ac36849d4cdbf556955777e6c24ff037e030892eb7bbd4f7b457b03d0eb17cf0')
sha256sums_i686=('bbf0d4ddfa670259b20922bc3f28d5f3187b50564a93954dbdd1afb6167a08a3')
sha256sums_armv7h=('6b65593d6920d52708c7ffdee46d679895d3e18cd260433fad236a258010337b')
sha256sums_aarch64=('bff1e7394f42261f6d3b520fa6379a9e3bb42be71da5aa7dfeab194886a37418')

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
