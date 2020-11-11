# Maintainer: Caleb Maclennan <caleb@alerque.com>
# Contributor: Gabriel Saillard (GitSquared) <gabriel@saillard.dev>
# Contributor: David Birks <david@tellus.space>
# Contributor: Simon Doppler (dopsi) <dop.simon@gmail.com>
# Contributor: dpeukert
# Contributor: lonaowna

pkgname=marktext-git
_pkgname=${pkgname%-git}
pkgver=0.16.2.r0.g1e7ff90
pkgrel=1
pkgdesc='A simple and elegant open-source markdown editor that focused on speed and usability'
arch=('x86_64')
url='https://marktext.app'
license=('MIT')
depends=('electron7'
         'libxkbfile'
         'libsecret'
         'ripgrep')
makedepends=('jq'
             'nodejs-lts-erbium'
             'node-gyp'
             'moreutils'
             'yarn'
             'yq')
conflicts=("$_pkgname")
provides=("$_pkgname-$pkgver")
source=("$pkgname::git+https://github.com/$_pkgname/${pkgname/-/.}"
        "$_pkgname.sh"
        "$_pkgname-arg-handling.patch")
sha256sums=('SKIP'
            '15a964fcc3f6bd7bf1c03566d35201032aecde994446533cad1f810e9b880f14'
            'c754a1cad52d10a38eeddb9293ce0a4540296c6adbb47eb5311eaaeded150a01')

pkgver() {
    cd "$pkgname"
    git describe --long --tags --abbrev=7 --match="v*" HEAD |
        sed 's/^v//;s/\([^-]*-g\)/r\1/;s/-/./g'
}

prepare() {
    local _electronDist=$(dirname $(realpath $(which electron7)))
    local _electronVersion=$(electron7 --version | sed -e 's/^v//')
    cd "$pkgname"
    jq 'del(.devDependencies["electron"], .scripts["preinstall", "postinstall"])' \
        package.json | sponge package.json
    yq -y ". + {\"electronDist\": \"$_electronDist\", \"electronVersion\": \"$_electronVersion\"}" \
        electron-builder.yml | sponge electron-builder.yml
    mkdir -p "$srcdir/node_modules"
    yarn --cache-folder "$srcdir/node_modules" install --frozen-lockfile
    yarn --cache-folder "$srcdir/node_modules" add -D -E --no-lockfile --ignore-scripts electron@$_electronVersion
    patch -p1 < "$srcdir/$_pkgname-arg-handling.patch"
}

build() {
    cd "$pkgname"
    yarn --cache-folder "$srcdir/node_modules" run electron-rebuild
    node .electron-vue/build.js
    yarn --cache-folder "$srcdir/node_modules" run \
        electron-builder --linux --x64 --dir dist
}

package() {
    cd "$pkgname"
    install -Dm755 "../$_pkgname.sh" "$pkgdir/usr/bin/$_pkgname"
    local _dist=build/linux-unpacked/resources
    install -Dm644 -t "$pkgdir/usr/lib/$_pkgname/" "$_dist/app.asar"
    cp -a "$_dist"/{app.asar.unpacked,hunspell_dictionaries} "$pkgdir/usr/lib/$_pkgname/"
    local _rg_path="$pkgdir/usr/lib/marktext/app.asar.unpacked/node_modules/vscode-ripgrep/bin/"
    mkdir -p $_rg_path
    ln -sf /usr/bin/rg "$_rg_path"
    install -Dm755 -t "${pkgdir}/usr/share/applications/" resources/linux/marktext.desktop
    install -Dm755 -t "${pkgdir}/usr/share/metainfo/" resources/linux/marktext.appdata.xml
    install -Dm644 resources/icons/icon.png "${pkgdir}/usr/share/pixmaps/marktext.png"
    install -Dm644 -t "$pkgdir/usr/share/licenses/$pkgname/" LICENSE
    install -Dm644 -t "$pkgdir/usr/share/doc/$pkgname/" README.md CONTRIBUTING.md
    cp -a docs "$pkgdir/usr/share/doc/$pkgname/"
    pushd "resources/icons"
    find -name maktext.png -exec install -Dm644 {} "$pkgdir/usr/share/icons/hicolor/{}" \;
}
