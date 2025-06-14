# Maintainer: Julia Abdel-Monem <juliaviolet.dev>
# Maintainer: Parmjot Singh <parmjotsinghrobot at gmail dot com>
# Maintainer: Zhanibek Adilbekov <zhanibek.adilbekov@pm.me>
# shellcheck disable=SC2034,2164,2154
pkgname=auto-cpufreq
pkgver=2.6.0
pkgrel=2
pkgdesc="Automatic CPU speed & power optimizer"
arch=('any')
url="https://github.com/AdnanHodzic/auto-cpufreq"
license=('LGPL-3.0-or-later')
depends=('python' 'python-setuptools' 'python-psutil' 'python-click' 'python-distro' 'python-requests' 'python-gobject' 'python-pyinotify' 'python-urwid' 'python-pyasyncore' 'dmidecode' 'gobject-introspection' 'gtk3')
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

sha256sums=('210a51baea539b560b5db4a3f98cfd02d6e0a70dd106f1e65fa3c0b70b84c767'
            '8ff1c82788f7cb6bf06151e6632aa4006eb09337daf03faa4866d23075b39e1b'
            '227d85df7f71187c87e24388104f0127b13a680c1e859a90a14864a0d29e1fdf'
            '0db58e3a6185418677a5c4f2ea15d7a1becf08bc2d955b8ffb9783190dd4666c')

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
	install -Dm644 $srcdir/auto-cpufreq.service "$pkgdir/usr/lib/systemd/system/$pkgname.service"
	install -Dm755 scripts/cpufreqctl.sh "$pkgdir/usr/share/$pkgname/scripts/"
	install -Dm644 scripts/style.css "$pkgdir/usr/share/$pkgname/scripts/"
	install -Dm644 scripts/auto-cpufreq-gtk.desktop -t "$pkgdir/usr/share/applications/"

}
