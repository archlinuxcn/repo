#Maintainer: danyf90 <daniele.formichelli@gmail.com>
#Co-Maintainer: syncrtl64 <syncrtl64@gmail.com>
#Contributor: Andrea Cattaneo <andrea.cattaneo.dev@gmail.com>

pkgname=genymotion
pkgver=2.8.1
pkgrel=4
pkgdesc="Complete set of tools that provides a virtual environment for Android."
arch=('x86_64')
url="http://www.genymotion.com/"
depends=('libpng' 'net-tools' 'protobuf' 'qca' 'qt5-script' 'qt5-webkit' 'virtualbox')
install=$pkgname.install
license=('custom')
_ARCH="x64"
source=("genymotion.desktop"
        "genymotion-player.desktop"
        "https://dl.genymotion.com/releases/genymotion-$pkgver/$pkgname-${pkgver}_$_ARCH.bin")
sha512sums=('48e9bafe1d64b688c51eceb8d129f44d690060ff9a6d82eefcf3295f7834516ce62439faf4f4454287f594fc410aafbafd30a43537ea3d295c42bee8e4e03ac7'
            'fabbccd65c22c2dc26b32a847c9fa81d4b7d3e2a13e976cd01c1517654e4bd7e4eac485152dbe8e97b1953ffda62f40e99223a76d24f0c8dfc6530fe3908b665'
            '8ca4f46e983ffa2a19c21e961b6638af859f7635bd3a976c0b5709622a536569c81ccf3b08f52f0016e37990d83b1fd38cc86c9dbb5599e727fd48558567dfa7')

package(){
  cd $srcdir

  install -d $pkgdir/opt
  yes | bash ./$pkgname-${pkgver}_$_ARCH.bin -d $pkgdir/opt

  install -d $pkgdir/usr/bin
  ln -s /opt/genymotion/genymotion $pkgdir/usr/bin/genymotion
  ln -s /opt/genymotion/genymotion-shell $pkgdir/usr/bin/genymotion-shell
  ln -s /opt/genymotion/player $pkgdir/usr/bin/genymotion-player
  ln -s /opt/genymotion/gmtool $pkgdir/usr/bin/gmtool
  install -Dm644 $srcdir/genymotion.desktop $pkgdir/usr/share/applications/genymotion.desktop
  install -Dm644 $srcdir/genymotion-player.desktop $pkgdir/usr/share/applications/genymotion-player.desktop
  chown -R root:root $pkgdir/opt/genymotion
  rm $pkgdir/opt/genymotion/libdrm.so.2
  rm $pkgdir/opt/genymotion/libxcb.so.1

}
