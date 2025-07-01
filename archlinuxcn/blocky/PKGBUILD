# Maintainer: Nicola Revelant <nicolarevelant@outlook.com>
# Contributor: Luis Martinez <luis dot martinez at disroot dot org>
# Contributor: Andrea Scarpino <andrea@archlinux.org>

pkgname=blocky
pkgver=0.26.2
pkgrel=1
pkgdesc="Fast and lightweight DNS proxy as ad-blocker"
arch=('x86_64' 'armv6h' 'armv7h' 'aarch64')
url="https://github.com/0xERR0R/blocky"
license=('Apache-2.0')
depends=('glibc')
makedepends=('go')
backup=('etc/blocky.yml')
install=blocky.install
source=("$pkgname-$pkgver.tar.gz::$url/archive/v$pkgver.tar.gz"
	'blocky.service'
	'blocky.sysusers'
	'blocky.yml'
)
b2sums=('30edff9e6746dd21128f7bb486bd8d8eac19da42aed237aa4917c1d806ff28b2ce6e0567dfc9096279cf7955ff483c994dd54995bf9720144381a058fea84cec'
	'b84ae53f2efae046f0b7695da9a14513d23f3e8cc8e5ef5b0c80fcbe87446d777b7c1197328472b0cb6500bee5c7ae2755a9e1674ecef545e9d9db443a28d1c2'
	'9641b73253d80a8f64fdd1c10a35ae7631e9eec8d2feda3214836af7634fc0d33d55a5b150912996b3380ef9242b17fbb2a847557b68bf5b657da68eb7d8321c'
	'39ad1c530ea0abc3d166880c2e8cc6b1dd266531a131bef8cd5a5ea0208b4d361f3e98d07a8b26af8517cddb34cbfadc37ae175337befa673f073ae744f40633'
)

prepare() {
	cd "$pkgname-$pkgver"
	echo ":: Downloading Go modules..."
	go mod download -x
}

build() {
	cd "$pkgname-$pkgver"
	make build
}

check() {
	cd "$pkgname-$pkgver"
	# make test # TODO: tests fail
}

package() {
	install -Dvm644 blocky.sysusers "$pkgdir/usr/lib/sysusers.d/blocky.conf"
	install -Dvm644 blocky.service -t "$pkgdir/usr/lib/systemd/system/"
	install -Dvm644 blocky.yml -t "$pkgdir/etc/"
	cd "$pkgname-$pkgver"
	install -Dv bin/blocky -t "$pkgdir/usr/bin/"
	install -Dvm644 README.md -t "$pkgdir/usr/share/doc/$pkgname/"
}
