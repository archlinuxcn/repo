pkgname=rime-sbxlm
pkgver=220304
pkgrel=1
pkgdesc='声笔系列码基础配置，包含声笔简码和声笔拼音'
arch=(any)
source=("https://gitee.com/sbxlm/sbxlm/attach_files/958461/download/$pkgver.zip" 'sbxlm-init')
sha256sums=('24d4a0ebe86b1c09b1a5184209286b9400fba411acd1dd0eb97b06e9325cd8d0'
            '496953ce12837de3f575c913a5317996002bcbf8ba2337f697b2efe15d2e0e5e')
optdepends=('librime-sbxlm-git' 'fcitx5-rime')
install=$pkgname.install
groups=(sbxlm)

prepare () {
  cd $srcdir/sbxlm
  chmod 755 $srcdir/sbxlm
  mv symbols.yaml sbxlm-symbols.yaml
  sed -i 's/import_preset: symbols/import_preset: sbxlm-symbols/g' *.schema.yaml
}

package() {
  mkdir -p $pkgdir/usr/share/sbxlm/init-userdb
  mkdir -p $pkgdir/usr/bin
  cp sbxlm-init $pkgdir/usr/bin
  cd $srcdir/sbxlm
  tar czf $pkgdir/usr/share/sbxlm/init-userdb/$pkgname.tar.gz *.userdb
  cp -r $srcdir/sbxlm/ $pkgdir/usr/share/rime-data/
  rm -rf $pkgdir/usr/share/rime-data/*.userdb
}
