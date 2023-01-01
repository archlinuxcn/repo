# Maintainer: Peter Cai <peter at typeblog dot net>

pkgname=unciv
_pkgname=Unciv
_gradle_ver=7.2 # This package does not work with system gradle
pkgver=4.3.15.REL
_pkgver=${pkgver%.*}-${pkgver##*.}
_pkgver=$(echo $_pkgver | sed -r 's/-([0-9]+)/-patch\1/g')
_pkgver=${_pkgver/-REL/}
pkgrel=1
_srcdir=$_pkgname-$_pkgver
pkgdesc="Open-source remake of Civilization V"
url="https://github.com/yairm210/Unciv"
license=('MPL-2.0')
depends=('jdk11-openjdk' 'bash' 'xorg-xrandr')
arch=('any')
source=(
  "https://github.com/yairm210/Unciv/archive/$_pkgver.zip"
  "https://services.gradle.org/distributions/gradle-$_gradle_ver-bin.zip"
  "$_pkgname.sh"
  "$pkgname.desktop"
)
noextract=("gradle-$_gradle_ver-bin.zip")
md5sums=('65ded9a42db0ccd8d5b975cf6a99b277'
         'b5fb25beea6f974e2a5198e079174cd6'
         'e6d812078de30b33ab4698a53118b773'
         '42d5f7ea8ee48d2d643d070786f039ba')

prepare() {
  # Use gradle downloaded by our pkgbuild to allow caching
  sed -i "6s|https\\\://services.gradle.org/distributions|../../../|" $_srcdir/gradle/wrapper/gradle-wrapper.properties
  # Get rid of the Android part (it somehow always asks for Android SDK)
  gawk -i inplace 'BEGIN { doPrint = 1; } /project\(":android"\) {/ { doPrint = 0; } /^}$/ { if (doPrint != 1) { doPrint = 1; next }} { if (doPrint) print $0;}' $_srcdir/build.gradle.kts
  # We cannot just get rid of the android/ folder becuase we need assets from it
  rm -rf $_srcdir/android/{res,src,build.gradle.kts,gradle.properties,project.properties}
}

build() {
  cd $_srcdir
  unset _JAVA_OPTIONS
  export PATH=/usr/lib/jvm/java-11-openjdk/bin/:$PATH
  GRADLE_USER_HOME="$srcdir" ./gradlew desktop:dist
}

package() {
  install -Dm755 $_pkgname.sh "$pkgdir/usr/bin/$_pkgname"
  install -Dm644 $pkgname.desktop "$pkgdir/usr/share/applications/$pkgname.desktop"
  install -Dm644 $_srcdir/extraImages/Icons/"Unciv icon v6.png" "$pkgdir/usr/share/pixmaps/unciv.png"
  install -Dm644 $_srcdir/desktop/build/libs/$_pkgname.jar "$pkgdir/usr/share/$_pkgname/$_pkgname.jar"
}
