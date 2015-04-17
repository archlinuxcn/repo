#Maintainer:xgdgsc<xgdgsc@gmail.com>

pkgname=mendeleydesktop
pkgver=1.13.8
pkgrel=1
pkgdesc="Academic software for managing and sharing research papers (desktop client)"
url=http://www.mendeley.com/release-notes/
arch=(i686 x86_64)
depends=(python2 qtwebkit)
license=(custom:mendeley_eula)
install=mendeleydesktop.install
md5sums=('' '44c54032370c2a7cbc6667af6d19acf7')


if [[ $CARCH = i686 ]];then
  _arch=i486
  md5sums[0]='79a33509d049a4fa5c139708109edc4a'

else
  _arch=$CARCH
  md5sums[0]='850dc2c604d8cd09ffaf1fd8d5cda615'
fi

if which gconftool-2 &>/dev/null;then
  depends=(${depends[@]} gconf)
fi

#http://desktop-download.mendeley.com/download/linux/mendeleydesktop-1.13.-linux-i486.tar.bz2
#http://desktop-download.mendeley.com/download/linux/mendeleydesktop-1.13.-linux-x86_64.tar.bz2
source=("http://desktop-download.mendeley.com/download/linux/$pkgname-$pkgver-linux-$_arch.tar.bz2"
        'mendeleydesktop.install')

package() {
    cd "$pkgname-$pkgver-linux-$_arch"

    rm -f share/doc/mendeleydesktop/*.txt

    install -dm755 "$pkgdir/opt/$pkgname/"
    mv bin lib share "$pkgdir/opt/$pkgname/"
    #ln -s "../lib/mendeleydesktop/libexec/mendeleydesktop.$_arch" "$pkgdir/opt/$pkgname/bin/$pkgname"
    cd "$pkgdir"
    sed -i '1s@^#!/usr/bin/python$@&2@' opt/"$pkgname"/bin/mendeleydesktop
    #install -Dm755 "bin/mendeleydesktop" "$pkgdir/usr/bin/mendeleydesktop"
    install -dm755 "$pkgdir"/usr/bin
    ln -s /opt/"$pkgname"/bin/mendeleydesktop "$pkgdir/usr/bin/mendeleydesktop"

    cd "$srcdir/$pkgname-$pkgver-linux-$_arch"
    install -Dm644 LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"

    install -dm755 "$pkgdir"/usr/share/applications
    ln -s /opt/"$pkgname"/share/applications/mendeleydesktop.desktop "$pkgdir"/usr/share/applications/

    #Romove bundled Qt from package
    cat << __EOF__
Removing bundled Qt library.
If you used "--force-bundled-qt" to start mendeley,
make sure you remove any old versions of ".desktop" file of mendeley in ~/.local/share/applications/,
because mendeley will automatically create one there.
__EOF__
    rm -rf "$pkgdir"/opt/"$pkgname"/lib/qt

    #Remove unneeded lines if gconf is not installed.
    if ! which gconftool-2 &>/dev/null;then
    sed -i '6d;74d;75d' \
        "$pkgdir"/opt/"$pkgname"/bin/install-mendeley-link-handler.sh
    fi
    #force mendeley to use bundled qt because which under qt 4.8 crashes at start point
    #make sure you remove any old versions of ".desktop" file of mendeley in ~/.local/share/applications/
#    sed -i 's/^Exec.*$/& --force-bundled-qt/' "$pkgdir"/opt/"$pkgname"/share/applications/mendeleydesktop.desktop
    for size in 16 22 32 48 64 128;do
        install -dm755 "$pkgdir"/usr/share/icons/hicolor/${size}x${size}/apps
        ln -s /opt/"$pkgname"/share/icons/hicolor/${size}x${size}/apps/"${pkgname}".png \
          "$pkgdir"/usr/share/icons/hicolor/${size}x${size}/apps
    done
}
