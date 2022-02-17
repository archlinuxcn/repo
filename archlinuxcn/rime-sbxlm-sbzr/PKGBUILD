pkgname=rime-sbxlm-sbzr
pkgver=220217
pkgrel=1
pkgdesc='声笔系列码，声笔自然'
arch=(any)
source=("https://gitee.com/sbxlm/sbxlm/attach_files/958326/download/$pkgver.zip")
sha256sums=('345b7a10be8cca7880e0b191eaa0223ad38504706793cbc76babd5344e9a56cc')
depends=('rime-sbxlm')
groups=(sbxlm)

prepare() {
  cd $srcdir
  sed -i 's/import_preset: symbols/import_preset: sbxlm-symbols/g' *.schema.yaml
}

package() {
  mkdir -p $pkgdir/usr/share/sbxlm/init-userdb
  cd $srcdir
  tar czf $pkgdir/usr/share/sbxlm/init-userdb/$pkgname.tar.gz *.userdb
  cp -r $srcdir/ $pkgdir/usr/share/rime-data/
  rm -rf $pkgdir/usr/share/rime-data/{*.userdb,$pkgver.zip}
  chmod 755 $pkgdir/usr/share/rime-data/
}
