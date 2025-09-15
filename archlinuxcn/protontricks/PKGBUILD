# Maintainer: Jason Stryker <public at jasonstryker dot com>
# Maintainer: Konstantin Liberty <jon9097 at gmail dot com>

pkgname=protontricks
pkgver=1.13.0
pkgrel=3
pkgdesc="Run Winetricks commands for Steam Play/Proton games among other common Wine features"
arch=('any')
url="https://github.com/Matoking/protontricks"
license=('GPL-3.0-or-later')
depends=('python' 'python-vdf' 'winetricks' 'python-setuptools' 'python-pillow')
optdepends=(
  'yad: GUI for game selection', 
  'zenity: GUI for winetricks'
)
makedepends=('git' 'python-setuptools-scm' 'python-build' 'python-installer' 'python-wheel')
provides=("protontricks")
conflicts=('protontricks-git')
source=("${pkgname}-${pkgver}::git+${url}.git#tag=${pkgver}"
        "protontricks.desktop"
        "protontricks.png")
sha512sums=('SKIP'
            '79490d897c4199b93af13206ba43f2403d78d3a0a340c5fa437b9523af5dab84f2e3059472bb22ec4452534649217263fcd32a4ce6c47766ee9f62d228858b23'
            'd95ce89ed1e4c6d2f55b89bac8af1052c4cd371ceabd9e93311126a256f8d2e8885733ba7513651b11cf3c0eedfb8048b45782c25ab843772e2b8d73a8094edd')

build() {
  cd "${srcdir}/${pkgname}-${pkgver}"

  python -m build --wheel --no-isolation
}

package() {
  cd "${srcdir}/${pkgname}-${pkgver}"

  python -m installer --destdir="$pkgdir" dist/*.whl

  install -Dm644 "$srcdir/protontricks.desktop" "$pkgdir/usr/share/applications/protontricks.desktop"
  install -Dm644 "$srcdir/protontricks.png" "$pkgdir/usr/share/icons/hicolor/128x128/apps/protontricks.png"
  install -Dm644 README.md "${pkgdir}/usr/share/doc/${pkgname}/README.md"
}
