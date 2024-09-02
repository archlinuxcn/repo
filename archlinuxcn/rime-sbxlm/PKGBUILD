# Maintainer: ZeekoZhu <vaezt@outlook.com>

pkgname=rime-sbxlm
pkgver=20240901
pkgrel=1
pkgdesc='声笔系列码配置'
arch=(any)
url="https://github.com/sbsrf/sbsrf"
source=('sbxlm-init' "${pkgname}-${pkgver}.zip::${url}/releases/download/${pkgver}/sbsrf.zip" "${pkgname}-${pkgver}-src.zip::${url}/archive/refs/tags/${pkgver}.zip")
noextract=("${pkgname}-${pkgver}.zip" "${pkgname}-${pkgver}-src.zip")
license=('BSD-3-Clause')
sha256sums=('ddd93d18c5ecd40df142666df06d8588d4c345d662c38e31ea22402c3308549f'
            '4d9f809fcee9a161bcd1f40c8fa01d07a2e3718b4e9e512784eeb6b23331de27'
            'd4e42d5e902daa38689dee959e7042471760e7e1b41e7ba030ee88ad94ee5cb5')
makedepends=('unzip')
optdepends=('librime' 'fcitx5-rime')
replaces=('rime-sbxlm-sbfm' 'rime-sbxlm-sbkm' 'rime-sbxlm-sbzr' 'rime-sbxlm-sbxh')
install=$pkgname.install
groups=(sbxlm)

prepare () {
  cd "$srcdir"
  unzip -juo ./${pkgname}-${pkgver}-src.zip sbsrf-${pkgver}/LICENSE
  unzip -uo ./${pkgname}-${pkgver}.zip -d ./assets
  chmod 755 $srcdir/assets
}

package() {
  mkdir -p $pkgdir/usr/share/sbxlm/
  mv $srcdir/assets/default.custom.yaml $pkgdir/usr/share/sbxlm
  mkdir -p $pkgdir/usr/bin
  cp sbxlm-init $pkgdir/usr/bin
  mkdir -p $pkgdir/usr/share/rime-data/
  cp -r $srcdir/assets/* $pkgdir/usr/share/rime-data/
  install -Dm664 $srcdir/LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
