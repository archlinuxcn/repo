# Maintainer: Zhanibek Adilbekov <zhanibek.adilbekov@pm.me>
# shellcheck disable=SC2034,2164,2154
pkgname=auto-cpufreq
pkgver=2.0.0
pkgrel=2
pkgdesc="Automatic CPU speed & power optimizer"
arch=('any')
url="https://github.com/AdnanHodzic/auto-cpufreq"
license=('LGPL3')
depends=('python-setuptools' 'python-distro' 'python-psutil' 'python-click' 'dmidecode' 'python-requests')
optdepends=(
	'cpufreqctl: CPU Power Manager'
	'gnome-shell-extension-cpufreq: CPU Power Manager for GNOME Shell'
	'thermald: recommended to have running alongside by upstream'
	'gobject-introspection: auto-cpufreq-gtk gui'
	'cairo: auto-cpufreq-gtk gui'
	'gtk3: auto-cpufreq-gtk gui'
	'python-gobject: auto-cpufreq-gtk gui'
)
makedepends=('python-pip' 'python-wheel')
install="$pkgname.install"
source=(
	"$pkgname-$pkgver.tar.gz::$url/archive/v$pkgver.tar.gz"
	"$pkgname.service"
	"001-fix-icon-n-style-locations.patch"
)
b2sums=('672fdf026d5223432bac05c8262d30eca487aab5b5d6db2ecb48f4fb7e550a2a152549963b4be9959ada6df54fd94835379634c12116fff867a0f7aca6bfdc64'
        '90d9a6e0a86d01803527462e0ed0ce93d04d245c2c99ab773f31e1eb46dd86b209f98af50967bbdb6627563b0aae0ca4bbc861c812576a243b07c40a483c37db'
        '22e24748e379722335d0e5c48c8f137bd262cc415dfd74aef7d32f6ceededc471da9c7a0985d72dc599dfe7b6ed56d4cbac0c49d59d5fdab548664f0c3cc04af')

prepare() {
	cd "$srcdir/$pkgname-$pkgver"
	sed -i 's|usr/local|usr|g' "scripts/${pkgname}.service" auto_cpufreq/core.py
	patch --strip=2 --input=../001-fix-icon-n-style-locations.patch
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
	install -Dm755 scripts/auto-cpufreq-gtk.desktop -t "$pkgdir/usr/share/applications"
	install -Dm644 images/icon.png "$pkgdir/usr/share/pixmaps/$pkgname.png"
	install -Dm644 scripts/style.css -t "$pkgdir/usr/share/$pkgname/scripts"
	install -Dm644 scripts/org.auto-cpufreq.pkexec.policy -t "$pkgdir/usr/share/polkit-1/actions"
	install -Dm644 "$srcdir/$pkgname.service" -t "$pkgdir/usr/lib/systemd/system"
}
