#Maintainer: danyf90 <daniele.formichelli@gmail.com>
#Co-Maintainer: syncrtl64 <syncrtl64@gmail.com>
#Contributor: Andrea Cattaneo <andrea.cattaneo.dev@gmail.com>

pkgname=genymotion
pkgver=2.10.0
pkgrel=1
pkgdesc="Complete set of tools that provides a virtual environment for Android."
arch=('x86_64')
url="http://www.genymotion.com/"
depends=('libpng' 'net-tools' 'protobuf' 'qca-qt5' 'qt5-script' 'qt5-webkit' 'virtualbox')
install=$pkgname.install
license=('custom')
_ARCH="x64"
source=("genymotion.desktop"
        "genymotion-player.desktop"
        "https://dl.genymotion.com/releases/genymotion-$pkgver/$pkgname-${pkgver}-linux_$_ARCH.bin")
sha512sums=('48e9bafe1d64b688c51eceb8d129f44d690060ff9a6d82eefcf3295f7834516ce62439faf4f4454287f594fc410aafbafd30a43537ea3d295c42bee8e4e03ac7'
            'fabbccd65c22c2dc26b32a847c9fa81d4b7d3e2a13e976cd01c1517654e4bd7e4eac485152dbe8e97b1953ffda62f40e99223a76d24f0c8dfc6530fe3908b665'
            'fe89376a48121b9c3cb1392d7365e13ee2865b795b1d8712e3461072bd0e0d38fd309814d7ecd5518fe2673229fb2e49b4c239211f4308f1057f3d01052d4007')

package(){
  cd $srcdir

  install -d $pkgdir/opt
  yes | bash ./$pkgname-${pkgver}-linux_$_ARCH.bin -d $pkgdir/opt

  install -d $pkgdir/usr/bin
  ln -s /opt/genymotion/genymotion $pkgdir/usr/bin/genymotion
  ln -s /opt/genymotion/genymotion-shell $pkgdir/usr/bin/genymotion-shell
  ln -s /opt/genymotion/player $pkgdir/usr/bin/genymotion-player
  ln -s /opt/genymotion/gmtool $pkgdir/usr/bin/gmtool
  install -Dm644 $srcdir/genymotion.desktop $pkgdir/usr/share/applications/genymotion.desktop
  install -Dm644 $srcdir/genymotion-player.desktop $pkgdir/usr/share/applications/genymotion-player.desktop
  chown -R root:root $pkgdir/opt/genymotion
}
