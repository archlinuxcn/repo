# Maintainer: Pavan Rikhi <pavan.rikhi@gmail.com>
pkgname=pencil
pkgver=3.1.0
pkgrel=3
pkgdesc="Sketching and GUI prototyping/wireframing tool"
arch=('any')
license=('GPL2')
url="http://github.com/evolus/pencil"
source=("https://github.com/evolus/pencil/archive/v$pkgver.tar.gz"
        "pencil.desktop"
        "pencil-mime.xml"
        "fixed-package.json")
sha256sums=('e14eddd0aad28919cfdf8d47b726f9c75a3a0d2042605e8da96309c23a995f44'
            '6d467da74509e74e06325e7464a6a177164ae8977470423da6cae43265dedd4d'
            '87aac9f5005ccd57aa6b1bf190052fcc4915eff1d7bddb2723863739545e42fc'
            '6f0902d9d2294865b8993c94ce4f01dd01318c7da428dad5a45b7753c46ad757')
conflicts=('evolus-pencil-bin' 'pencil-v2')
depends=('nodejs' 'npm' 'libxss' 'nss' 'libxtst' 'gtk2' 'alsa-lib')

package() {
    cd "$srcdir/$pkgname-$pkgver"

    if [ -d "$HOME" ]; then
        TMP_HOME="$HOME"
    else
        TMP_HOME="$(pwd)/tmp-home"
        mkdir -p "$TMP_HOME/.config"
    fi

    # Temporary fix of package.json for v3.1.0 builds.
    cp -f "$srcdir/fixed-package.json" package.json

    HOME="$TMP_HOME" npm ci --unsafe-perm
    HOME="$TMP_HOME" node_modules/.bin/build --linux dir

    install -d "$pkgdir/usr/share/$pkgname/" "$pkgdir/usr/bin" \
        "$pkgdir/usr/share/applications" "$pkgdir/usr/share/mime/packages"

    cp -r dist/linux-unpacked/* "$pkgdir/usr/share/$pkgname/"
    cp app/css/images/logo-shadow.png "$pkgdir/usr/share/$pkgname/icon.png"

    install -m644 "$srcdir/pencil.desktop" "$pkgdir/usr/share/applications/"
    cp "$srcdir/pencil-mime.xml" "$pkgdir/usr/share/mime/packages/"

    ln -s "/usr/share/$pkgname/pencil" "$pkgdir/usr/bin/"
}
