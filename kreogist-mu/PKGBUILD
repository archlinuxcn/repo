# Maintainer: Frantic1048 <dev_frantic1048@163.com>

pkgname=kreogist-mu
pkgver='0.8'
pkgrel=9
epoch=1
pkgdesc="Fantastic cross-platform music manager.based on Qt5"
changelog="kreogist-mu.changelog"
arch=('x86_64')
url="https://kreogist.github.io/Mu/"
license=('GPL')
depends=(
  'qt5-base'
  'pulseaudio'
  'ffmpeg'
  'phonon-qt5'
  'gst-libav'
  'gstreamer0.10-ffmpeg')
optdepends=(
  'gst-plugins-good: good plugin libraries'
  'gst-plugins-bad: bad plugin libraries'
  'gst-plugins-ugly: ugly plugin libraries'
)
changelog=$pkgname.changelog
source=("https://github.com/frantic1048/mu-archlinux/releases/download/$pkgver/$pkgname-$pkgver-$arch.7z")
md5sums=('ef52dc72deacb1286f5ad221dfeb24c2')

package() {
  cd "$pkgname-$pkgver-$arch"
  install -d  "${pkgdir}/usr/bin/"
  install -m=775 $pkgname "${pkgdir}/usr/bin"
  install -d "${pkgdir}/usr/share/icons/hicolor/512x512/apps/"
  install -m=664 $pkgname.png "${pkgdir}/usr/share/icons/hicolor/512x512/apps/"
  install -d "${pkgdir}/usr/share/applications/"
  install -m=664 $pkgname.desktop "${pkgdir}/usr/share/applications/"
}
