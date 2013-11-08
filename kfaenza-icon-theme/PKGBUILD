# Maintainer:  danyf90 <daniele.formichelli@gmail.com>
# Maintainer: JokerBoy <jokerboy at punctweb dot ro>

pkgname=kfaenza-icon-theme
pkgver=0.8.9
pkgrel=4
pkgdesc="Faenza icon theme for KDE4"
url="http://kde-look.org/content/show.php?content=143890"
license=('GPL')
arch=('any')
depends=('kdebase-workspace')
source=(
	"http://pkgs.fedoraproject.org/repo/pkgs/kfaenza-icon-theme/kfaenza-icon-theme-${pkgver}.tar.gz/95e9f287da7a0fd76fb406d313eee77e/kfaenza-icon-theme-${pkgver}.tar.gz"
	"kfaenza-icon-patch-0.3.tar.gz")
sha512sums=(
	'cb66f9ab7f25c4f5c4f5148d6dcdda4015f7ef128234845b60ab06db4b82f2fc0103f922f349a93a8e559b781db44e9c6865a2d0dadab8988c4a34f65a867cc4'
	'0a0bf105d320c25ffca06f6fbfdd4298ea891012aaa33df9494dbab04f786bd5b9b7a18a5a388333fb8af708334ee4653f8aaa86b0221b3ef45755bb3b8f3d8a')
options=(!strip)

package() {
  install -d $pkgdir/usr/share/icons
  cp -r $srcdir/KFaenza $pkgdir/usr/share/icons/

  for size in 16 22 32 48 64 128 256; do
    cd $pkgdir/usr/share/icons/KFaenza/places/$size/
    mv start-here-kde.png start-here-kde-default.png
    ln -sf archlinux-logo.png distributor-logo.png
    ln -sf start-here-archlinux.png start-here-kde.png
  done;

  cd $pkgdir/usr/share/icons/KFaenza/places/scalable/
  mv start-here-kde.svg start-here-kde-default.svg
  ln -sf archlinux-logo.svg distributor-logo.svg
  ln -sf start-here-archlinux.svg start-here-kde.svg

  find $pkgdir/usr -type f -exec chmod 644 {} \;
  find $pkgdir/usr -type d -exec chmod 755 {} \;
  find $pkgdir/usr -type f -name '.directory' -delete

  #apply kfaenza patch
  cd $srcdir
  tar -xvzf kfaenza-icon-patch-0.3.tar.gz -C $pkgdir/usr/share/icons/KFaenza/
}
