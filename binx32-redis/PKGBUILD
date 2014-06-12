# $Id: PKGBUILD 113033 2014-06-11 15:06:18Z spupykin $
# Upstream Maintainer: Sergej Pupykin <pupykin.s+arch@gmail.com>
# Upstream Maintainer: Jan-Erik Rediger <badboy at archlinux dot us>
# Contributor: nofxx <x@<nick>.com>
# Maintainer: Fantix King <fantix.king at gmail.com>

_basepkgname=redis
pkgname=binx32-redis
pkgver=2.8.11
pkgrel=1
pkgdesc="Advanced key-value store (x32 ABI)"
arch=('x86_64')
url="http://redis.io/"
license=('BSD')
depends=('bash' 'libx32-glibc' "${_basepkgname}")
makedepends=('gcc-multilib-x32>=3.1' 'make' 'pkgconfig')
backup=("etc/redis-x32.conf"
	"etc/logrotate.d/redis-x32")
install=redis.install
source=("http://download.redis.io/releases/redis-$pkgver.tar.gz"
	"redis.service"
	"redis.logrotate"
	"redis.tmpfiles.d")
md5sums=('196e0cf387d8885439add8a3e1cab469'
         'db421c66570172e780ab6c4c9e41ccca'
         '5a51ae6c10564edb716a93f22e821d67'
         '33b11afbb94d642606fc12ba4dda9985')

prepare() {
  cd "$srcdir/${_basepkgname}-${pkgver}"
  sed -i 's|# bind 127.0.0.1|bind 127.0.0.1|' redis.conf
  sed -i 's|daemonize no|daemonize yes|' redis.conf
  sed -i 's|dir \./|dir /var/lib/redis-x32/|' redis.conf
  sed -i 's|pidfile .*|pidfile /run/redis-x32/redis-x32.pid|' redis.conf
  sed -i 's|logfile stdout|logfile /var/log/redis-x32.log|' redis.conf
  sed -i 's|port 6379|port 6378|' redis.conf
}

build() {
  cd "$srcdir/${_basepkgname}-${pkgver}"
  make MALLOC=libc CC="gcc -mx32"
}

package() {
  cd "$srcdir/${_basepkgname}-${pkgver}"
  mkdir -p $pkgdir/usr/bin
  make INSTALL_BIN="$pkgdir/usr/bin" PREFIX=/usr install

  for _x in ${pkgdir}/usr/bin/*; do mv $_x $_x-x32; done
  
  install -Dm644 "$srcdir"/redis.service "$pkgdir"/usr/lib/systemd/system/redis-x32.service
  install -Dm644 "$srcdir/redis.logrotate" "$pkgdir/etc/logrotate.d/redis-x32"
  install -Dm644 "$srcdir/${_basepkgname}-${pkgver}/redis.conf" "$pkgdir/etc/redis-x32.conf"
  install -Dm644 "$srcdir/redis.tmpfiles.d" "$pkgdir/usr/lib/tmpfiles.d/redis-x32.conf"

  # install license
  install -dm755 "$pkgdir"/usr/share/licenses
  ln -s ${_basepkgname} "${pkgdir}"/usr/share/licenses/${pkgname}
}
