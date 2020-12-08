# Maintainer: Jiachen Yang <farseerfc@gmail.com>
pkgname=systemd-report-entropy
pkgver=3
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
sha512sums=('e15412015f32665f24715c099fd658f561a4ef71207e5820e7c0ff6e4f38083d5c593bc72b344d9af0c00998fabc2a734037c74580434a22fde562548f31fcd2'
            '847444c837ab903e46f9944352a93d76c8663d43fe9960bcf4d8533b2a647d276d870d8963594a26d0a67035499d7d88091af7ed8e6957c67f0679ee8edd3517'
            '6b75fd3686d5b4ae44c7dae0ede5caf38203bb285242e2abaa6f587f357c11138e969fead87f8362834803cea3b1a488da7bfc952545110d0c9a02cf230d4e48')

package() {
    install -Dm755 $pkgname "$pkgdir/usr/bin/$pkgname"
    install -Dm644 $pkgname.service "$pkgdir/usr/lib/systemd/system/$pkgname.service"
    install -Dm644 LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
