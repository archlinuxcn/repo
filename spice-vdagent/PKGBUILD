# Maintainer: mutantmonkey <aur@mutantmonkey.in>
pkgname=spice-vdagent
pkgver=0.16.0
pkgrel=4
pkgdesc="Spice agent xorg client that enables copy and paste between client and X-session and more"
arch=('i686' 'x86_64')
url="http://www.spice-space.org/"
license=('GPL')
depends=('libpciaccess' 'libxinerama' 'libxrandr' 'libxfixes'
         'libsystemd' 'alsa-lib' 'glib2')
optdepends=('dex: start spice-vdagent automatically on login')
makedepends=('systemd' 'spice-protocol>=0.12.8')
backup=('etc/conf.d/spice-vdagentd.conf')
source=("http://www.spice-space.org/download/releases/$pkgname-$pkgver.tar.bz2"{,.sign}
        'spice-vdagentd.conf.d')
sha256sums=('5b951646e0bd996afda2d063e706fa2aad2655af5bdd1b6525260ab50be30f7d'
            'SKIP'
            '7e17b0b30213ed528ba1c206ccaeff340685699cd84901162f40763c50d4a071')
validpgpkeys=('94A9F75661F77A6168649B23A9D8C21429AC6C82')

prepare() {
  cd "$srcdir/$pkgname-$pkgver"

  # libsystemd-login.so was deprecated with systemd 209
  sed -i 's/libsystemd-login >=/libsystemd >=/' configure.ac

  # set udevrulesdir, since this is impossible with a flag
  sed -i 's/udevrulesdir = \/lib/udevrulesdir = \/usr\/lib/' Makefile.am

  # remove mkdir for /var/run/spice-vdagentd
  sed -i 's/$(mkdir_p) $(DESTDIR)$(localstatedir)\/run\/spice-vdagentd/true/' \
    Makefile.am

  sed -i 's/\/var\/run/\/run/' data/tmpfiles.d/spice-vdagentd.conf
}

build() {
  cd "$srcdir/$pkgname-$pkgver"
  autoreconf -fi
  ./configure --prefix=/usr \
    --bindir=/usr/bin --sbindir=/usr/bin --sysconfdir=/etc \
    --localstatedir=/var --libdir=/usr/lib \
    --with-session-info=systemd --with-init-script=systemd \
    --enable-static-uinput
  make
}

check() {
  cd "$srcdir/$pkgname-$pkgver"
  make -k check
}

package() {
  cd "$srcdir/$pkgname-$pkgver"
  make DESTDIR="$pkgdir/" install

  sed -i 's/\/etc\/sysconfig\/spice-vdagentd/\/etc\/conf.d\/spice-vdagentd.conf/' $pkgdir/usr/lib/systemd/system/spice-vdagentd.service
  sed -i 's/\/usr\/sbin/\/usr\/bin/' $pkgdir/usr/lib/systemd/system/spice-vdagentd.service

  install  -Dm0755 "${srcdir}/spice-vdagentd.conf.d" "${pkgdir}/etc/conf.d/spice-vdagentd.conf"
}

# vim:set ts=2 sw=2 et:
