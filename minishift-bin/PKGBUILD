# Maintainer: Tomas Kral <tomas.kral@gmail.com>

pkgname=minishift-bin
minishift_version=1.17.0
pkgver=${minishift_version//-/_}
pkgrel=1
pkgdesc="Tool that makes it easy to run OpenShift locally."
url="https://github.com/minishift/minishift"
license=('Apache')
arch=('x86_64')
makedepends=()
provides=('minishift')

optdepends=(
  'virtualbox: to use minishift with VirtualBox virtualization'
  'docker-machine-kvm: to use minishisft with KVM virtualization'
)

source=(https://github.com/minishift/minishift/releases/download/v${minishift_version}/minishift-${minishift_version}-linux-amd64.tgz)
sha256sums=('ab8fa3b8ea74b4432925e7490e44a8df6559ed046a02d8965c3a6a8cf3ec1de5')


prepare() {
    tar -xf minishift-${minishift_version}-linux-amd64.tgz
}

package() {
  install -Dm755 "${srcdir}/minishift-${minishift_version}-linux-amd64/minishift" "${pkgdir}/usr/bin/minishift"
  install -Dm644 "${srcdir}/minishift-${minishift_version}-linux-amd64/LICENSE" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
