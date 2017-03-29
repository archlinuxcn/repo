# Maintainer: Vlad M. <vlad@archlinux.net>
# Contributor: Gordin <9ordin @t gmail dot com>
# Contributor: Christoph Bayer <chrbayer@criby.de>

pkgname=android-sdk-platform-tools
pkgver=r25.0.4
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
sha256sums=('79048c41f69e730800d4fb710f6128691b7b8dfcb3a280e6b4e112a6f9285cbf'
            '1c219abea7584ae13f3f76b04e269ef21c1699d6bd29b7615523f927a9d10deb'
            'a7f3a259290ae6a5dc61bd34ecae36e2b7e2f644865ddc3c7fde5d248b8a7cef'
            'd50cd65551230298a7c1d4c29552aecd35d2c99270d22ba4ce6b4ff3d6f9ecf1')

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
