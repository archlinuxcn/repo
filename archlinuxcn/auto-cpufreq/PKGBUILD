# Maintainer: Julia Abdel-Monem <juliaviolet.dev>
# Maintainer: Parmjot Singh <parmjotsinghrobot at gmail dot com>
# Maintainer: Zhanibek Adilbekov <zhanibek.adilbekov@pm.me>
# shellcheck disable=SC2034,2164,2154
pkgname=auto-cpufreq
pkgver=3.2.0
pkgrel=1
pkgdesc="Automatic CPU speed & power optimizer"
arch=('any')
url="https://github.com/AdnanHodzic/auto-cpufreq"
license=('GPL-3.0-or-later')
depends=('python' 'python-psutil' 'python-click' 'python-distro' 'python-requests' 'python-gobject' 'python-pyinotify' 'python-urwid' 'python-pyasyncore' 'dmidecode' 'gtk3' 'pango' 'glib2' 'gdk-pixbuf2' 'bash')
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
	sed -i "s|/opt/auto-cpufreq/current/venv/bin/auto-cpufreq|/usr/bin/auto-cpufreq|g" scripts/org.auto-cpufreq.pkexec.policy
	patch --strip=2 --input=../001-fix-icon-n-style-locations.patch
	patch --strip=2 --input=../002-fix-other-icon-path.patch

}

sha256sums=('99d46c8bbc8ca6a22caf08bbd7857813a0b27c4403ba6f76830863a64621395b'
            '8ff1c82788f7cb6bf06151e6632aa4006eb09337daf03faa4866d23075b39e1b'
            'f0fda29c1b5aab24de392281a186bc71acdec765fc1c08c16ac588ff0bff348b'
            '6afa9b853b690c832eff5fe499063c17719a870840f5cfec8903285eaf1dddc0')

build() {
	cd "$srcdir/$pkgname-$pkgver"

	POETRY_DYNAMIC_VERSIONING_BYPASS="$pkgver" python -m build --wheel --no-isolation
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
	# Upstream writes governor/turbo override state here without creating the directory.
	mkdir -p "$pkgdir/opt/auto-cpufreq/"

	install -Dm755 scripts/auto-cpufreq-install.sh "$pkgdir/usr/share/$pkgname/scripts/"
	install -Dm755 scripts/auto-cpufreq-remove.sh "$pkgdir/usr/share/$pkgname/scripts/"
	install -Dm644 $srcdir/auto-cpufreq.service "$pkgdir/usr/lib/systemd/system/$pkgname.service"
	install -Dm755 scripts/cpufreqctl.sh "$pkgdir/usr/share/$pkgname/scripts/"
	install -Dm644 scripts/style.css "$pkgdir/usr/share/$pkgname/scripts/"
	install -Dm644 scripts/auto-cpufreq-gtk.desktop -t "$pkgdir/usr/share/applications/"

}
