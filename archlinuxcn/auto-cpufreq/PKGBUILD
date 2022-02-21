# Maintainer: Zhanibek Adilbekov <zhanibek.adilbekov@pm.me>
pkgname=auto-cpufreq
pkgver=1.9.2
pkgrel=1
pkgdesc="Automatic CPU speed & power optimizer"
arch=('any')
url="https://github.com/AdnanHodzic/auto-cpufreq"
license=('LGPL3')
depends=('python-distro' 'python-psutil' 'python-click' 'dmidecode')
optdepends=(
	'cpufreqctl: CPU Power Manager'
	'gnome-shell-extension-cpufreq: CPU Power Manager for GNOME Shell'
)
makedepends=('python-setuptools' 'python-pip')
install="$pkgname.install"
source=("$pkgname-$pkgver.tar.gz::$url/archive/v$pkgver.tar.gz" "$pkgname.service")
b2sums=('3f4f5b6aeaa4764791a5eb727558da170e7f635e7aae2119a0fde8be4a3009c7504fd888bbea5c961b0716c4ca03929c8f7e81cc2a2afe04eab159337fd74f0d'
        '90d9a6e0a86d01803527462e0ed0ce93d04d245c2c99ab773f31e1eb46dd86b209f98af50967bbdb6627563b0aae0ca4bbc861c812576a243b07c40a483c37db')

prepare() {
	cd "$srcdir/$pkgname-$pkgver"
	sed -i 's|usr/local|usr|g' "scripts/${pkgname}.service" auto_cpufreq/core.py
}

build() {
	cd "$srcdir/$pkgname-$pkgver"
	python setup.py build
}

package() {
	cd "$srcdir/$pkgname-$pkgver"
	python setup.py install --root="$pkgdir" --optimize=1 --skip-build
	install -Dm644 LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
	install -Dm644 README.md "$pkgdir/usr/share/doc/$pkgname/README"
	install -Dm755 scripts/cpufreqctl.sh -t "$pkgdir/usr/share/$pkgname/scripts"
	install -Dm644 "$srcdir/$pkgname.service" -t "$pkgdir/usr/lib/systemd/system"
}
