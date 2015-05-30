# Maintainer: Brian Bidulock <bidulock@openss7.org>
# Contributo: Jianhui Z <jianhui@outlook.com>
# Contributo: Tau Tsao <realturner at gmail.com>
# Contributor: Tomasz Zok <tomasz.zok [at] gmail.com>
# Contributor: techryda <techryda at silentdome dot com>
# Contributor: Mathias R. <pu154r@overlinux.org>
pkgname=xrdp
pkgver=0.8.0
pkgrel=2
pkgdesc="An open source remote desktop protocol (RDP) server"
url="http://xrdp.sourceforge.net/"
arch=('i686' 'x86_64' 'armv6h')
license=('Apache')
depends=('tigervnc' 'libjpeg-turbo' 'libxrandr' 'libpulse' 'fuse')
backup=('etc/xrdp/sesman.ini' 'etc/xrdp/xrdp.ini')
install=xrdp.install
source=(https://github.com/neutrinolabs/${pkgname}/archive/v${pkgver}.tar.gz
	fixups.patch)
md5sums=('2b0c3affc65ee77ad251514c62896757'
         '07f35f8700cd9384f5d13117fd3a4e04')

prepare() {
  cd "${pkgname}-${pkgver}"

  sed -i 's|/etc/sysconfig/xrdp|/etc/xrdp/xrdp.ini|' instfiles/xrdp.service
  sed -i 's|/etc/sysconfig/xrdp|/etc/xrdp/xrdp.ini|' instfiles/xrdp-sesman.service

  sed -i 's|/usr/local/sbin|/usr/bin|' instfiles/xrdp.sh
  sed -i 's|/usr/sbin|/usr/bin|' instfiles/xrdp.service
  sed -i 's|/usr/sbin|/usr/bin|' instfiles/xrdp-sesman.service

  patch -p2 -b -z .orig <../fixups.patch

  ./bootstrap
}

build() {
  cd "${pkgname}-${pkgver}"
  ./configure --prefix=/usr \
              --sysconfdir=/etc \
              --localstatedir=/var \
              --sbindir=/usr/bin \
              --with-systemdsystemdunitdir=/usr/lib/systemd/system \
              --enable-jpeg \
              --enable-simplesound \
              --enable-fuse \
              --enable-loadpulsemodules
  make V=0
}

package() {
  cd "${pkgname}-${pkgver}"
  make DESTDIR="$pkgdir" install

  install -Dm644 COPYING "$pkgdir"/usr/share/licenses/$pkgname/COPYING
}
