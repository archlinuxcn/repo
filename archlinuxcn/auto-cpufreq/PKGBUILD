# Maintainer: Julia Abdel-Monem <juliaviolet.dev>
# Maintainer: Parmjot Singh <parmjotsinghrobot at gmail dot com>
# Maintainer: Zhanibek Adilbekov <zhanibek.adilbekov@pm.me>
# shellcheck disable=SC2034,2164,2154
pkgname=auto-cpufreq
pkgver=2.2.0
pkgrel=1
pkgdesc="Automatic CPU speed & power optimizer"
arch=('any')
url="https://github.com/AdnanHodzic/auto-cpufreq"
license=('LGPL3')
depends=('python' 'python-setuptools' 'python-psutil' 'python-click' 'python-distro' 'python-requests' 'python-gobject' 'dmidecode' 'gobject-introspection' 'gtk3')
makedepends=('python-build' 'python-installer' 'python-wheel' 'python-poetry-core' 'python-poetry-dynamic-versioning' )

install="$pkgname.install"

source=(
	"$pkgname-$pkgver.tar.gz::$url/archive/v$pkgver.tar.gz"
	"$pkgname.service"
	"001-fix-icon-n-style-locations.patch"
	"002-fix-other-icon-path.patch"
)

prepare() {
	cd "$srcdir/$pkgname-$pkgver"
	sed -i 's|usr/local|usr|g' "scripts/${pkgname}.service" auto_cpufreq/core.py
	patch --strip=2 --input=../001-fix-icon-n-style-locations.patch
	patch --strip=2 --input=../002-fix-other-icon-path.patch

}

sha256sums=('d84d45a1638f5bff72b5ce7c1653886143cdbb4c6b198e63e054b6a18f7ade68'
            'b9233e3ae649cd1a0f91cb2d1f3ddc8eb48e475882a0d3ff5ab51295f0a30d56'
            'afe7e64dbde2ea599b319e8632d72a3c237b5c4275dd31d0f40e39719193a67b'
            '1f6ee3f549a0fe4d818c8301d9e6a893bfb473ad3c0d9d0b93d38fd4a6635dc5')




build() {
	cd "$srcdir/$pkgname-$pkgver"

	POETRY_DYNAMIC_VERSIONING_BYPASS=1 python -m build --wheel --no-isolation
}

package() {
	cd "$srcdir"
	cd $pkgname-$pkgver

	python -m installer --destdir="$pkgdir" dist/*.whl

	# install -Dm755 scripts/auto-cpufreq-venv-wrapper "$pkgdir/usr/bin/auto-cpufreq"
	# install -Dm755 scripts/start_app "$pkgdir/usr/bin/auto-cpufreq-gtk"
	install -Dm644 scripts/org.auto-cpufreq.pkexec.policy -t "$pkgdir/usr/share/polkit-1/actions/"
	install -Dm644 images/icon.png "$pkgdir/usr/share/pixmaps/auto-cpufreq.png"
	install -Dm644 images/icon.png -t "$pkgdir/usr/share/$pkgname/"
	
	mkdir -p $pkgdir/usr/share/$pkgname/scripts/
	mkdir -p $pkgdir/opt/auto-cpufreq/
	
	install -Dm755 scripts/auto-cpufreq-install.sh "$pkgdir/usr/share/$pkgname/scripts/"
	install -Dm755 scripts/auto-cpufreq-remove.sh "$pkgdir/usr/share/$pkgname/scripts/"
	install -Dm644 $srcdir/auto-cpufreq.service "$pkgdir/etc/systemd/system/$pkgname.service"
	install -Dm755 scripts/cpufreqctl.sh "$pkgdir/usr/share/$pkgname/scripts/"
	install -Dm644 scripts/style.css "$pkgdir/usr/share/$pkgname/scripts/"
	install -Dm644 scripts/auto-cpufreq-gtk.desktop -t "$pkgdir/usr/share/applications/"

}
