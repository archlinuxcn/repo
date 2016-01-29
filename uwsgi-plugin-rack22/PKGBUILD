# Maintainer: Felix Yan <felixonmars@archlinux.org>
# Contributor: Daniel Wallace <danielwallace at gtmanfred dot com>
# Contributor: Sven-Hendrik Haase <sh@lutzhaase.com>
# Contributor: Daniel Wallace <danielwallace at gtmanfred dot com>
# Contributor: Valentin Hăloiu <vially.ichb+aur@gmail.com>
# Contributor: Angel Velasquez <angvp@archlinux.org>
# Contributor: Kevin Zuber <uKev@knet.eu>
# Contributor: Vsevolod Balashov <vsevolod@balashov.name>
# Contributor: David Runge <dave@sleepmap.de>

pkgname=uwsgi-plugin-rack22
pkgdesc="Plugin for Ruby 2.2 support"
pkgver=2.0.12
pkgrel=1
arch=(i686 x86_64)
url="http://projects.unbit.it/uwsgi"
license=(GPL2)
depends=('ruby2.2' 'uwsgi')
makedepends=('python2')
source=(http://projects.unbit.it/downloads/uwsgi-$pkgver.tar.gz
        archlinux.ini
        uwsgi_ruby20_compatibility.patch
        uwsgi_trick_chroot.patch)

md5sums=('1451cab954bad0d7d7429e4d2c84b5df'
         '9aced0faffc5fc04afccf946e8a2a886'
         '4d09535ce379c8acd76160f35d5d6b55'
         '0c09a52fdb88f08c36a8b380f451ce6d')

prepare(){
    cd $srcdir/uwsgi-$pkgver
    cp $srcdir/archlinux.ini buildconf/archlinux.ini
    for patch in uwsgi_ruby20_compatibility.patch uwsgi_trick_chroot.patch; do
        patch -Np1 -i $srcdir/$patch
    done
}

build() {
  pushd $srcdir/uwsgi-$pkgver

  UWSGICONFIG_RUBYPATH=ruby-2.2 python2 uwsgiconfig.py --plugin plugins/rack archlinux rack22
}

package(){
    install -Dm755 uwsgi-$pkgver/rack22_plugin.so $pkgdir/usr/lib/uwsgi/rack22_plugin.so
}
