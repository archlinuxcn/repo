# Maintainer: Sébastien Luttringer
# Contributor: Michal Soltys <soltys@ziu.info>

pkgname=ebtables
pkgver=2.0.10_4
pkgrel=8
pkgdesc='Ethernet bridge filtering utilities'
arch=('x86_64')
url='http://ebtables.sourceforge.net/'
depends=('perl' 'bash' 'iptables')
license=('GPL2')
backup=("etc/$pkgname.conf")
# ebtables segfault with --as-needed
options=('!buildflags')
install=$pkgname.install
source=("https://downloads.sourceforge.net/${pkgname}/${pkgname}-v${pkgver/_/-}.tar.gz"
        "$pkgname.systemd"
        "$pkgname.service")
md5sums=('506742a3d44b9925955425a659c1a8d0'
         'b4c329060809e5b290ae49fbd0ad61f2'
         '5fc546b232c8e4d66058031ddde71b2f')

build() {
  cd $pkgname-v${pkgver/_/-}
  make CFLAGS='-Wunused -Wall -Werror -Wno-error=unused-but-set-variable'
}

package() {
  pushd $pkgname-v${pkgver/_/-}
  make install \
    DESTDIR="$pkgdir" \
    LIBDIR=/usr/lib \
    MANDIR=/usr/share/man \
    BINDIR=/usr/bin \
    INITDIR=/etc/rc.d \
    SYSCONFIGDIR=/etc
  popd
  # rm package ebtables rc.d scripts
  rm "$pkgdir/etc/ebtables-config"
  rm -r "$pkgdir/etc/rc.d"
  # systemd
  install -Dm 755 $pkgname.systemd \
    "$pkgdir/usr/lib/systemd/scripts/$pkgname"
  install -Dm 644 $pkgname.service \
    "$pkgdir/usr/lib/systemd/system/$pkgname.service"
  # default config file
  install -Dm 644 /dev/null "$pkgdir/etc/$pkgname.conf"
  # since iptables 1.6.0 /etc/ethertype is provided by iptables
  # see https://bugs.archlinux.org/task/48648
  rm "$pkgdir/etc/ethertypes"
}

# vim:set ts=2 sw=2 et:
