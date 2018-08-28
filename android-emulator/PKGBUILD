# Maintainer: Zhang Hai <dreaming.in.code.zh@gmail.com>

pkgname=android-emulator
pkgver=27.3.10
pkgrel=1
pkgdesc='Google Android Emulator'
arch=('x86_64')
url='https://developer.android.com/studio/releases/emulator.html'
license=('custom')
depends=('libpulse' 'libx11' 'libxcb' 'libxdamage' 'libxext'
         'libxfixes' 'ncurses5-compat-libs' 'zlib')
install="${pkgname}.install"
source=('https://dl.google.com/android/repository/emulator-linux-4969155.zip'
        "${pkgname}.sh"
        "${pkgname}.csh")
sha1sums=('5b037b25bc6567fda3071457f0009c057670d9e8'
          '4537a7ce30bedf87cedafc2020822219ad58310d'
          '2fb371b5774b67143f0610dfbec4963a4e2f11cc')

package() {

  install -Dm755 "${pkgname}.sh" "${pkgdir}/etc/profile.d/${pkgname}.sh"
  install -Dm755 "${pkgname}.csh" "${pkgdir}/etc/profile.d/${pkgname}.csh"

  rm -rf emulator/lib64/libstdc++

  install -d "${pkgdir}/opt/android-sdk/"
  cp -a emulator "${pkgdir}/opt/android-sdk/"

  # Fix broken permissions
  chmod -R o=g "${pkgdir}/opt/android-sdk/emulator"
  find "${pkgdir}/opt/android-sdk/emulator" -perm 744 -exec chmod 755 {} +
}

# getver: https://developer.android.com/studio/releases/emulator.html
# see https://dl.google.com/android/repository/repository2-1.xml for new versions
# vim:set ts=2 sw=2 et:
