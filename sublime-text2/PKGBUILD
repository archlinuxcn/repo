# Maintainer: carstene1ns <arch carsten-teibes de> - http://git.io/ctPKG

pkgname=sublime-text2
pkgver=2.0.2
pkgrel=1
pkgdesc="Sophisticated text editor for code, html and prose (legacy version)"
arch=('i686' 'x86_64')
url="https://www.sublimetext.com/2"
license=('custom: commercial')
depends=("libpng" "gtk2" "bash" "xdg-utils" "desktop-file-utils" "shared-mime-info")
conflicts=("sublime-text")
        # EULA file: 'html2text --body-width=80 https://www.sublimetext.com/eula'
source=("$pkgname-EULA"
        "$pkgname.desktop"
        "$pkgname.sh"
        "http://downloads.sourceforge.net/libpng/libpng-1.6.2.tar.xz"
        "http://downloads.sourceforge.net/libpng-apng/libpng-1.6.2-apng.patch.gz"
        "0001-libpng16-Avoid-dereferencing-NULL-pointer-possibly-r.patch"
        "0002-libpng16-Calculate-our-own-zlib-windowBits-when-deco.patch"
        "adjust-apng-patch-for-libpng16-git-changes.patch")
source_i686=("https://download.sublimetext.com/Sublime%20Text%20${pkgver}.tar.bz2")
source_x86_64=("https://download.sublimetext.com/Sublime%20Text%20${pkgver}%20x64.tar.bz2")
sha256sums=('dec26169ec941f1089810b7be599193577d0250f20e465d1399b062f71f2a244'
            '7a3d0ea23fc0eb8d1e4d322df96a18aab214f8f7ef5808a60f9ad4866c0fc14b'
            '153cfa48f8f058cba03e30aa39dc90d9b9ab1d07ce9bfb3bceb78b2c699c47e8'
            '1c97a90bc22107e50f04f77a0115f4ec890d5c6a373ac4c560e8fb87259e92de'
            '4196f3c3894f455a78a65170209fc948b01a7448304d8c39bc29d37852b8c73b'
            '0632ea1d588cb7b85dfc2c13444de1682e9d7e61caaf8cce118fc535bc9f4d90'
            '2a65904c85ff492d4f91edd55e17f81ba36ee6af1cac7402f786580f3fc56216'
            '1f51e33233ce560c5d8002bc096aa4cc5be70c082e08b14db4376a9a02f2714a')
sha256sums_i686=('07338e041cfb348938fa8069f0aad3b5b43c319b7ec564ffff1489796f2dcf08')
sha256sums_x86_64=('01baed30d66432e30002a309ff0393967be1daba5cce653e43bba6bd6c38ab84')

prepare() {
  # libpng
  rm -rf png_fake_install
  mkdir png_fake_install
  patch -Np0 < adjust-apng-patch-for-libpng16-git-changes.patch
  cd libpng-1.6.2
  patch -Np1 < ../0001-libpng16-Avoid-dereferencing-NULL-pointer-possibly-r.patch
  patch -Np1 < ../0002-libpng16-Calculate-our-own-zlib-windowBits-when-deco.patch
  patch -Np1 < ../libpng-1.6.2-apng.patch
}

build() {
  # libpng
  cd libpng-1.6.2
  ./configure --prefix=/ --without-binconfigs --enable-shared --disable-static
  make install DESTDIR="$srcdir"/png_fake_install
}

package () {
  install -d "$pkgdir"/opt
  cp -r "Sublime Text 2" "$pkgdir"/opt/$pkgname

  # launcher
  install -Dm0755 $pkgname.sh "$pkgdir"/usr/bin/subl

  # .desktop file and icons
  install -Dm0644 $pkgname.desktop "$pkgdir"/usr/share/applications/$pkgname.desktop
  for _res in 256x256 128x128 48x48 32x32 16x16; do
    install -d "$pkgdir"/usr/share/icons/hicolor/$_res/apps
    ln -s /opt/$pkgname/Icon/$_res/sublime_text.png \
      "$pkgdir"/usr/share/icons/hicolor/$_res/apps/$pkgname.png
  done

  # license
  install -Dm0644 $pkgname-EULA "$pkgdir"/usr/share/licenses/$pkgname/EULA

  # libpng
  install -m0644 png_fake_install/lib/libpng16.so.16.2.0 \
    "$pkgdir"/opt/$pkgname/lib/libpng16.so.16.2.0
  ln -s libpng16.so.16.2.0 "$pkgdir"/opt/$pkgname/lib/libpng16.so.16
  ln -s libpng16.so.16 "$pkgdir"/opt/$pkgname/lib/libpng16.so
  ln -s libpng16.so "$pkgdir"/opt/$pkgname/lib/libpng.so
}
