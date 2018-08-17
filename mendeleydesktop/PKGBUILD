# Maintainer: xgdgsc <xgdgsc at gmail dot com>
# Maintainer: Alesandar Trifunović <akstrfn at gmail dot com>

pkgname=mendeleydesktop
pkgver=1.19.2
pkgrel=1
pkgdesc="Academic software for managing and sharing research papers (desktop client)"
url=http://www.mendeley.com/release-notes/
arch=(i686 x86_64)
depends=(qt5-webengine)
license=(custom:mendeley_eula)
source_i686=("https://desktop-download.mendeley.com/download/linux/$pkgname-$pkgver-linux-i486.tar.bz2")
source_x86_64=("https://desktop-download.mendeley.com/download/linux/$pkgname-$pkgver-linux-x86_64.tar.bz2")
sha512sums_i686=('b8b8b291a2b2d3cf43ec96005f891b9acd73090c945252b0b22abbc71c631bd74c9cf600c3c5e2c75ee3784a3ac3d06d8d925b5a70a3e47e34901047f67ca587')
sha512sums_x86_64=('ddcbac4f863706f1226157a4528d89801502af6d5af105558ee1b3a5ecad4ba4c90ff64dffd822f485d45670c6ad54cae93f9a582a5bc82bc23e404c767aca40')

if [[ $CARCH = i686 ]];then
$CARCH=i486
fi

prepare() {
    cd "$pkgname-$pkgver-linux-$CARCH"
    # Using shared libraries so remove the bundled ones
    rm -rf lib/cpp lib/qt lib/ssl lib/libpng12.so.0 lib/mendeleydesktop/plugins
    rm -rf lib/mendeleydesktop/libexec/resources
    rm -rf lib/mendeleydesktop/libexec/translations/qtwebengine_locales

    # TODO Run install-mendeley-link-handler.sh for gconf or just remove it?
    rm bin/install-mendeley-link-handler.sh

    # # Remove unneeded lines if gconf is not installed.
    # if ! which gconftool-2 &>/dev/null;then
    # sed -i '/GCONF/d' \
    #     "$pkgdir"/opt/"$pkgname"/bin/install-mendeley-link-handler.sh
    # fi
}

package() {
    cd "$pkgname-$pkgver-linux-$CARCH"

    # Link system Qt
    ln -s /usr/share/qt/resources \
          lib/mendeleydesktop/libexec/
    ln -s /usr/share/qt/translations/qtwebengine_locales \
          lib/mendeleydesktop/libexec/translations/

    install -d "$pkgdir/opt/$pkgname/"
    cp -a bin lib share "$pkgdir/opt/$pkgname/"

    # Replace default python laucher with custom bash
cat <<'EOF' > "$pkgdir/opt/$pkgname/bin/mendeleydesktop"
#!/bin/bash
export LD_LIBRARY_PATH=/usr/lib/:/opt/mendeleydesktop/lib/:/usr/lib/qt/
export MENDELEY_BUNDLED_QT_PLUGIN_PATH=/lib/qt/plugins/
/opt/mendeleydesktop/lib/mendeleydesktop/libexec/mendeleydesktop.x86_64 "$@"
EOF

    install -d "$pkgdir"/usr/bin
    ln -s "/opt/$pkgname/bin/mendeleydesktop" \
          "$pkgdir/usr/bin/mendeleydesktop"

    install -Dm644 LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
    install -Dm644 share/applications/mendeleydesktop.desktop \
                   "$pkgdir"/usr/share/applications/mendeleydesktop.desktop

    cp -a "$pkgdir/opt/$pkgname/share/icons" "$pkgdir/usr/share/icons"

    # Clean share from opt (don't remove mendeleydesktop)
    rm -rf "$pkgdir/opt/$pkgname/share/"{applications,doc,icons}
}
