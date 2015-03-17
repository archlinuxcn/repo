# Maintainer: Gordin <9ordin @t gmail dot com>

pkgname=android-sdk-platform-tools
pkgver=r22
pkgrel=2
pkgdesc='Platform-Tools for Google Android SDK (adb and fastboot)'
arch=('i686' 'x86_64')
url="http://developer.android.com/sdk/index.html"
license=('custom')
depends=('gcc-libs' 'zlib' 'ncurses')
if [[ $CARCH = x86_64 ]]; then
  depends=('lib32-gcc-libs' 'lib32-zlib' 'lib32-ncurses')
fi
provides=('adb')
conflicts=('adb')
_sdk=android-sdk
_tools="opt/${_sdk}/tools"
_ptools="opt/${_sdk}/platform-tools"

source=("https://dl-ssl.google.com/android/repository/platform-tools_${pkgver}-linux.zip"
        "adb.service"
        "license.html")
sha256sums=('8164ae019f54854a8c4230b4a6208c0205f0014f6a141b066146abe6be2b77cd'
            '1c219abea7584ae13f3f76b04e269ef21c1699d6bd29b7615523f927a9d10deb'
            'a7f3a259290ae6a5dc61bd34ecae36e2b7e2f644865ddc3c7fde5d248b8a7cef')

package() {
  install -Dm644 "${srcdir}/adb.service" "${pkgdir}/usr/lib/systemd/system/adb.service"
  install -Dm644 "${srcdir}/license.html" usr/share/licenses/$pkgname/license.html
  cd "$pkgdir"
  mkdir -p opt etc/profile.d
  echo 'export PATH=$PATH:/opt/android-sdk/platform-tools' > etc/profile.d/${pkgname}.sh
  echo 'setenv PATH ${PATH}:/opt/android-sdk/platform-tools' > etc/profile.d/${pkgname}.csh
  chmod 755 etc/profile.d/${pkgname}.{csh,sh}
  mkdir -p opt/$_sdk
  cp -a "$srcdir/platform-tools" "$pkgdir/opt/$_sdk/platform-tools"
  chmod +Xr -R "$pkgdir/opt/$_sdk/platform-tools"
  #chgrp 420 opt/$_sdk
  #chgrp 420 opt/$_sdk/platform-tools
  #chmod g+w opt/$_sdk
  #chmod g+w opt/$_sdk/platform-tools
}
