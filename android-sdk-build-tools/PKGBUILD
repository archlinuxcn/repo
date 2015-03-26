# Maintainer: xgdgsc <xgdgsc @t gmail dot com>

pkgname=android-sdk-build-tools
pkgver=r22.0.1
_ver=22.0.1
pkgrel=1
pkgdesc='Build-Tools for Google Android SDK (aapt, aidl, dexdump, dx, llvm-rs-cc)'
arch=('i686' 'x86_64')
url="http://developer.android.com/sdk/index.html"
license=('custom')
depends=('gcc-libs' 'zlib')
optdepends=()

if [[ $CARCH = x86_64 ]]; then
  depends=('lib32-gcc-libs' 'lib32-zlib')
fi

_sdk=android-sdk

source=("https://dl-ssl.google.com/android/repository/build-tools_${pkgver}-linux.zip")
sha1sums=('da8b9c5c3ede39298e6cf0283c000c2ee9029646')
_android=android-5.1
options=('!strip')

package() {
  
  cd "$pkgdir"
  install -Dm644 "${srcdir}/$_android/NOTICE.txt" usr/share/licenses/$pkgname/NOTICE.txt
  # mkdir -p opt etc/profile.d
  # echo 'export PATH=$PATH:/opt/android-sdk/build-tools/'"$_ver/" > etc/profile.d/${pkgname}.sh
  # echo 'setenv PATH ${PATH}:/opt/android-sdk/build-tools/'"$_ver/" > etc/profile.d/${pkgname}.csh
  # chmod 755 etc/profile.d/${pkgname}.{csh,sh}
  
  mkdir -p opt/$_sdk/build-tools/$_ver
  cp -r "$srcdir/$_android/"* "$pkgdir/opt/$_sdk/build-tools/$_ver"
  chmod +Xr -R "$pkgdir/opt/$_sdk/build-tools/$_ver"
}
