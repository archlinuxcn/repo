# Maintainer: xgdgsc <xgdgsc @t gmail dot com>

pkgname=android-sdk-build-tools
_ver=28.0.3
pkgver=r$_ver
pkgrel=1
pkgdesc='Build-Tools for Google Android SDK (aapt, aidl, dexdump, dx, llvm-rs-cc)'
arch=('i686' 'x86_64')
url="https://developer.android.com/studio/releases/build-tools"
license=('custom')
depends_i686=('gcc-libs' 'zlib')
optdepends=()
depends_x86_64=('lib32-gcc-libs' 'lib32-zlib')
_sdk=android-sdk

source=("https://dl-ssl.google.com/android/repository/build-tools_${pkgver}-linux.zip")
sha1sums=('ea6f2f7103cd9da9ff0bdf6e37fbbba548fa4165')
_android=android-9
options=('!strip')

package() {

  cd "$pkgdir"
  install -Dm644 "${srcdir}/$_android/NOTICE.txt" usr/share/licenses/$pkgname/NOTICE.txt
  # mkdir -p opt etc/profile.d
  # echo 'export PATH=$PATH:/opt/android-sdk/build-tools/'"$_ver/" > etc/profile.d/${pkgname}.sh
  # echo 'setenv PATH ${PATH}:/opt/android-sdk/build-tools/'"$_ver/" > etc/profile.d/${pkgname}.csh
  # chmod 755 etc/profile.d/${pkgname}.{csh,sh}
  ver=$(cat "${srcdir}/$_android/source.properties" |grep ^Pkg.Revision=|sed 's/Pkg.Revision=\([0-9.]*\).*/\1/')
  mkdir -p opt/$_sdk/build-tools/$ver
  cp -r "$srcdir/$_android/"* "$pkgdir/opt/$_sdk/build-tools/$ver"
  chmod +Xr -R "$pkgdir/opt/$_sdk/build-tools/$ver"
}
