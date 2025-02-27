# Maintainer: Aseem Athale <athaleaseem@gmail.com>

_appprefix="/opt"
_appdataprefix="/var/opt"

pkgname=open-webui
pkgver=0.5.18
pkgrel=1
pkgdesc="Web UI and OpenAI API for various LLM runners, including Ollama"
arch=('any')
url="https://github.com/open-webui/open-webui"
license=('MIT')
depends=('python312')
makedepends=('npm' 'nvm')
optdepends=('ollama' 'tika-server')
conflicts=('open-webui-git')
source=("${pkgname}-${pkgver}.tar.gz"::"${url}/archive/refs/tags/v${pkgver}.tar.gz"
    "open-webui.service"
    "open-webui.conf")

install="${pkgname}.install"
sha1sums=('8c6a327dd650a3d5bcb94ea01f132383ea7ed14a'
          '9b789adb8d91f15ece2187af4aec810847d4b0b2'
          'fb015c224b9529988823f0e24d65ab4a004d30c0')
options=(!strip !debug)

_ensure_local_nvm() {
    # let's be sure we are starting clean
    which nvm >/dev/null 2>&1 && nvm deactivate && nvm unload
    export NVM_DIR="${srcdir}/.nvm"

    # The init script returns 3 if version specified
    # in ./.nvrc is not (yet) installed in $NVM_DIR
    # but nvm itself still gets loaded ok
    source /usr/share/nvm/init-nvm.sh || [[ $? != 1 ]]
}

prepare() {
    _ensure_local_nvm
    nvm install lts/iron
}

build() {
    _ensure_local_nvm
    cd "${pkgname}-${pkgver}"
    export NODE_OPTIONS="--max_old_space_size=4096"
    npm install
    npm run format
    npm run i18n:parse
    npm run build
}

check() {
    _ensure_local_nvm
    cd "${pkgname}-${pkgver}"
    export NODE_OPTIONS="--max_old_space_size=4096"
    npm run test:frontend
}

package() {
    # Install systemd service
    install -Dm644 "./$pkgname.service" "$pkgdir/usr/lib/systemd/system/$pkgname.service"

    # Install license
    install -Dm 644 "$srcdir/${pkgname}-${pkgver}"/LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"

    # Install the default config file to /usr/share/$pkgname/open-webui.conf
    install -d "$pkgdir/usr/share/$pkgname"
    install -Dm644 "./$pkgname.conf" "$pkgdir/usr/share/$pkgname/$pkgname.conf"

    # Copy source to app's home directory
    parent_dir="$pkgdir/${_appprefix}"  # /opt

    install -d "$pkgdir/${_appprefix}/$pkgname"
    install -d "$pkgdir/${_appdataprefix}/$pkgname"
    install -d "$pkgdir/${_appdataprefix}/$pkgname/data"

    # copy over files
    cp -R "$srcdir/${pkgname}-${pkgver}/." "$pkgdir/${_appprefix}/$pkgname"

    # clean up stuff we don't need
    rm -rf "$pkgdir/${_appprefix}/$pkgname/node_modules"
    rm -rf "$pkgdir/${_appprefix}/$pkgname/.git"

    # Fix permissions
    echo "Setting permissions for $pkgdir${_appprefix}/$pkgname"
    chmod 755 "$pkgdir/${_appprefix}/$pkgname"
    find "$pkgdir/${_appprefix}/$pkgname" -type d -exec chmod 755 {} \;
    find "$pkgdir/${_appprefix}/$pkgname" -type f -exec chmod 644 {} \;

    echo "Setting permissions for $pkgdir${_appdataprefix}/$pkgname"
    chmod 700 "$pkgdir/${_appdataprefix}/$pkgname"
    find "$pkgdir/${_appdataprefix}/$pkgname" -type d -exec chmod 700 {} \;
    find "$pkgdir/${_appdataprefix}/$pkgname" -type f -exec chmod 664 {} \;
}
