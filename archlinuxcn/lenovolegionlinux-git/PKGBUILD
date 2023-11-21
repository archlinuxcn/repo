# Maintainer: MrDuartePT <gonegrier.duarte@gmail.com>
# Maintainer: xenhat <aur@xenh.at>
# Maintainer: johnfanv2 <https://github.com/johnfanv2>


_pkgname=lenovolegionlinux
pkgname=${_pkgname}-git
pkgver=r255.f087da8
pkgrel=1
pkgdesc="LenovoLegionLinux (LLL) brings additional drivers and tools for Lenovo Legion series laptops to Linux. PLEASE READ THE REPO BEFORE INSTALL THIS PACKAGE!!!"
arch=("x86_64")
url="https://github.com/johnfanv2/LenovoLegionLinux"
license=('GPL')

depends=(
  python-argcomplete
  python-yaml
  python-pyqt5
  polkit
  python-darkdetect
)
makedepends=(
  git
  python-build
  python-installer
  python-setuptools
  python-wheel
)
optdepends=(
  "lenovolegionlinux-dkms-git: DKMS module"
)

conflicts=(
  legion-fan-utils-linux-git
)

source=("${_pkgname}::git+https://github.com/johnfanv2/LenovoLegionLinux")
sha256sums=('SKIP')
install="lenovolegionlinux.install"

pkgver() {
  cd "${_pkgname}"
  printf "r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short=7 HEAD)"
}

prepare() {
  cd "${_pkgname}"
  pkgver_commit=$(echo $pkgver | cut -c 6-)
  git checkout $pkgver_commit
  sed -i "s/version = _VERSION/version = 1.0.0/g" "${srcdir}/${_pkgname}/python/legion_linux/setup.cfg"
}

build() {
 cd "${srcdir}/${_pkgname}/python/legion_linux"
 python -m build --wheel --no-isolation
	
}
package() {
  mkdir -p ${pkgdir}/etc/systemd/system
  mkdir -p ${pkgdir}/etc/acpi/{events,actions}

  cd "${srcdir}/${_pkgname}/python/legion_linux"
  python -m installer --destdir="$pkgdir" dist/*.whl

# Systemd service
  cd "${srcdir}/${_pkgname}/extra"
  install -Dm664 service/*.service "${pkgdir}/etc/systemd/system" 
	install -Dm664 service/*.path "${pkgdir}/etc/systemd/system"
	
# ACPI service
  install -Dm775 acpi/actions/battery-legion-quiet.sh "${pkgdir}/etc/acpi/actions/"
  install -Dm664 acpi/events/ac_adapter_legion-fancurve "${pkgdir}/etc/acpi/events/"
}
