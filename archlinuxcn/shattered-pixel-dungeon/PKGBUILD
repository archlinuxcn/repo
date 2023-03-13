# Maintainer: Peter Cai <peter at typeblog dot net>
# Thanks: Kevin MacMartin <prurigro at gmail dot com>

pkgname=shattered-pixel-dungeon
_pkgname=$pkgname
pkgver=2.0.0.REL
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
sha512sums=('dba90e2c340e0d8ea24b5ade30f888dc83c2dc1784b5a3102206968f5d1958008a77ce3c98bac75ccf8345e818081ad71506ec7dc63a7aa6946b750c0a8be569'
            'a601d3bf570396f2038b0221825d8c432748e08ea336c3b64dd6ff048c81f0bd271acc8b0d7d4b298b5085ee6bd6770e5845089085756dcda9a5b69cb7569265'
            '204a7bcedbbc14bdad6586e4b759b326191a7fd2c344dadc7032495d4caa5fe32edac4118d7294229a6fe24f6684416fff37e260bbc9dde9e50846a03ba77db8')

build() {
  cd $_srcdir
  unset _JAVA_OPTIONS
  # Force the system to build the package using JDK11
  export PATH=/usr/lib/jvm/java-11-openjdk/bin/:$PATH
  GRADLE_USER_HOME="$srcdir" gradle desktop:release
}

package() {
  install -Dm755 $pkgname.sh "$pkgdir/usr/bin/$pkgname"
  install -Dm644 $pkgname.desktop "$pkgdir/usr/share/applications/$pkgname.desktop"
  install -Dm644 $_srcdir/android/src/main/res/mipmap-xxxhdpi/ic_launcher.png "$pkgdir/usr/share/pixmaps/$pkgname.png"
  install -Dm644 $_srcdir/desktop/build/libs/desktop-*.jar "$pkgdir/usr/share/$pkgname/$pkgname.jar"
}
