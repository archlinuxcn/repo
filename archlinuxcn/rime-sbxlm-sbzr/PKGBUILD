pkgname=rime-sbxlm-sbzr
pkgver=221030
pkgrel=1
pkgdesc='声笔系列码，声笔自然'
arch=(any)
source=('fetch-release.sh')
sha256sums=('25753b1ae73ed951b43d0db122dd929b070df7ad38418314dc6a5956bef084fc')
makedepends=('jq' 'unzip')
depends=('rime-sbxlm')
groups=(sbxlm)

prepare() {
  cd $srcdir
  curl -L $(./fetch-release.sh 自然) -o assets.zip
  unzip -uo assets.zip -d ./assets
  cd ./assets
  sed -i 's/import_preset: symbols/import_preset: sbxlm-symbols/g' *.schema.yaml
}

package() {
  mkdir -p $pkgdir/usr/share/sbxlm/init-userdb
  cd $srcdir/assets
  tar czf $pkgdir/usr/share/sbxlm/init-userdb/$pkgname.tar.gz *.userdb
  cp -r $srcdir/assets $pkgdir/usr/share/rime-data/
  rm -rf $pkgdir/usr/share/rime-data/{*.userdb,$pkgver.zip}
  chmod 755 $pkgdir/usr/share/rime-data/
}

