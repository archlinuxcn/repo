# Maintainer: Hai Zhang <dreaming.in.code.zh@gmail.com>

pkgname=android-emulator
pkgver=31.2.8
pkgrel=1
pkgdesc='Google Android Emulator'
arch=('x86_64')
url='https://developer.android.com/studio/releases/emulator.html'
license=('custom')
depends=('alsa-lib' 'dbus' 'expat' 'gcc-libs' 'glibc' 'libpulse'
         'libutil-linux' 'libx11' 'libxcb' 'libxcomposite' 'libxcursor'
         'libxdamage' 'libxext' 'libxfixes' 'libxi' 'libxrender' 'libxtst'
         'nspr' 'nss' 'zlib')
install="${pkgname}.install"
source=('https://dl.google.com/android/repository/emulator-linux_x64-8143646.zip'
        "${pkgname}.sh"
        "${pkgname}.csh"
        'package.xml')
sha1sums=('a87b73425e697d40721ad128155a0596a3d6b949'
          '80c9b3ffc8865b5f8e55b1ffed36c08ee7a9d8ad'
          'e1485ef14463f275005cae43a0a1e43ce52354ca'
          'db3507d8e8a010ceeef64ae417c38848466485a5')

package() {
  install -Dm755 "${pkgname}.sh" "${pkgdir}/etc/profile.d/${pkgname}.sh"
  install -Dm755 "${pkgname}.csh" "${pkgdir}/etc/profile.d/${pkgname}.csh"

  install -d "${pkgdir}/opt/android-sdk/"
  cp -a emulator "${pkgdir}/opt/android-sdk/"
  install -Dm755 'package.xml' "${pkgdir}/opt/android-sdk/emulator/package.xml"

  # Fix broken permissions
  chmod -R o=g "${pkgdir}/opt/android-sdk/emulator"
  find "${pkgdir}/opt/android-sdk/emulator" -perm 744 -exec chmod 755 {} +
}

# getver: https://developer.android.com/studio/releases/emulator.html
# see https://dl.google.com/android/repository/repository2-1.xml for new versions
# vim:set ts=2 sw=2 et:
