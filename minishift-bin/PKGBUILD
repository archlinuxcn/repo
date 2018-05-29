# Maintainer: Tomas Kral <tomas.kral@gmail.com>

pkgname=minishift-bin
minishift_version=1.18.0
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
sha256sums=('a2091a4f053839a34e03bdb617ae02f348155afe58331e3a6220ef491dc88014')


prepare() {
    tar -xf minishift-${minishift_version}-linux-amd64.tgz
}

package() {
  install -Dm755 "${srcdir}/minishift-${minishift_version}-linux-amd64/minishift" "${pkgdir}/usr/bin/minishift"
  install -Dm644 "${srcdir}/minishift-${minishift_version}-linux-amd64/LICENSE" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
