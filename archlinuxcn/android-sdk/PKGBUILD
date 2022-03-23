# Maintainer: Hai Zhang <dreaming.in.code.zh@gmail.com>
# Contributor: Alexander F Rødseth <xyproto@archlinux.org>
# Contributor: Daniel Micay <danielmicay@gmail.com>
# Contributor: Gordin <9ordin@gmail.com>

# Finding dependencies:
# ELF dependencies:
# cd /lib/ && find /opt/android-sdk/tools/ -type f -executable \
#   | LANG=C xargs readelf -d 2>/dev/null \
#   | grep -oP '(?<=Shared library: \[).*(?=\])' | LANG=C xargs pacman -Qo \
#   | cut -d' ' -f5 | sort | uniq
# .so in JAR files:
# find /opt/android-sdk/tools/ -type f -exec unzip -l {} 2>&1 \; \
#   | grep -P '^Archive:|\.so$' \
#   | awk 'BEGIN { archive = ""; } { if (NF == 2) { archive = $0; } else { \
#     if (length(archive) > 0) { print archive; archive="" } print $0; } }'
# Note that dependency on libxtst is from swt.

pkgname=android-sdk
pkgver=26.1.1
pkgrel=2
pkgdesc='Google Android SDK'
arch=('x86_64' 'i686')
url='https://developer.android.com/studio/releases/sdk-tools.html'
license=('custom')
depends_i686=('java-environment' 'libxtst' 'fontconfig' 'freetype2' 'gcc-libs'
              'libx11' 'libxext' 'libxrender' 'zlib')
depends_x86_64=('java-environment' 'libxtst' 'fontconfig' 'freetype2'
                'lib32-gcc-libs' 'lib32-glibc' 'libx11' 'libxext' 'libxrender'
                'zlib')
optdepends=('android-emulator: emulator has become standalone since 25.3.0'
            'android-sdk-platform-tools: adb, aapt, aidl, dexdump and dx'
            'android-udev: udev rules for Android devices')
install="${pkgname}.install"
source=('https://dl.google.com/android/repository/sdk-tools-linux-4333796.zip'
        "${pkgname}.sh"
        "${pkgname}.csh"
        "${pkgname}.conf"
        'license.html')
sha1sums=('8c7c28554a32318461802c1291d76fccfafde054'
          'bc48fea40da956ce4d1afdd7e8d378f5b120e65c'
          '71bfc50d6b0ea1650c981b24f358020ad2ca7bd6'
          '145bdf3eb41a56574b289c1577a24bc47097ec83'
          'bfb91be7e0b602d765b7a1fcaf0ce1b7e1a93faa')

package() {

  install -Dm755 "${pkgname}.sh" "${pkgdir}/etc/profile.d/${pkgname}.sh"
  install -Dm755 "${pkgname}.csh" "${pkgdir}/etc/profile.d/${pkgname}.csh"
  install -Dm644 "${pkgname}.conf" "${pkgdir}/etc/ld.so.conf.d/${pkgname}.conf"
  install -Dm644 license.html "${pkgdir}/usr/share/licenses/${pkgname}/license.html"
  install -d "${pkgdir}/opt/${pkgname}/platforms"
  install -d "${pkgdir}/opt/${pkgname}/add-ons"

  cp -a tools "${pkgdir}/opt/${pkgname}"

  if [[ $CARCH = i686 ]]; then
    rm -rf "${pkgdir}"/opt/android-sdk/tools/lib/{monitor-,}x86_64
  fi

  # Fix broken permissions
  chmod -R o=g "${pkgdir}/opt/${pkgname}"
  find "${pkgdir}/opt/${pkgname}" -perm 744 -exec chmod 755 {} +
}

# getver: https://developer.android.com/studio/releases/sdk-tools.html
# see https://dl.google.com/android/repository/repository2-1.xml for new versions
# vim:set ts=2 sw=2 et:
