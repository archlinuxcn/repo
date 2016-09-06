# Maintainer: Jingbei Li <i@jingbei.li>
pkgname=qrsctl
pkgver=3.1.20160816
pkgrel=1
pkgdesc="CLI tool for qiniu.com"
arch=('x86_64')
url="http://developer.qiniu.com/code/v6/tool/qrsctl.html"
license=('custom')

source=("http://devtools.qiniu.com/linux/amd64/qrsctl-v$pkgver")
sha256sums=('797b1530eb1320f1c722f175442e621e8c2849b55538e2168ae56f11b28b2359')

package() {
  cd "${srcdir}"
  mkdir -p "${pkgdir}/usr/bin"
  install -Dm755 $pkgname-v$pkgver $pkgdir/usr/bin/$pkgname
}

# vim: ft=sh syn=sh et
