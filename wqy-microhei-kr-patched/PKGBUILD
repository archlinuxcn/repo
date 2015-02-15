# Maintainer: wicast <wicastchen at hotmail>
# This is the patched version of wqy-microhei .ttc to fix korean rendering problem on Chromium/Chorme(and possibly other programs).
# The patch is provided by Ben Wagner (Bungeman) who comes from Chromium team.
# Debian's fonts-wqy-microhei package has already contained the patched version.

pkgname=wqy-microhei-kr-patched
_pkgname=wqy-microhei
pkgver=0.2.0_beta
pkgrel=2
pkgdesc="A Sans-Serif style high quality CJK outline font.Fix incorrect advanceWidths in hmtx for composite glyphs, which
    had caused Korean Hangul glyphs to stack on top of each other."
arch=('any')
license=('GPL3' 'APACHE' 'custom:"font embedding exception"')
install=wqy-microhei.install
url="https://packages.debian.org/jessie/all/fonts-wqy-microhei"
depends=('fontconfig' 'xorg-font-utils')
provides=('wqy-microhei')
conflicts=('wqy-microhei')
source=(
        '44-wqy-microhei.conf'
        "http://ftp.cn.debian.org/debian/pool/main/f/fonts-wqy-microhei/fonts-wqy-microhei_${pkgver//_/-}-${pkgrel}_all.deb"
)
md5sums=('2614129902fda4e45aa7f0f7b635cc4f'
         '922fc2e9b9efeaf50ad464cb1d7e57d0')
build() {
  msg2 "Extracting the data.tar.xz"
  tar -xf data.tar.xz -C "$srcdir/"
}

package() {
  install -d "$pkgdir/etc/fonts/conf.d/"
  install -Dm644 "$srcdir/44-wqy-microhei.conf" "$pkgdir/etc/fonts/conf.avail/44-wqy-microhei.conf"
  install -Dm644 "$srcdir/usr/share/fonts/truetype/wqy/wqy-microhei.ttc" "$pkgdir/usr/share/fonts/wenquanyi/${_pkgname}/wqy-microhei.ttc"
  install -Dm644 "$srcdir/usr/share/doc/fonts-wqy-microhei/copyright" "$pkgdir/usr/share/licenses/${_pkgname}/copyright"
  cd "$pkgdir/etc/fonts/conf.d/"
  ln -s ../conf.avail/44-wqy-microhei.conf .
}
