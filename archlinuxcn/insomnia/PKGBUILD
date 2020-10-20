# Maintainer: kpcyrd <kpcyrd[at]archlinux[dot]org>
# Contributor: vscncls <lucaslou4@protonmail.com>

pkgname=insomnia
pkgver=2020.4.1
pkgrel=1
pkgdesc="Cross-platform HTTP and GraphQL Client"
url="https://github.com/Kong/insomnia"
arch=('any')
license=('MIT')
depends=('electron')
makedepends=('npm')
source=(
  "https://github.com/Kong/insomnia/archive/core@${pkgver}/${pkgname}-${pkgver}.tar.gz"
  "insomnia.desktop"
  "insomnia.sh"
  "node-any.patch"
)
b2sums=('9d6d8323307b28994500b0aa379ddec0243ed4ba6599690c42e90ff886946f1fbbc4364a543deaa69aa18d70b320ab9b6b4858f6d642cf17064b8d722b80c57e'
        'd2ceeb224fa3a35551b0929648d5e066da93a451a66b73373c13ed0dd89575a2482c2dc8e7499b214d0d62cca2532189dac9a681537751a5a86b592cae5686c7'
        '36e005db6302a01287d9d7b19cd0780efaff9799098f292f92aeda8c62cad1864f58eb8ad81ae37777ff4fd660fed4db85f35f9b6b309cb1ca7c84c2c2de29e7'
        'db40a0e7d85cb8378c1f973150249d67e5cfc5d018787b733f2516892144f3c536e1587cdba2eec5da800ee474d4bccf090379b371cb6c59a0a9829090012896')

prepare() {
  cd ${pkgname}-core-${pkgver}

  # remove hard lock to node 12
  node --version | sed s/v// > .nvmrc
  patch --forward --strip=1 --input="${srcdir}/node-any.patch"
}

build() {
  cd ${pkgname}-core-${pkgver}
  npm run bootstrap
  GIT_TAG="core@${pkgver}" npm run app-package
}

package() {
  # Install start script
  install -Dm755 ${pkgname}.sh "${pkgdir}/usr/bin/insomnia"
  install -Dm644 ${pkgname}.desktop -t "${pkgdir}/usr/share/applications"

  cd ${pkgname}-core-${pkgver}
  install -Dm644 packages/insomnia-app/dist/com.insomnia.app/linux-unpacked/resources/app.asar -t "${pkgdir}/usr/share/insomnia"

  for size in 16 32 48 128 256 512; do
    install -Dm644 packages/insomnia-app/build/com.insomnia.app/static/icon.png "${pkgdir}/usr/share/icons/hicolor/${size}x${size}/apps/insomnia.png"
  done

  install -Dm644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}

# vim: ts=2 sw=2 et:
