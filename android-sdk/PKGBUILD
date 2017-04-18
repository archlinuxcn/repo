# Maintainer: Zhang Hai <dreaming.in.code.zh@gmail.com>
# Contributor: Alexander F Rødseth <xyproto@archlinux.org>
# Contributor: Daniel Micay <danielmicay@gmail.com>
# Contributor: Gordin <9ordin@gmail.com>

pkgname=android-sdk
pkgver=26.0.1
pkgrel=1
pkgdesc='Google Android SDK'
arch=('x86_64' 'i686')
url='https://developer.android.com/studio/releases/sdk-tools.html'
license=('custom')
depends_x86_64=('java-environment' 'lib32-alsa-lib' 'lib32-openal'
  'lib32-libstdc++5' 'lib32-libxv' 'lib32-mesa' 'lib32-ncurses' 'lib32-sdl'
  'lib32-zlib' 'lib32-fontconfig' 'lib32-libpulse' 'swt')
depends_i686=('java-environment' 'alsa-lib' 'openal' 'libstdc++5' 'libxv' 'sdl'
              'ncurses' 'swt' 'zlib')
install="${pkgname}.install"
optdepends=('android-udev: udev rules for Android devices'
            'android-sdk-platform-tools: adb, aapt, aidl, dexdump and dx')
source=('https://dl.google.com/android/repository/sdk-tools-linux-3859397.zip'
        'android.png.txt::https://android.googlesource.com/platform/tools/base/+/studio-master-dev/templates/gradle-projects/NewAndroidModule/root/res/mipmap-xxxhdpi/ic_launcher.png?format=TEXT'
        "${pkgname}.desktop"
        "${pkgname}.sh"
        "${pkgname}.csh"
        "${pkgname}.conf"
        'license.html')
sha1sums=('7eab0ada7ff28487e1b340cc3d866e70bcb4286e'
          '57f405807d1fb3fa09577df56854f0116a912026'
          '8f886de363ad91a7f93a0c6ded993e99bef3e1a7'
          '30a6ed281d54f8b7be08663a18c367f79c0d8d47'
          '1bd09bf137fd09171cb426daa5748f117cfb3c25'
          '145bdf3eb41a56574b289c1577a24bc47097ec83'
          'bfb91be7e0b602d765b7a1fcaf0ce1b7e1a93faa')

package() {

  install -Dm755 "${pkgname}.sh" "${pkgdir}/etc/profile.d/${pkgname}.sh"
  install -Dm755 "${pkgname}.csh" "${pkgdir}/etc/profile.d/${pkgname}.csh"
  install -Dm644 "${pkgname}.conf" "${pkgdir}/etc/ld.so.conf.d/${pkgname}.conf"
  base64 -d android.png.txt >android.png
  install -Dm644 android.png "${pkgdir}/usr/share/pixmaps/${pkgname}.png"
  install -Dm644 "${pkgname}.desktop" \
    "${pkgdir}/usr/share/applications/${pkgname}.desktop"
  install -Dm644 license.html \
    "${pkgdir}/usr/share/licenses/${pkgname}/license.html"
  install -d "${pkgdir}/opt/${pkgname}/platforms"
  install -d "${pkgdir}/opt/${pkgname}/add-ons"

  cp -a tools "${pkgdir}/opt/${pkgname}"

  if [[ $CARCH = i686 ]]; then
    rm -rf \
      "${pkgdir}"/opt/android-sdk/tools/lib/{monitor-,}x86_64 \
      "${pkgdir}"/opt/android-sdk/tools/lib/lib64* \
      "${pkgdir}"/opt/android-sdk/tools/emulator64-*
  fi

  # Fix broken permissions
  chmod -R o=g "${pkgdir}/opt/${pkgname}"
  find "${pkgdir}/opt/${pkgname}" -perm 744 -exec chmod 755 {} +

  # Remove libstd* from the tools directory
  find "${pkgdir}/opt/${pkgname}/tools" -name "libstd*" -type f -delete
}

# getver: https://developer.android.com/studio/releases/sdk-tools.html
# see https://dl.google.com/android/repository/repository2-1.xml for new versions
# vim:set ts=2 sw=2 et:
