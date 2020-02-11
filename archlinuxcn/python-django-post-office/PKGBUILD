# Maintainer: Joffrey <j-off@live.fr>

pkgname=('python-django-post-office' 'python2-django-post-office')
pkgbase='python-django-post-office'
pkgver='3.2.1'
pkgrel=2
pkgdesc='A simple app to send and manage your emails in Django'
arch=('any')
url='https://github.com/ui/django-post_office'
license=('MIT')
makedepends=('python-setuptools' 'python2-setuptools')
source=("$pkgbase.tar.gz::$url/archive/v$pkgver.tar.gz")
sha256sums=('f9c8767a577001f0a074612c5af562addf10d3631645a11399cb9a72c0cb5318')

package_python-django-post-office() {
    depends=('python-django-jsonfield')
    cd "$srcdir/django-post_office-$pkgver"
    install -Dm644 './LICENSE.txt' "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
    python './setup.py' install --root="$pkgdir" --optimize=1
}

package_python2-django-post-office() {
    depends=('python2-django-jsonfield')
    cd "$srcdir/django-post_office-$pkgver"
    install -Dm644 './LICENSE.txt' "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
    python2 './setup.py' install --root="$pkgdir" --optimize=1
}
