# Maintainer: marmis <tiagodepalves@gmail.com>
# Contributor: Benzy
# Contributor: Kudlaty
# Contributor: "marmis" Tiago de Paula <tiagodepalves@gmail.com>
# Contributor: vitor_hideyoshi <vitor.h.n.batista@gmail.com>
# Contributor: katt <magunasu.b97@gmail.com>
# Contributor: Yangtse Su <i@yangtse.me>

pkgname=xpadneo-dkms
pkgdesc='Advanced Linux Driver for Xbox One Wireless Gamepad'
pkgver=0.10.5
pkgrel=1
url='https://github.com/atar-axis/xpadneo'
arch=(any)
license=('GPL-2.0-only AND GPL-3.0-or-later')
checkdepends=('dkms' 'fakeroot' 'LINUX-HEADERS')
source=("xpadneo-v${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz")
b2sums=('b980c98a92c64dafd459ac98783d2cc2bf4a4af2fef6e72dc89adac0bf304c1c6a1449a40639b4dc75d0ae4733d4d98f6a28d70d992d07053514a04862ddcb25')

build() {
  cd "xpadneo-${pkgver}"

  make build
}

check() {
  local kernels=(/usr/lib/modules/*/build)
  if [[ ! -d ${kernels[0]} ]]; then
    echo LINUX-HEADERS required to run check > /dev/stderr
    return 0
  fi

  local kver=${kernels[0]}
  kver=$(dirname "${kver}")
  kver=$(basename "${kver}")
  echo '##' Checking if module builds on Linux "${kver}"...
  echo

  mkdir -p check/dkms check/src
  local dkms_options=(
    --dkmstree "${PWD}/check/dkms"
    --sourcetree "${PWD}/check/src"
    -k "${kver}"
  )

  fakeroot dkms "${dkms_options[@]}" add "xpadneo-${pkgver}/hid-xpadneo"
  fakeroot dkms "${dkms_options[@]}" build "hid-xpadneo/v${pkgver}"
}

package() {
  depends=('dkms' 'bluez' 'bluez-utils')

  cd "xpadneo-${pkgver}"

  # Add modprobe and udev files
  make PREFIX="${pkgdir}" ETC_PREFIX='/usr/lib' install

  # License applicability
  local license_dir="${pkgdir}/usr/share/licenses/${pkgname}"
  install -vD -t "${license_dir}/" -m644 LICENSE.md LICENSES/*.txt

  # DKMS files
  local target_dir="${pkgdir}/usr/src/hid-xpadneo-v${pkgver}"
  install -vD -t "${target_dir}" -m644 hid-xpadneo/{Makefile,dkms.conf}
  install -vD -t "${target_dir}" -m755 hid-xpadneo/dkms.post_{install,remove}

  # Module source
  cd hid-xpadneo
  find src/ -type f -not -name '.*' -not -name 'AGENTS.md' \
    -exec install -vD -m644 {} -T "${target_dir}/{}" \;
}
