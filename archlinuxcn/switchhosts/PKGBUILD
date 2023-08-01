# Contributor: Qingxu <me@linioi.com>

pkgname=switchhosts
pkgver=4.1.2
_subpkgver=6086
pkgrel=1
pkgdesc="app for hosts management & switching"
arch=('any')
url="https://github.com/oldj/SwitchHosts"
license=('Apache')
provides=('switchhosts')
conflicts=(
    'switchhosts-bin'
    'switchhosts-appimage'
)
depends=(
    "gtk3"
    "nss"
)
optdepends=(
    'c-ares'
    'ffmpeg'
    'http-parser'
    'libevent'
    'libvpx'
    'libxslt'
    'minizip'
    're2'
    'snappy'
    'libnotify'
    'libappindicator-gtk3'
)
makedepends=(
    'nodejs'
    'electron19'
    'npm'
)
source=(
    "${pkgname}-${pkgver}.tar.gz::${url}/archive/v${pkgver}/SwitchHosts-v${pkgver}.tar.gz"
)
sha256sums=('7e966120286ea9a77288e3df7393c5b0230b4dcfa427a7012237ae6ff399afe9')

prepare() {
    cd SwitchHosts-${pkgver}
    # use system electron version
    # see: https://wiki.archlinux.org/index.php/Electron_package_guidelines
    electronVer=$(electron19 --version | tail -c +2)
    sed -i "/electronDownload/,/}/d" scripts/make.js
    sed -i "/directories/i\  electronVersion: \`$electronVer\`," scripts/make.js
    sed -i "/directories/i\  electronDist: \`/usr/lib/electron\`," scripts/make.js
    sed -i "s/.*\"electron\":.*$/    \"electron\": \"^$electronVer\",/"  package.json
    # Set arch and target
    local i686=ia32 x86_64=x64 armv7h=armv7l aarch64=arm64
    sed -i "s/.*AppImage:x64.*$/    linux: ['pacman:build_arch'],/" scripts/make.js
    sed -i "s#build_arch#${!CARCH}#g" scripts/make.js
    sed -i "/await makeMacArm/d" scripts/make.js
    sed -i "/await sign/d" scripts/make.js
    sed -i "s/TARGET_PLATFORMS_configs.all/TARGET_PLATFORMS_configs.all.linux/g" scripts/make.js 
}

build() {
    cd SwitchHosts-${pkgver}
    npm install
    npm run build
    npm run make
}

package() {
    tar -xvf SwitchHosts-${pkgver}/dist/SwitchHosts_linux_${pkgver}\(${_subpkgver}\).pacman -C ${pkgdir}
    rm -f ${pkgdir}/.PKGINFO ${pkgdir}/.MTREE ${pkgdir}/.INSTALL
}

