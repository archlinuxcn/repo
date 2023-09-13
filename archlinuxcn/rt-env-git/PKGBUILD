pkgbase="rt-env"
pkgname="rt-env-git"
pkgver=1.1.2.225.3517
pkgrel=1
pkgdesc="RT_Thread env!"
arch=("x86_64")
license=("Apache-2.0" "GPL-2.0")
depends=('git' 'scons' 'python')
url="https://github.com/RT-Thread/env"

source=(env::git+https://github.com/RT-Thread/env.git
	packages::git+https://github.com/RT-Thread/packages.git)
sha512sums=(SKIP SKIP)

ENV_ROOT="${HOME}/.env"
ENV_CMD_ROOT="${ENV_ROOT}/tools/scripts"
PKGS_ROOT="${ENV_ROOT}/packages/packages"

pkgver() {
	_envver=`cd env && git describe --long --tags | sed 's/-/\./g; s/^v//; s/g.*$//'`
	_packagesver=`cd packages && git rev-list --count HEAD`
	echo $_envver$_packagesver
}

build() {
	mkdir -p "${srcdir}${PKGS_ROOT}"
	mkdir -p "${srcdir}${ENV_CMD_ROOT}"
	mkdir -p "${srcdir}${ENV_ROOT}/local_pkgs"
	cp -r ${srcdir}/env/* "${srcdir}${ENV_CMD_ROOT}"
	cp -r ${srcdir}/packages/* "${srcdir}${PKGS_ROOT}"
	echo 'source "$PKGS_DIR/packages/Kconfig"' > ${srcdir}${PKGS_ROOT}/../Kconfig
	echo 'export PATH=~/.env/tools/scripts:$PATH' > "${srcdir}${ENV_ROOT}/env.sh"
}

package() {
	mkdir -p ${pkgdir}${HOME}
	chmod 700 ${pkgdir}${HOME}
	install -d -m755 "${pkgdir}${ENV_ROOT}"
	cp -rf ${srcdir}${ENV_ROOT}/* "${pkgdir}${ENV_ROOT}"
  	chown -R $USER:`id -g -n $USER` ${pkgdir}${ENV_ROOT}
}
