# Maintainer: Felix Yan <felixonmars@gmail.com>
# Contributor: Sascha Weaver <wzyboies@gmail.com>

pkgname=openvpn-obfs-boypt
_pkgname=openvpn
pkgver=2.3.2
pkgrel=1
pkgdesc="OpenVPN binary with obfs patch from BOYPT"
arch=(i686 x86_64)
url="https://www.gsea.com.cn/blog/topic/traffic-obsfucate-patch-for-openvpn/"
depends=('openssl' 'lzo2' 'iproute2' 'openvpn>=2.3.0')
conflicts=('openvpn-obfs')
makedepends=('systemd')
license=('custom')
source=(http://swupdate.openvpn.net/community/releases/openvpn-${pkgver}.tar.gz
        https://gist.github.com/pentie/b1d5d75cdbc47b53bf9b/raw/bfe876b521636c1f9b1a5f3278f875c8258bc3f0/OpenVPN-2.3.0-obfs.patch
        openvpn-2.3.0-fix-systemd-ask-password-path.patch
        openvpn-obfs@.service)
options=(!libtool)

build() {
  cd $srcdir/$_pkgname-$pkgver
  patch -p0 -i $srcdir/OpenVPN-2.3.0-obfs.patch
  patch -p0 -i $srcdir/openvpn-2.3.0-fix-systemd-ask-password-path.patch
  CFLAGS="$CFLAGS -DPLUGIN_LIBDIR=\\\"/usr/lib/openvpn\\\"" ./configure \
    --prefix=/usr \
    --sbindir=/usr/bin \
    --enable-password-save \
    --mandir=/usr/share/man \
    --enable-iproute2 \
    --enable-systemd
  make
}

package() {
  cd $srcdir/$_pkgname-$pkgver
  make DESTDIR=$pkgdir install
  mv $pkgdir/usr/bin/openvpn{,-obfs}
  rm -r $pkgdir/usr/{share,lib,include}
  cd ..
  install -Dm644 openvpn-obfs@.service \
  $pkgdir/usr/lib/systemd/system/openvpn-obfs@.service
}
md5sums=('06e5f93dbf13f2c19647ca15ffc23ac1'
         'c454d0b468df1a60fdc1250781d7d0c1'
         'e1bd1523e38745e948c710db1a330bb1'
         '5a27f1207aba303c01b2874763e2bba0')
