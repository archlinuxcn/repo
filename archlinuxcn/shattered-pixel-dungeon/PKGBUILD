# Maintainer: Peter Cai <peter at typeblog dot net>
# Thanks: Kevin MacMartin <prurigro at gmail dot com>

pkgname=shattered-pixel-dungeon
_pkgname=$pkgname-gdx
pkgver=0.7.5.REL
_pkgver=${pkgver%.*}${pkgver##*.}
_pkgver=${_pkgver/REL/}
_srcdir=$_pkgname-$_pkgver
pkgrel=1
pkgdesc='Shattered fork of the popular rogue-like game'
url='https://shatteredpixel.com/'
license=('GPL3')
depends=('jre8-openjdk' 'bash' 'xorg-xrandr')
makedepends=('gradle' 'jdk8-openjdk')
conflicts=('shattered-pixel-dungeon-git')
arch=('any')
source=(
  "https://github.com/00-Evan/shattered-pixel-dungeon-gdx/archive/v$_pkgver.tar.gz"
  "$pkgname.sh"
  "$pkgname.desktop"
)
sha512sums=('e7d168a036a398845960954b6527eb92debd9a6c29e3c25be7a32d3957d0eba587598e8625adb688810b489dc7099bbe836d2b349cbfef7134abec5b77630363'
            '586ac3e1357495434e318dbda539792565a423ca59768b4e1aee8c81764ad6daea75365b4714fdac76a098b0ffc42da91cf5f2a5ab83fa0dc1beb7abf99f2607'
            '204a7bcedbbc14bdad6586e4b759b326191a7fd2c344dadc7032495d4caa5fe32edac4118d7294229a6fe24f6684416fff37e260bbc9dde9e50846a03ba77db8')

prepare() {
  # Hack to use system gradle (thanks to @jonathon on AUR)
  sed -i '164c/usr/bin/gradle "$@"' "$_srcdir"/gradlew
}

build() {
  cd $_srcdir
  unset _JAVA_OPTIONS
  # Force the system to build the package using JDK8
  export PATH=/usr/lib/jvm/java-8-openjdk/jre/bin/:$PATH
  GRADLE_USER_HOME="$srcdir" ./gradlew desktop:dist
}

package() {
  install -Dm755 $pkgname.sh "$pkgdir/usr/bin/$pkgname"
  install -Dm644 $pkgname.desktop "$pkgdir/usr/share/applications/$pkgname.desktop"
  install -Dm644 $_srcdir/android/res/drawable-xxxhdpi/ic_launcher.png "$pkgdir/usr/share/pixmaps/$pkgname.png"
  install -Dm644 $_srcdir/desktop/build/libs/desktop-*.jar "$pkgdir/usr/share/$pkgname/$pkgname.jar"
}
