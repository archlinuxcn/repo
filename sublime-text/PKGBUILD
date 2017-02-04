# Maintainer: carstene1ns <arch carsten-teibes de> - http://git.io/ctPKG
# Contributor: Josh Kropf <josh@slashdev.ca>
# Contributor: Bartosz Chmura <chmurli at gmail dot com>
# Contributor: Mikkel Kroman <mk at maero dot dk>

pkgname=sublime-text
pkgver=2.0.2
pkgrel=4
pkgdesc="Sophisticated text editor for code, html and prose"
arch=('i686' 'x86_64')
url="http://www.sublimetext.com/2"
license=('custom')
depends=("libpng" "gtk2" "bash" "procps-ng" "xdg-utils" "desktop-file-utils"
         "shared-mime-info")
install="$pkgname.install"
                        # EULA file is from http://www.sublimetext.com/eula
                        # converted with 'html2text --ignore-links --body-width=80'
source=("$pkgname-EULA"
        "$pkgname.desktop"
        "$pkgname.sh"
        "http://downloads.sourceforge.net/libpng/libpng-1.6.2.tar.xz"
        "http://downloads.sourceforge.net/libpng-apng/libpng-1.6.2-apng.patch.gz"
        "0001-libpng16-Avoid-dereferencing-NULL-pointer-possibly-r.patch"
        "0002-libpng16-Calculate-our-own-zlib-windowBits-when-deco.patch"
        "adjust-apng-patch-for-libpng16-git-changes.patch")
source_i686=("http://c758482.r82.cf2.rackcdn.com/Sublime%20Text%20${pkgver}.tar.bz2")
source_x86_64=("http://c758482.r82.cf2.rackcdn.com/Sublime%20Text%20${pkgver}%20x64.tar.bz2")
sha256sums=('43aa2cf3becee23697177c6e6ecd4fc2c4b459499631bfdb2533cdb60c27530e'
            '3f11bf8cb814b68ed81b535dd13cc86bb28c71010d74141bfa06137782fd2f7d'
            '765c8a65ef429dc81a983d14d94c97a2d185575d74e702861ad3e374e2759338'
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
  cd libpng-1.6.2
  patch -Np1 < ../0001-libpng16-Avoid-dereferencing-NULL-pointer-possibly-r.patch
  patch -Np1 -i ../0002-libpng16-Calculate-our-own-zlib-windowBits-when-deco.patch
  patch -d .. -Np0 < ../adjust-apng-patch-for-libpng16-git-changes.patch
  patch -Np1 < ../libpng-1.6.2-apng.patch
}

build() {
  # libpng
  cd libpng-1.6.2
  ./configure --prefix=/ --with-binconfigs=no --enable-shared --disable-static
  make install DESTDIR="$srcdir"/png_fake_install
}

package () {
  install -d "$pkgdir"/opt
  cp -rup "Sublime Text 2" "$pkgdir"/opt/$pkgname

  # launcher
  install -Dm755 $pkgname.sh "$pkgdir"/usr/bin/subl

  # .desktop file and icons
  install -Dm644 $pkgname.desktop "$pkgdir"/usr/share/applications/$pkgname.desktop
  for _res in 256x256 128x128 48x48 32x32 16x16; do
    install -d "$pkgdir"/usr/share/icons/hicolor/$_res/apps
    ln -s /opt/$pkgname/Icon/$_res/sublime_text.png \
      "$pkgdir"/usr/share/icons/hicolor/$_res/apps/$pkgname.png
  done

  # license
  install -Dm644 $pkgname-EULA "$pkgdir"/usr/share/licenses/$pkgname/EULA

  # libpng
  install -m644 png_fake_install/lib/libpng16.so.16.2.0 \
    "$pkgdir"/opt/$pkgname/lib/libpng16.so.16.2.0
  ln -s libpng16.so.16.2.0 "$pkgdir"/opt/$pkgname/lib/libpng16.so.16
  ln -s libpng16.so.16 "$pkgdir"/opt/$pkgname/lib/libpng16.so
  ln -s libpng16.so "$pkgdir"/opt/$pkgname/lib/libpng.so
}
