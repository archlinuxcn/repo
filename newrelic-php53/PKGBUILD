# Maintainer: Felix Yan <felixonmars@archlinux.org>
# Contributor: Vinh Nguyen <kurei [at] axcoto.com>

pkgname=newrelic-php53
_pkgname=newrelic-php5
pkgver=6.2.0.158
_libver=20090626
pkgrel=1
pkgdesc="NewRelic PHP 5.3"
arch=('i686' 'x86_64')
url="http://newrelic.com/"
license=('non-free')
depends=('glibc' 'php53')
backup=('etc/php/conf.d/newrelic.ini')
install=$pkgname.install
source=("https://download.newrelic.com/php_agent/release/$_pkgname-$pkgver-linux.tar.gz"
        "newrelic-daemon.service"
        "$pkgname.install")
md5sums=('01fbc0175e4ae522522273ef7f4c6ec0'
         '4fc78347663adcb32ed28eddb546619c'
         '32167cda26104c489f5a672a87543821')

build() {
  cd "$srcdir/$_pkgname-$pkgver-linux"
}

package() {
  cd "$srcdir/$_pkgname-$pkgver-linux" 

  mkdir -p $pkgdir/usr/bin/ \
            $pkgdir/usr/lib/php/modules/ \
            $pkgdir/usr/share/doc/newrelic-php53/ \
            $pkgdir/usr/lib/systemd/system/ \
            $pkgdir/etc/php/conf.d/;

  if [ $CARCH == i686 ]; then
    # Binary Daemon
    install -v -Dm755 ./daemon/newrelic-daemon.x86 $pkgdir/usr/bin/newrelic-daemon
    # PHP extension
    install -v -Dm755 ./agent/x86/newrelic-$_libver-zts.so $pkgdir/usr/lib/php/modules/newrelic-$_libver-zts.so
    install -v -Dm755 ./agent/x86/newrelic-$_libver.so $pkgdir/usr/lib/php/modules/newrelic-$_libver.so
  else
    # Binary Daemon
    install -v -Dm755 ./daemon/newrelic-daemon.x64 $pkgdir/usr/bin/newrelic-daemon
    # PHP extension
    install -v -Dm755 ./agent/x64/newrelic-$_libver-zts.so $pkgdir/usr/lib/php/modules/newrelic-$_libver-zts.so
    install -v -Dm755 ./agent/x64/newrelic-$_libver.so $pkgdir/usr/lib/php/modules/newrelic-$_libver.so
  fi

  install -v -Dm644 ./README.txt ./LICENSE.txt $pkgdir/usr/share/doc/newrelic-php53/
  
  install -v -Dm644 ./scripts/newrelic.ini.template $pkgdir/etc/php/conf.d/newrelic.ini
  install -v -Dm644 ./scripts/newrelic.ini.template $pkgdir/etc/php/conf.d/newrelic.ini.template
  
  install -v -Dm644 ../newrelic-daemon.service $pkgdir/usr/lib/systemd/system/
}
