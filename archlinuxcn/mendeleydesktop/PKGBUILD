# Maintainer: xgdgsc <xgdgsc at gmail dot com>
# Maintainer: Alesandar Trifunović <akstrfn at gmail dot com>

pkgbase=mendeleydesktop
pkgname=('mendeleydesktop'
         'mendeleydesktop-bundled')
pkgver=1.19.6
pkgrel=1
pkgdesc="Academic software for managing and sharing research papers."
url=http://www.mendeley.com/release-notes/
arch=(i686 x86_64)
license=(custom:mendeley_eula)
source_i686=("https://desktop-download.mendeley.com/download/linux/$pkgbase-$pkgver-linux-i486.tar.bz2")
source_x86_64=("https://desktop-download.mendeley.com/download/linux/$pkgbase-$pkgver-linux-x86_64.tar.bz2")
sha512sums_i686=('8d610043abb325a8396256b4e6fca53db9198be7fecad0128120e79279b5ea048240fd98ccb9833d885eb9f9873b8479e184e4103455528d6a897011f798e2f0')
sha512sums_x86_64=('7baebb8e20b7fb47ae49c5d8378469fb30f74f36033b8d9820ccf2b5559a184ec848a2463464c42d526d42c9c111c47e440e3dbf681b4e87dc5eafb9a42cf8ef')

if [[ $CARCH = i686 ]];then
    $CARCH=i486
fi

prepare() {
    cp -a "$pkgbase-$pkgver-linux-$CARCH" "mendeley-native"
}

package_mendeleydesktop() {
    depends=('qt5-webengine')
    cd "mendeley-native"

    # Using shared libraries so remove the bundled ones
    rm -rf lib/cpp lib/qt lib/ssl lib/libpng12.so.0 lib/mendeleydesktop/plugins
    rm -rf lib/mendeleydesktop/libexec/resources
    rm -rf lib/mendeleydesktop/libexec/translations/qtwebengine_locales

    # TODO Run install-mendeley-link-handler.sh for gconf or just remove it?
    rm bin/install-mendeley-link-handler.sh

    # # Remove unneeded lines if gconf is not installed.
    # if ! which gconftool-2 &>/dev/null;then
    # sed -i '/GCONF/d' \
    #     "$pkgdir"/opt/"$pkgbase"/bin/install-mendeley-link-handler.sh
    # fi

    # Link system Qt
    ln -s /usr/share/qt/resources \
          lib/mendeleydesktop/libexec/
    ln -s /usr/share/qt/translations/qtwebengine_locales \
          lib/mendeleydesktop/libexec/translations/

    install -d "$pkgdir/opt/$pkgbase/"
    cp -a bin lib share "$pkgdir/opt/$pkgbase/"

    # Replace default python laucher with custom bash
cat <<'EOF' > "$pkgdir/opt/$pkgbase/bin/mendeleydesktop"
#!/bin/bash
export LD_LIBRARY_PATH=/usr/lib/:/opt/mendeleydesktop/lib/:/usr/lib/qt/
export MENDELEY_BUNDLED_QT_PLUGIN_PATH=/lib/qt/plugins/
/opt/mendeleydesktop/lib/mendeleydesktop/libexec/mendeleydesktop.x86_64 "$@"
EOF

    install -d "$pkgdir"/usr/bin
    ln -s "/opt/$pkgbase/bin/mendeleydesktop" \
          "$pkgdir/usr/bin/mendeleydesktop"

    install -Dm644 LICENSE "$pkgdir/usr/share/licenses/$pkgbase/LICENSE"
    install -Dm644 share/applications/mendeleydesktop.desktop \
                   "$pkgdir"/usr/share/applications/mendeleydesktop.desktop

    cp -a "$pkgdir/opt/$pkgbase/share/icons" "$pkgdir/usr/share/icons"

    # Clean share from opt (don't remove mendeleydesktop)
    rm -rf "$pkgdir/opt/$pkgbase/share/"{applications,doc,icons}
}

package_mendeleydesktop-bundled() {
    provides=('mendeleydesktop')
    conflicts=('mendeleydesktop')
    cd "$pkgbase-$pkgver-linux-$CARCH"

    sed -i 's/Exec=/&env LD_LIBRARY_PATH=\/opt\/mendeleydesktop\/lib\/mendeleydesktop\/plugins\/platforms /' bin/install-mendeley-link-handler.sh

    install -d "$pkgdir/opt/$pkgbase"
    cp -a bin lib share "$pkgdir/opt/$pkgbase/"


    install -d "$pkgdir"/usr/bin
    ln -s "/opt/$pkgbase/bin/mendeleydesktop" \
          "$pkgdir/usr/bin/mendeleydesktop"

    install -Dm644 LICENSE "$pkgdir/usr/share/licenses/$pkgbase/LICENSE"
    install -Dm644 share/applications/mendeleydesktop.desktop \
                   "$pkgdir"/usr/share/applications/mendeleydesktop.desktop

    cp -a "$pkgdir/opt/$pkgbase/share/icons" "$pkgdir/usr/share/icons"

    # Clean share from opt (don't remove mendeleydesktop)
    rm -rf "$pkgdir/opt/$pkgbase/share/"{applications,doc,icons}
}
