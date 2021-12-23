# Maintainer: Peter Cai <peter at typeblog dot net>
# Thanks: Kevin MacMartin <prurigro at gmail dot com>

pkgname=shattered-pixel-dungeon
_pkgname=$pkgname
pkgver=1.1.1.REL
_pkgver=${pkgver%.*}${pkgver##*.}
_pkgver=${_pkgver/REL/}
_srcdir=$_pkgname-$_pkgver
pkgrel=1
pkgdesc='Shattered fork of the popular rogue-like game'
url='https://shatteredpixel.com/'
license=('GPL3')
depends=('jre11-openjdk' 'bash' 'xorg-xrandr')
makedepends=('gradle' 'jdk11-openjdk')
conflicts=('shattered-pixel-dungeon-git')
arch=('any')
source=(
  "https://github.com/00-Evan/shattered-pixel-dungeon/archive/v$_pkgver.tar.gz"
  "$pkgname.sh"
  "$pkgname.desktop"
)
sha512sums=('663ab501d9994441605928867d90bf41f821ad1fa555bb6586fe874eb9952f237dcdd9b1367684a56738bbe11ecb1b01cdaa661d097b9ef22d04a3ce8807d7d3'
            'b0218d4189cee0d4bb4109fa671a0a535715a58e91dd6dc0c364a57db948c818b3ad5e29bbbbf14c245bcf83fecb7588b80f250235b87e87051b380bc7cef34c'
            '204a7bcedbbc14bdad6586e4b759b326191a7fd2c344dadc7032495d4caa5fe32edac4118d7294229a6fe24f6684416fff37e260bbc9dde9e50846a03ba77db8')

build() {
  cd $_srcdir
  unset _JAVA_OPTIONS
  # Force the system to build the package using JDK8
  export PATH=/usr/lib/jvm/java-11-openjdk/jre/bin/:$PATH
  GRADLE_USER_HOME="$srcdir" gradle desktop:release
}

package() {
  install -Dm755 $pkgname.sh "$pkgdir/usr/bin/$pkgname"
  install -Dm644 $pkgname.desktop "$pkgdir/usr/share/applications/$pkgname.desktop"
  install -Dm644 $_srcdir/android/src/main/res/mipmap-xxxhdpi/ic_launcher.png "$pkgdir/usr/share/pixmaps/$pkgname.png"
  install -Dm644 $_srcdir/desktop/build/libs/desktop-*.jar "$pkgdir/usr/share/$pkgname/$pkgname.jar"
}
