# Maintainer: Peter Cai <peter at typeblog dot net>

pkgname=unciv
_pkgname=Unciv
_gradle_ver=5.6.4 # This package does not work with system gradle
pkgver=3.6.11.REL
_pkgver=${pkgver%.*}-patch${pkgver##*.}
_pkgver=${_pkgver/-patchREL/}
pkgrel=1
_srcdir=$_pkgname-$_pkgver
pkgdesc="Open-source remake of Civilization V"
url="https://github.com/yairm210/Unciv"
license=('MPL-2.0')
depends=('jre8-openjdk' 'bash' 'xorg-xrandr')
makedepends=('jdk8-openjdk')
arch=('any')
source=(
  "https://github.com/yairm210/Unciv/archive/$_pkgver.zip"
  "https://services.gradle.org/distributions/gradle-$_gradle_ver-all.zip"
  "$_pkgname.sh"
  "$pkgname.desktop"
)
noextract=("gradle-$_gradle_ver-all.zip")
md5sums=('d50bcbec27eb077841a4ed17bfd2f9f4'
         '9fc6bd2c1bf6f18f5620bca5c19e3c05'
         'f8eab098f20681b8db232cc5709713d3'
         '42d5f7ea8ee48d2d643d070786f039ba')

prepare() {
  # Use gradle downloaded by our pkgbuild to allow caching
  sed -i "6s|https\\\://services.gradle.org/distributions|../../../|" $_srcdir/gradle/wrapper/gradle-wrapper.properties
}

build() {
  cd $_srcdir
  unset _JAVA_OPTIONS
  export PATH=/usr/lib/jvm/java-8-openjdk/jre/bin/:$PATH
  GRADLE_USER_HOME="$srcdir" ./gradlew desktop:dist
}

package() {
  install -Dm755 $_pkgname.sh "$pkgdir/usr/bin/$_pkgname"
  install -Dm644 $pkgname.desktop "$pkgdir/usr/share/applications/$pkgname.desktop"
  install -Dm644 $_srcdir/extraImages/"Unciv icon v4.png" "$pkgdir/usr/share/pixmaps/unciv.png"
  install -Dm644 $_srcdir/desktop/build/libs/$_pkgname.jar "$pkgdir/usr/share/$_pkgname/$_pkgname.jar"
}
