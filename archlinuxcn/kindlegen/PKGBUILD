# Maintainer: Caleb Maclennan <caleb@alerque.com>
# Contributor: AUR[flyingpig]
# Contributor: Valentin-Costel Haloiu <vially.ichb@gmail.com>
# Contributor: Eugene Yunak <e.yunak@gmail.com>
# Contributor: Pellegrino Prevete <pellegrinoprevete@gmail.com>

pkgname=kindlegen
pkgver=2.9
pkgrel=7
pkgdesc='cli tool to build eBooks that can be used on Amazon’s Kindle platform (binary)'
arch=(x86_64 i686)
url='https://www.amazon.com/gp/feature.html?ie=UTF8&docId=1000765211'
license=(custom)
source=("https://archive.org/download/$pkgname$pkgver/${pkgname}_linux_2.6_i386_v${pkgver/./_}.tar.gz")
md5sums=('21aef3c8846946203e178c83a37beba1')
sha256sums=('9828db5a2c8970d487ada2caa91a3b6403210d5d183a7e3849b1b206ff042296')

package() {
	install -Dm0755 -t "$pkgdir/usr/bin/" kindlegen
	install -Dm0644 -t "$pkgdir/usr/share/licenses/$pkgname/" EULA.txt "KindleGen Legal Notices 2013-02-19 Linux.txt"
	install -Dm0644 -t "$pkgdir/usr/share/doc/$pkgname/" manual.html docs/english/*
}
