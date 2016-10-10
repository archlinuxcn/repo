# Maintainer: Vlad M. <vlad@archlinux.net>
# Contributor: Gordin <9ordin @t gmail dot com>
# Contributor: Christoph Bayer <chrbayer@criby.de>

pkgname=android-sdk-platform-tools
pkgver=r24.0.3
pkgrel=1
pkgdesc='Platform-Tools for Google Android SDK (adb and fastboot)'
arch=('x86_64')
url="http://developer.android.com/sdk/index.html"
license=('custom')
depends_x86_64=('zlib' 'ncurses')
provides=('adb' 'android-tools')
conflicts=('adb')
install=$pkgname.install
_sdk="android-sdk"
_tools="opt/${_sdk}/tools"
_ptools="opt/${_sdk}/platform-tools"

source=("https://dl-ssl.google.com/android/repository/platform-tools_${pkgver}-linux.zip"
        "adb.service"
        "license.html"
        "source.properties")
sha256sums=('b8d833f4eea1a730e12339e9ceab3c25c625ad1fc9226a282121d6ea427c5b96'
            '1c219abea7584ae13f3f76b04e269ef21c1699d6bd29b7615523f927a9d10deb'
            'a7f3a259290ae6a5dc61bd34ecae36e2b7e2f644865ddc3c7fde5d248b8a7cef'
            '08e921dee35079773ac01b3b3cb802b1a1cbd292c904f8e7a659932fa96c8f72')

package() {
  install -Dm644 "${srcdir}/adb.service" "${pkgdir}/usr/lib/systemd/system/adb.service"
  install -Dm644 "${srcdir}/license.html" "usr/share/licenses/$pkgname/license.html"
  cd "$pkgdir"
  mkdir -p opt etc/profile.d
  echo 'export PATH=$PATH:/opt/android-sdk/platform-tools' > "etc/profile.d/${pkgname}.sh"
  echo 'setenv PATH ${PATH}:/opt/android-sdk/platform-tools' > "etc/profile.d/${pkgname}.csh"
  chmod 755 "etc/profile.d/${pkgname}".{csh,sh}
  mkdir -p "opt/$_sdk"
  cp -a "$srcdir/platform-tools" "$pkgdir/opt/$_sdk/platform-tools"
  install -m644 "${srcdir}/source.properties" "${pkgdir}/opt/android-sdk/platform-tools/source.properties"
  chmod +Xr -R "$pkgdir/opt/$_sdk/platform-tools"
}
