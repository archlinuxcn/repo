# Maintainer: William McKIE <mckie.william@hotmail.co.uk>
pkgname=monogame-git
pkgver=3.5
pkgrel=1
pkgdesc="Open Source implementation of the Microsoft XNA 4 Framework."
arch=('any')
url="http://www.monogame.net/"
license=('Microsoft Public License (Ms-PL)')
groups=('any')
depends=('freeimage' 'ffmpeg' 'gtk-sharp-3' 'openal' 'opentk')
makedepends=('git' 'nvidia-texture-tools' 'dos2unix' 'monodevelop' 'sharpfonts' 'assimp-net')
conflicts=('monogame' 'tao-framework' 'tao-framework-svn')
provides=('monogame')
source=('git+https://github.com/mono/MonoGame.git'
		'monogame.pc.in'
		'mgcb.sh'
        # '2mgfx.sh'
		'monogame-pipeline.sh')
md5sums=('SKIP'
         'c41ca3ef34fc31b114b77bdff626c5a0'
         'a0ff773f5647651148ecb443a29b9ea9'
         '46a2caa68e21fd99aa4b30b78ab1a109')

prepare() {
	cd "${srcdir}/MonoGame"
	git checkout --detach v${pkgver}
	git submodule update --init --recursive
	cd "${srcdir}/MonoGame/ThirdParty/Dependencies"
	find . -type f -exec dos2unix {} \;
}

build() {
	cd "${srcdir}/MonoGame"
	mono Protobuild.exe
	cd "${srcdir}/MonoGame/IDE/MonoDevelop/MonoDevelop.MonoGame"
	xbuild MonoDevelop.MonoGame.csproj /p:Configuration=Release
	cd "${srcdir}/MonoGame"
	xbuild MonoGame.Framework.Linux.sln /p:Configuration=Release
}

package() {
    # Assemblies
	cd "${srcdir}/MonoGame/MonoGame.Framework/bin/Linux/AnyCPU/Release"
	find . -name 'MonoGame.Framework.*' -exec install -Dm644 {} "${pkgdir}/usr/lib/monogame/"{} \;
	find . -name 'Lidgren.Network.*' -exec install -Dm644 {} "${pkgdir}/usr/lib/monogame/"{} \;

    # Pipeline
	cd "${srcdir}/MonoGame/MonoGame.Framework.Content.Pipeline/bin/Linux/AnyCPU/Release"
	find . -name 'MonoGame.Framework.Content.Pipeline.*' -exec install -Dm644 {} "${pkgdir}/usr/lib/monogame/"{} \;
	find . -name 'Nvidia.TextureTools.*' -exec install -Dm644 {} "${pkgdir}/usr/lib/monogame/"{} \;
	find . -name 'ManagedPVRTC.*' -exec install -Dm644 {} "${pkgdir}/usr/lib/monogame/"{} \;
	find . -name 'FreeImageNET.*' -exec install -Dm644 {} "${pkgdir}/usr/lib/monogame/"{} \;
	find . -name 'NVorbis.*' -exec install -Dm644 {} "${pkgdir}/usr/lib/monogame/"{} \;
	find . -name 'PVRTexLibNET.*' -exec install -Dm644 {} "${pkgdir}/usr/lib/monogame/"{} \;
	find . -name 'ATI.TextureConverter.*' -exec install -Dm644 {} "${pkgdir}/usr/lib/monogame/"{} \;

    # AddIns
    cd "${srcdir}/MonoGame/IDE/MonoDevelop/bin/Release"
	find . -type f -exec install -Dm644 {} "${pkgdir}/usr/lib/monodevelop/AddIns/MonoDevelop.MonoGame/"{} \;

    # Tools
    cd "${srcdir}/MonoGame/Tools/Pipeline/bin/Linux/AnyCPU/Release"
	find . -name 'MGCB.*' -exec install -Dm644 {} "${pkgdir}/usr/lib/monogame/"{} \;
	find . -name 'Pipeline.*' -exec install -Dm644 {} "${pkgdir}/usr/lib/monogame/"{} \;
	find ./Templates -type f -exec install -Dm644 {} "${pkgdir}/usr/lib/monogame/"{} \;

    # NOTE: For now, there is no official linux release of 2MGFX tool
    #  SEE: http://community.monogame.net/t/compiling-effects-on-linux/2089
    # cd "${srcdir}/MonoGame/Tools/2MGFX/bin/Linux/AnyCPU/Release"
	# find . -name '2MGFX.*' -exec install -Dm644 {} "${pkgdir}/usr/lib/monogame/"{} \;

    # Install
	install -Dm644 "${srcdir}/MonoGame/LICENSE.txt" "${pkgdir}/usr/share/licenses/monogame/LICENSE.txt"
	install -Dm755 "${srcdir}/mgcb.sh" "${pkgdir}/usr/bin/mgcb"
    # install -Dm755 "${srcdir}/2mgfx.sh" "${pkgdir}/usr/bin/2mgfx"
	install -Dm755 "${srcdir}/monogame-pipeline.sh" "${pkgdir}/usr/bin/monogame-pipeline"
	install -Dm644 "${srcdir}/monogame.pc.in" "${pkgdir}/usr/lib/pkgconfig/monogame.pc"
	sed -i "s,@VERSION@,v${pkgver}," "${pkgdir}/usr/lib/pkgconfig/monogame.pc"
}
