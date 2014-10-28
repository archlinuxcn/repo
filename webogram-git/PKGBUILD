# Maintainer: Vincent Ambo <tazjin@gmail.com>

pkgname=webogram-git
pkgver=20140806.160ae72
pkgrel=1
pkgdesc='Web-based Telegram client'
url='https://github.com/zhukov/webogram'
arch=('any')
license=('GPL3')
depends=('nodejs')
makedepends=('git')
source=('git+https://github.com/zhukov/webogram.git'
        'webogram@.service')
sha1sums=('SKIP'
          'c1c2f5cb83d55616d3715bbe505522c718b168d2')

pkgver() {
	cd "${srcdir}/webogram"
	git log -1 --format='%cd.%h' --date=short | tr -d -
}

prepare() {
  cd "${srcdir}/webogram"
  rm -rf .git
}

package() {
	cd "${srcdir}"
        pwd
        install -dm755 "${pkgdir}/opt/"
        cp -r "webogram" "${pkgdir}/opt/webogram"

        install -Dm644 webogram@.service "${pkgdir}/usr/lib/systemd/system/webogram@.service"
}
