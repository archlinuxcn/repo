pkgname=rime-sbxlm
pkgver=20230118
pkgrel=2
pkgdesc='声笔系列码配置'
arch=(any)
source=('fetch-release.sh' 'sbxlm-init')
sha256sums=('8a63e188b5f0601d881503d7d058362eda5fcfdfcf88fa6b4010c8f063c5689e'
            '496953ce12837de3f575c913a5317996002bcbf8ba2337f697b2efe15d2e0e5e')
makedepends=('jq' 'unzip')
optdepends=('librime-sbxlm-git' 'fcitx5-rime')
replaces=('rime-sbxlm-sbfm' 'rime-sbxlm-sbkm' 'rime-sbxlm-sbzr' 'rime-sbxlm-sbxh')
install=$pkgname.install
groups=(sbxlm)

prepare () {
  cd "$srcdir"
  curl -L $(./fetch-release.sh url $pkgver) -o assets.zip
  unzip -uo ./assets.zip -d ./assets
  cd $srcdir/assets/sbxlm
  chmod 755 $srcdir/assets/sbxlm
  mv symbols.yaml sbxlm-symbols.yaml
  sed -i 's/import_preset: symbols/import_preset: sbxlm-symbols/g' *.schema.yaml
}

package() {
  mkdir -p $pkgdir/usr/share/sbxlm/init-userdb
  mkdir -p $pkgdir/usr/bin
  cp sbxlm-init $pkgdir/usr/bin
  cd $srcdir/assets/sbxlm
  tar czf $pkgdir/usr/share/sbxlm/init-userdb/$pkgname.tar.gz *.userdb
  cp -r $srcdir/assets/sbxlm/ $pkgdir/usr/share/rime-data/
  rm -rf $pkgdir/usr/share/rime-data/*.userdb
}
