# Maintainer: tuxce <tuxce.net@gmail.com>
pkgname=aurvote
pkgver=1.8
pkgrel=1
pkgdesc="Tool to vote for favorite AUR packages"
url="http://git.archlinux.fr/aurvote.git/" 
license="GPL" 
arch=('any')
depends=('curl') 
source=($pkgname) 

package() { 
  	install -D -m 755 "$srcdir/$pkgname" "$pkgdir/usr/bin/$pkgname"
}

md5sums=('1cba0a7377b8de6aec9f84b3a5491bda')
