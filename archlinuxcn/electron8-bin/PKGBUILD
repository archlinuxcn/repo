# Maintainer: Daniel Peukert <daniel@peukert.cc>
# Contributor: Nicola Squartini <tensor5@gmail.com> (electron-launcher.sh script)
# Contributor: Tom Vincent <http://tlvince.com/contact/>
_projectname='electron'
_pkgname="${_projectname}8"
pkgname="$_pkgname-bin"
pkgver='8.5.5'
pkgrel='5'
epoch='1'
pkgdesc='Build cross platform desktop apps with web technologies - version 8 - binary version'
arch=('x86_64' 'i686' 'pentium4' 'armv7h' 'aarch64')
url="https://${_projectname}js.org"
license=('MIT')
provides=("$_pkgname")
conflicts=("$_pkgname")
depends=('c-ares' 'ffmpeg' 'gtk3' 'http-parser' 'libevent' 'libxslt' 'libxss' 'minizip' 'nss' 're2' 'snappy')
optdepends=(
	'kde-cli-tools: file deletion support (kioclient5)'
	'libappindicator-gtk3: StatusNotifierItem support'
	'trash-cli: file deletion support (trash-put)'
	"xdg-utils: open URLs with desktop's default (xdg-email, xdg-open)"
)
_releaseurl="https://github.com/$_projectname/$_projectname/releases/download/v$pkgver"
source_x86_64=(
	"$pkgname-chromedriver-$pkgver-x86_64.zip::$_releaseurl/chromedriver-v$pkgver-linux-x64.zip"
	"$pkgname-$pkgver-x86_64.zip::$_releaseurl/$_projectname-v$pkgver-linux-x64.zip"
)
source_i686=(
	"$pkgname-chromedriver-$pkgver-i686.zip::$_releaseurl/chromedriver-v$pkgver-linux-ia32.zip"
	"$pkgname-$pkgver-i686.zip::$_releaseurl/$_projectname-v$pkgver-linux-ia32.zip"
)
source_pentium4=(
	"$pkgname-chromedriver-$pkgver-pentium4.zip::$_releaseurl/chromedriver-v$pkgver-linux-ia32.zip"
	"$pkgname-$pkgver-pentium4.zip::$_releaseurl/$_projectname-v$pkgver-linux-ia32.zip"
)
source_armv7h=(
	"$pkgname-chromedriver-$pkgver-armv7h.zip::$_releaseurl/chromedriver-v$pkgver-linux-armv7l.zip"
	"$pkgname-$pkgver-armv7h.zip::$_releaseurl/$_projectname-v$pkgver-linux-armv7l.zip"
)
source_aarch64=(
	"$pkgname-chromedriver-$pkgver-aarch64.zip::$_releaseurl/chromedriver-v$pkgver-linux-arm64.zip"
	"$pkgname-$pkgver-aarch64.zip::$_releaseurl/$_projectname-v$pkgver-linux-arm64.zip"
)
source=('electron-launcher.sh')
sha512sums=('e38d31100ed4d7a435f7a1ae5eb2e7f68a58003789c1bd2708ee1b1f3ad847b9a21182295bf704f06269014c226688dd1fa99017229137cafe69f3fc61b9b72c')
sha512sums_x86_64=('2d6d314b17c10bb4c567be1443c973955074b1591dab24beca2e5575187e4071e0bbb2b201857a86cee5d793f0bf1283beaa56255ef26330d92f0a627bca98f1'
                   '6e58b1d0f009cde205b8d06bad5df3f1a1457308d6045cd65eae0246d874d810dc1bec0ba51ccc0d7e1f4a32399c678c017377e218ed09e339b6f5c2419dc21c')
sha512sums_i686=('22dc96a8bcacc685cc9cdc53ae03c24e48637c59374d29e4a5fe84206919a920add3b1c7da1afce71bc9722481bc33b0302728edc84a74570ebe8848605036b7'
                 '8d00540024a96e3cc36ca0506cece5fa96c1a0ef884290e47097e7aa2b15cc52bfa66697f14bcc0f8d7973ad2a8b33992d76f64063b0f405dd63682ec91f8bcc')
sha512sums_pentium4=('22dc96a8bcacc685cc9cdc53ae03c24e48637c59374d29e4a5fe84206919a920add3b1c7da1afce71bc9722481bc33b0302728edc84a74570ebe8848605036b7'
                     '8d00540024a96e3cc36ca0506cece5fa96c1a0ef884290e47097e7aa2b15cc52bfa66697f14bcc0f8d7973ad2a8b33992d76f64063b0f405dd63682ec91f8bcc')
sha512sums_armv7h=('2b1587e06b54dd25210e3dfd0aa40e376c7ed69c3776974e0a80f662de92300d0f2555e41003651fa5bafba37c20f0e6372c9991f428bdcb438c5a82c2ec0d1b'
                   'd774af6c894ad393407752e240885cecc4eacf70cda45c9d1f6453795b13fe6d22580a5971311888ca0916e7465ec58c80c1d653eea65c8c28af3aae56638241')
sha512sums_aarch64=('0708979c3ce47ff473d8a07f49cd444a18744554d0b7492ac3aa0850cf039e343c688f93700a5dc434ce4908eda4921b81b445e9de8bc74c2219e192b1f88d17'
                    '423a7da2ebd669a91124daf93a0f4a5a75bf3d2f445eed1e9e8aca724fb4d51a0b7b843425eb0a397fab96b25f180463f16eed8feaf4f4a6baa558c241becd3a')

prepare() {
	sed -i -e "s/%%PKGNAME%%/$_pkgname/g" -e "s/%%PROJECTNAME%%/$_projectname/g" "$srcdir/electron-launcher.sh"
}

package() {
	cd "$srcdir/"
	install -dm755 "$pkgdir/usr/lib/$_pkgname/"
	find . -mindepth 1 -maxdepth 1 -type f ! -name "*.zip" ! -name "LICENSE*" -exec cp -r --no-preserve=ownership --preserve=mode -t "$pkgdir/usr/lib/$_pkgname/." {} +

	for _folder in 'locales' 'resources' 'swiftshader'; do
		cp -r --no-preserve=ownership --preserve=mode "$_folder/" "$pkgdir/usr/lib/$_pkgname/$_folder/"
	done

	chmod u+s "$pkgdir/usr/lib/$_pkgname/chrome-sandbox"

	install -Dm755 'electron-launcher.sh' "$pkgdir/usr/bin/$_pkgname"

	for _license in 'LICENSE' 'LICENSES.chromium.html'; do
		install -Dm644 "$_license" "$pkgdir/usr/share/licenses/$pkgname/$_license"
	done
}
