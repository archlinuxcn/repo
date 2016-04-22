# Contributor: Doug Newgard <scimmia at archlinux dot info>
# Contributor: Jameson Pugh <imntreal@gmail.com>
 
pkgname=onedrive
pkgver=1.1
pkgrel=2
pkgdesc='Free OneDrive client written in D'
arch=('i686' 'x86_64')
url='https://github.com/skilion/onedrive'
license=('GPL3')
depends=('curl' 'sqlite')
makedepends=('dmd')
install=$pkgname.install
source=("https://github.com/skilion/onedrive/archive/v$pkgver.tar.gz")
sha256sums=('c54fad2b452a6a84e009f8743efecdaaca37abcbfe046fc830d7e101cac3594d')
 
prepare() {
  cd $pkgname-$pkgver
  
  sed -i 's|/usr/local|/usr|g' onedrive.service
}

build() {
  cd $pkgname-$pkgver

  make
}
 
package() {
  cd $pkgname-$pkgver

  install -Dm755 onedrive "$pkgdir/usr/bin/onedrive"
  install -Dm644 onedrive.conf "$pkgdir/etc/onedrive.conf"
  install -Dm644 onedrive.service "$pkgdir/usr/lib/systemd/user/onedrive.service"
}
 
