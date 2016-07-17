# Maintainer: Alexander F Rødseth <xyproto@archlinux.org>
# Contributor: Daniel Micay <danielmicay@gmail.com>
# Contributor: Gordin <9ordin@gmail.com>

pkgname=android-sdk
pkgver=25.1.7
pkgrel=3
pkgdesc='Google Android SDK'
arch=('x86_64' 'i686')
url='http://developer.android.com/sdk/'
license=('custom')
depends_x86_64=('java-environment' 'lib32-alsa-lib' 'lib32-openal'
  'lib32-libstdc++5' 'lib32-libxv' 'lib32-mesa' 'lib32-ncurses' 'lib32-sdl'
  'lib32-zlib' 'lib32-fontconfig' 'lib32-libpulse' 'swt' 'ncurses5-compat-libs')
depends_i686=('java-environment' 'alsa-lib' 'openal' 'libstdc++5' 'libxv' 'sdl'
              'ncurses' 'swt' 'zlib' 'ncurses5-compat-libs')
install="$pkgname.install"
optdepends=('android-udev: udev rules for Android devices'
            'android-sdk-platform-tools: adb, aapt, aidl, dexdump and dx')
source=("https://dl.google.com/android/repository/tools_r${pkgver}-linux.zip"
        'https://source.android.com/source/images/Android_Robot_100.png'
        "$pkgname.desktop"
        "$pkgname.sh"
        "$pkgname.csh"
        "$pkgname.conf"
        'license.html')
sha1sums=('36869e6c81cda18f862959a92301761f81bc06b8'
          'f359ac923ed008dae3a007a513d26cfbaf025626'
          '8f886de363ad91a7f93a0c6ded993e99bef3e1a7'
          'ab7251df3a382a920e81663f25d4a7813918ae1c'
          '5430d75f38ff74667919efc13f380bef0d67e8ff'
          '145bdf3eb41a56574b289c1577a24bc47097ec83'
          'bfb91be7e0b602d765b7a1fcaf0ce1b7e1a93faa')

package() {
  install -Dm755 "$pkgname.sh" "$pkgdir/etc/profile.d/$pkgname.sh"
  install -Dm755 "$pkgname.csh" "$pkgdir/etc/profile.d/$pkgname.csh"
  install -Dm644 "$pkgname.conf" "$pkgdir/etc/ld.so.conf.d/$pkgname.conf"
  install -Dm644 Android_Robot_100.png "$pkgdir/usr/share/pixmaps/$pkgname.png"
  install -Dm644 "$pkgname.desktop" \
    "$pkgdir/usr/share/applications/$pkgname.desktop"
  install -Dm644 license.html \
    "$pkgdir/usr/share/licenses/$pkgname/license.html"
  install -d "$pkgdir/opt/$pkgname/platforms"
  install -d "$pkgdir/opt/$pkgname/add-ons"

  cp -a tools "$pkgdir/opt/$pkgname"

  if [[ $CARCH = i686 ]]; then
    rm -rf \
      "${pkgdir}"/opt/android-sdk/tools/lib/{monitor-,}x86_64 \
      "${pkgdir}"/opt/android-sdk/tools/lib/lib64* \
      "${pkgdir}"/opt/android-sdk/tools/emulator64-*
  fi

  # Fix broken permissions
  chmod -R o=g "$pkgdir/opt/$pkgname"
  find "$pkgdir/opt/$pkgname" -perm 744 -exec chmod 755 {} +

  # Remove libstd* from the tools directory
  for kw in libstd; do
    find "$pkgdir/opt/$pkgname/tools" -name "$kw*" -type f -delete
  done
}

# getver: developer.android.com/tools/sdk/tools-notes.html
# see https://dl.google.com/android/repository/repository-11.xml for new versions
# vim:set ts=2 sw=2 et:
