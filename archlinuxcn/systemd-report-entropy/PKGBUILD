# Maintainer: Jiachen Yang <farseerfc@gmail.com>
pkgname=systemd-report-entropy
pkgver=2
pkgrel=1
pkgdesc="report system entropy to journald during boot"
arch=(any)
url="http://github.com/farseerfc/systemd-report-entropy"
license=('custom:BSD')
depends=('bash' 'bc')
source=("$pkgname"
    "$pkgname.service"
    'LICENSE'
)
sha512sums=('c96c9178f2b8716d75e6a2ff7f4674c2dd0056661000243a66de6c12790ba45123fc4dec7e1fcc7c19fe51578163a5e69b269ce8d4492247e2cc3c064628f178'
            '847444c837ab903e46f9944352a93d76c8663d43fe9960bcf4d8533b2a647d276d870d8963594a26d0a67035499d7d88091af7ed8e6957c67f0679ee8edd3517'
            '6b75fd3686d5b4ae44c7dae0ede5caf38203bb285242e2abaa6f587f357c11138e969fead87f8362834803cea3b1a488da7bfc952545110d0c9a02cf230d4e48')

package() {
    install -Dm755 $pkgname "$pkgdir/usr/bin/$pkgname"
    install -Dm644 $pkgname.service "$pkgdir/usr/lib/systemd/system/$pkgname.service"
    install -Dm644 LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
