# $Id: PKGBUILD 153960 2015-12-21 17:26:59Z spupykin $
# Maintainer:  Sergej Pupykin <pupykin.s+arch@gmail.com>
# Maintainer:  Bartłomiej Piotrowski <bpiotrowski@archlinux.org>
# Contributor: Jan-Erik Rediger <badboy at archlinux dot us>
# Contributor: nofxx <x@<nick>.com>
# x32 Maintainer: Fantix King <fantix.king at gmail.com>

_basepkgname=redis
pkgname=libx32-redis
pkgver=3.0.6
pkgrel=1.1
pkgdesc='Advanced key-value store (x32 ABI)'
arch=('x86_64')
url='http://redis.io/'
license=('BSD')
depends=('libx32-jemalloc' 'grep' 'shadow' 'libx32-glibc' "${_basepkgname}")
backup=('etc/redis-x32.conf'
        'etc/logrotate.d/redis-x32')
install=redis.install
source=(http://download.redis.io/releases/redis-$pkgver.tar.gz
        redis.service
        redis.logrotate
        redis.conf-sane-defaults.patch
        redis-2.8.11-use-system-jemalloc.patch)
md5sums=('9a44ea6bff987d2113caea7761730376'
         'f9fa2ea6d714154966f42ce4fc147b74'
         '5a51ae6c10564edb716a93f22e821d67'
         'cab5413181e8d11c779bdf1e404a98ae'
         '2ae176578f538e37a67a463258302bc6')

prepare() {
  cd $_basepkgname-$pkgver
  patch -p1 -i ../redis.conf-sane-defaults.patch
  patch -p1 -i ../redis-2.8.11-use-system-jemalloc.patch
}

build() {
  make -C $_basepkgname-$pkgver CC="gcc -mx32"
}

package() {
  cd $_basepkgname-$pkgver
  make PREFIX="$pkgdir"/usr install

  for _x in ${pkgdir}/usr/bin/*; do mv $_x $_x-x32; done
  
  install -Dm644 redis.conf "$pkgdir"/etc/redis-x32.conf
  install -Dm644 ../redis.service "$pkgdir"/usr/lib/systemd/system/redis-x32.service

  # files kept for compatibility with installations made before 2.8.13-2
  install -Dm644 ../redis.logrotate "$pkgdir"/etc/logrotate.d/redis-x32
  ln -sf redis-server-x32 $pkgdir/usr/bin/redis-sentinel-x32

  # install license
  install -dm755 "$pkgdir"/usr/share/licenses
  ln -s ${_basepkgname} "${pkgdir}"/usr/share/licenses/${pkgname}
}
