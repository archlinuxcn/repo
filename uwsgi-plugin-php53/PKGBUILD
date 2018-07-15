# Maintainer: Felix Yan <felixonmars@archlinux.org>
# Contributor: Daniel Wallace <danielwallace at gtmanfred dot com>
# Contributor: Sven-Hendrik Haase <sh@lutzhaase.com>
# Contributor: Daniel Wallace <danielwallace at gtmanfred dot com>
# Contributor: Valentin Hăloiu <vially.ichb+aur@gmail.com>
# Contributor: Angel Velasquez <angvp@archlinux.org>
# Contributor: Kevin Zuber <uKev@knet.eu>
# Contributor: Vsevolod Balashov <vsevolod@balashov.name>
# Contributor: David Runge <dave@sleepmap.de>

pkgname=uwsgi-plugin-php53
pkgdesc="Plugin for PHP 5.3 support"
pkgver=2.0.17.1
pkgrel=1
arch=(i686 x86_64)
url="http://projects.unbit.it/uwsgi"
license=(GPL2)
depends=('php53-embed' 'libyaml' 'jansson' 'uwsgi')
makedepends=('python2')
source=(http://projects.unbit.it/downloads/uwsgi-$pkgver.tar.gz
        archlinux.ini
        uwsgi_fix_rpath.patch
        uwsgi_trick_chroot.patch)

md5sums=('0b1d89f62d0a291ba837c57b2f5dae39'
         '9aced0faffc5fc04afccf946e8a2a886'
         '1a4516d5cdcf5b95b036f4eae2d0c152'
         'a49705b98c28dee890b2f88cbaa58be3')

prepare(){
    cd $srcdir/uwsgi-$pkgver
    cp $srcdir/archlinux.ini buildconf/archlinux.ini
    #sed -i 's/LIBS .*-lphp5.*/LIBS = []/' plugins/php/uwsgiplugin.py
    for patch in uwsgi_trick_chroot.patch; do
        patch -Np1 -i $srcdir/$patch
    done
}

build() {
  pushd $srcdir/uwsgi-$pkgver

  UWSGICONFIG_PHPPATH=/usr/bin/php-config53 python2 uwsgiconfig.py --plugin plugins/php archlinux php53
}

package(){
    install -dm755 $pkgdir/usr/bin
    install -Dm755 uwsgi-$pkgver/php53_plugin.so $pkgdir/usr/lib/uwsgi/php53_plugin.so
    ln -s uwsgi $pkgdir/usr/bin/uwsgi_${pkgname#uwsgi-plugin-}
}
