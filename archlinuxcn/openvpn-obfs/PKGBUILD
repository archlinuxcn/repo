# Maintainer: Zhuoyun Wei <wzyboy@wzyboy.org>

pkgname=openvpn-obfs
_pkgname=openvpn
pkgver=2.3.6
pkgrel=2
pkgdesc="OpenVPN binary with obfs patch"
arch=('i686' 'x86_64')
url="https://www.gsea.com.cn/blog/topic/traffic-obsfucate-patch-for-openvpn/"
depends=('openssl' 'lzo' 'iproute2' 'openvpn>=2.3.0' 'libsystemd')
makedepends=('systemd')
license=('custom')
source=(http://swupdate.openvpn.net/community/releases/openvpn-${pkgver}.tar.gz
        openvpn-2.3.6-obfs.patch
        openvpn-obfs@.service)
sha256sums=('7baed2ff39c12e1a1a289ec0b46fcc49ff094ca58b8d8d5f29b36ac649ee5b26'
            'fef778ed0b4facdb20d65d7d7803ab512f36ed7ae6f295e5664a3c953c23bfcf'
            '0f9830b732160523713cd03be3201ba3c5a5bad79fe8bbedc36776558a9feb90')
options=(!libtool)

build() {
  cd $srcdir/$_pkgname-$pkgver
  patch -p0 -F10 -i $srcdir/openvpn-2.3.6-obfs.patch
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
