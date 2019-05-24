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
pkgver=1.15.6.1079
_pkgsum=78232c603
pkgrel=1
pkgdesc='Plex Media Server'
arch=('x86_64' 'armv7h' 'aarch64')
url='https://plex.tv/'
license=('custom')
options=('!emptydirs')
conflicts=('plex-media-server-plexpass')
# Commented to override user version
#backup=('etc/conf.d/plexmediaserver')
install='plex-media-server.install'
source=('plexmediaserver.conf.d'
        'plexmediaserver.service'
        'plex.sysusers'
        'plex.tmpfiles'
        'terms.txt')

source_aarch64=("https://downloads.plex.tv/plex-media-server-new/${pkgver}-${_pkgsum}/debian/plexmediaserver_${pkgver}-${_pkgsum}_arm64.deb")
source_armv7h=("https://downloads.plex.tv/plex-media-server-new/${pkgver}-${_pkgsum}/debian/plexmediaserver_${pkgver}-${_pkgsum}_armhf.deb")
source_x86_64=("https://downloads.plex.tv/plex-media-server-new/${pkgver}-${_pkgsum}/redhat/plexmediaserver-${pkgver}-${_pkgsum}.x86_64.rpm")

sha256sums=('398ba7958598609453f5289b3d5f2389d2756158b340cf28e83c39d9ed60280b'
            '348075917da3bac9659d047a45c264c556475e66779ecd84cf00d178a5b7bebf'
            'c597bee0bcbb59ed791651555a904e5f7e9d2e82f6c6986b6352e5fc38e5b557'
            'e3c278315bf325d9bddbedbbdb5680791acdc72ce3d4972935ef27b491518ce5'
            'dbfb5a9a7146a975863c0932f1a68c4b040ec5d7e693361f39ddfbf60885e631')
sha256sums_x86_64=('aadc3a44f2fdea27a56a5d0c8d9a6d19919c5e4629c2505ee4478890162a72bb')
sha256sums_armv7h=('b25c81444b8e5a86ea9edd540c3c71763d123b774752d981a482dbd26e83ea92')
sha256sums_aarch64=('6aef31b4555ac4c6e3c4376f48543bb58798e079f7666f8c8357ea9b4aee7e13')

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
}

# vim: ts=2 sw=2 et:
