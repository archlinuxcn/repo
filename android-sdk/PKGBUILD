# Maintainer: Alexander Rødseth <rodseth@gmail.com>
# Contributor: Daniel Micay <danielmicay@gmail.com>
# Contributor: Gordin <9ordin @t gmail dot com>

pkgname=android-sdk
pkgver=24.3.3
pkgrel=2
pkgdesc='Google Android SDK'
arch=('x86_64' 'i686')
url='http://developer.android.com/sdk/'
license=('custom')
depends_x86_64=('java-environment' 'lib32-alsa-lib' 'lib32-openal'
  'lib32-libstdc++5' 'lib32-libxv' 'lib32-mesa' 'lib32-ncurses' 'lib32-sdl'
  'lib32-zlib' 'swt')
depends_i686=('java-environment' 'alsa-lib' 'openal' 'libstdc++5' 'libxv' 'sdl'
              'ncurses' 'swt' 'zlib')
install="$pkgname.install"
optdepends=('android-udev: udev rules for Android devices'
            'android-sdk-platform-tools: adb, aapt, aidl, dexdump and dx')
source=("https://dl-ssl.google.com/android/repository/tools_r${pkgver}-linux.zip"
        'https://developer.android.com/assets/images/android_logo.png'
        "$pkgname.desktop"
        "$pkgname.sh"
        "$pkgname.csh"
        "$pkgname.conf"
        'license.html')
sha1sums=('c2c6f6236cbee34c80ec6b5f9f6b7bf0bc5919cb'
          'b8726c63294a23e5fea066a36061164e583b5732'
          'e834f53e13d5926ec7be3fd775fa80aa6f328eb6'
          '78f8574e651c9bf8b7515ecb30c7ef93edbc4a96'
          '08c85aab7523e22b298891c7047bc0e7adbf3437'
          '145bdf3eb41a56574b289c1577a24bc47097ec83'
          'bfb91be7e0b602d765b7a1fcaf0ce1b7e1a93faa')

package() {
  install -Dm755 "$pkgname.sh" "$pkgdir/etc/profile.d/$pkgname.sh"
  install -Dm755 "$pkgname.csh" "$pkgdir/etc/profile.d/$pkgname.csh"
  install -Dm644 "$pkgname.conf" "$pkgdir/etc/ld.so.conf.d/$pkgname.conf"
  install -Dm644 android_logo.png "$pkgdir/usr/share/pixmaps/$pkgname.png"
  install -Dm644 "$pkgname.desktop" \
    "$pkgdir/usr/share/applications/$pkgname.desktop"
  install -Dm644 license.html \
    "$pkgdir/usr/share/licenses/$pkgname/license.html"
  install -d "$pkgdir/opt/$pkgname/platforms"
  install -d "$pkgdir/opt/$pkgname/add-ons"

  cp -a tools "$pkgdir/opt/$pkgname"

  if [[ $CARCH = i686 ]]; then
    rm -rf ${pkgdir}/opt/android-sdk/tools/lib/{monitor-,}x86_64 \
      ${pkgdir}/opt/android-sdk/tools/lib/lib64* \
      ${pkgdir}/opt/android-sdk/tools/emulator64-*
  fi

  # Fix broken permissions
  chmod -R o=g "$pkgdir/opt/$pkgname"
  find "$pkgdir/opt/$pkgname" -perm 744 -exec chmod 755 {} +
}

# getver: developer.android.com/tools/sdk/tools-notes.html
# vim:set ts=2 sw=2 et:
