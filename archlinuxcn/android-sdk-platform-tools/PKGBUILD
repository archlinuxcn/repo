# Maintainer: Hai Zhang <dreaming.in.code.zh@gmail.com>
# Contributor: Vlad M. <vlad@archlinux.net>
# Contributor: Gordin <9ordin @t gmail dot com>
# Contributor: Christoph Bayer <chrbayer@criby.de>

pkgname=android-sdk-platform-tools
pkgver=35.0.0
pkgrel=1
pkgdesc='Platform-Tools for Google Android SDK (adb and fastboot)'
arch=('x86_64')
url='http://developer.android.com/sdk/index.html'
license=('custom')
depends=('zlib' 'ncurses')
provides=('adb' 'android-tools')
conflicts=('adb')
install="${pkgname}.install"
source=("https://dl.google.com/android/repository/platform-tools_r${pkgver}-linux.zip"
        'adb.service'
        'license.html'
        'package.xml')
sha1sums=('03b781f9ed812a7219d4bd5e8df3b61dc97b347a'
          '49a40c129199844603afe71fce69c0908e062393'
          'bfb91be7e0b602d765b7a1fcaf0ce1b7e1a93faa'
          '87be28d028765cc090451a8f4311de215c3683a0')

package() {
  install -Dm644 "${srcdir}/adb.service" "${pkgdir}/usr/lib/systemd/system/adb.service"
  install -Dm644 "${srcdir}/license.html" "${pkgdir}/usr/share/licenses/${pkgname}/license.html"

  install -d "${pkgdir}/etc/profile.d"
  echo 'export PATH="${PATH}:/opt/android-sdk/platform-tools"' >"${pkgdir}/etc/profile.d/${pkgname}.sh"
  echo 'setenv PATH "${PATH}:/opt/android-sdk/platform-tools"' >"${pkgdir}/etc/profile.d/${pkgname}.csh"
  chmod 755 "${pkgdir}/etc/profile.d/${pkgname}".{csh,sh}

  install -d "${pkgdir}/opt/android-sdk/"
  cp -a "${srcdir}/platform-tools" "${pkgdir}/opt/android-sdk/platform-tools"
  chmod -R +rX "${pkgdir}/opt/android-sdk/platform-tools"
  install -Dm755 'package.xml' "${pkgdir}/opt/android-sdk/platform-tools/package.xml"
}
