#Maintainer: danyf90 <daniele.formichelli@gmail.com>
#Co-Maintainer: syncrtl64 <syncrtl64@gmail.com>
#Contributor: Andrea Cattaneo <andrea.cattaneo.dev@gmail.com>

pkgname=genymotion
pkgver=2.8.0
pkgrel=2
pkgdesc="Complete set of tools that provides a virtual environment for Android."
arch=('x86_64')
url="http://www.genymotion.com/"
depends=('ffmpeg-compat' 'gstreamer0.10' 'gstreamer0.10-base' 'libpng' 'net-tools' 'protobuf' 'qca' 'qt5-script' 'qt5-webkit' 'virtualbox')
install=$pkgname.install
license=('custom')
_ARCH="x64"
source=("genymotion.desktop"
        "genymotion-player.desktop"
        "https://dl.genymotion.com/releases/genymotion-$pkgver/$pkgname-${pkgver}-linux_$_ARCH.bin")
sha512sums=('48e9bafe1d64b688c51eceb8d129f44d690060ff9a6d82eefcf3295f7834516ce62439faf4f4454287f594fc410aafbafd30a43537ea3d295c42bee8e4e03ac7'
            '92286b54b4dfa68b4400ab4c72717c091fe6ea7e9142ef1cfebabe801e682f2a217a443c5990cf2b59f7fa5a4bc22484e8f11b0071766f689363d74d19cbe840'
            '3e45ffe6904032128e0bc251ac1657b06874f686d4281fad8418f37216ebcb19298eb3456bb96025d081a8af3322731858c1595836a3e9a9531e394f719277f6')

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
