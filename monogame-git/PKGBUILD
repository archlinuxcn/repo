pkgname=monogame-git
pkgver=v3.2.2792
pkgrel=1
pkgdesc="XNA Implementation for Mono based platforms (git)"
arch=(i686 x86_64)
license=("Microsoft Public License")
depends=(opentk sdl_mixer sdl_ttf sdl_image sdl_net smpeg sdl_gfx)
makedepends=(nant nvidia-texture-tools dos2unix monodevelop sharpfont assimp-net)
conflicts=(monogame tao-framework tao-framework-svn)
provides=(monogame)
url="http://monogame.codeplex.com"
source=("${pkgname%-*}::git+https://github.com/mono/MonoGame.git"
"Dependencies::git+https://github.com/Mono-Game/MonoGame.Dependencies.git"
"monogame.pc.in"
"mgcb.sh")
md5sums=(SKIP 
SKIP
'ca37d66293d3aac43cac32628ed5d6b6'
'3cad3825e124ea7b7d060ba492adee47')

pkgver () {
	cd "$srcdir/${pkgname%-*}"
	git describe | sed 's|\(.*-.*\)-.*|\1|;s|-|.|'
}

prepare() {
	cd "$srcdir/Dependencies"
	find . -type f -exec dos2unix {} \;
	cd ../${pkgname%-*}/ThirdParty/Dependencies
	cp -r ../../../Dependencies/* .
	cd ../..
	find . -name '*.csproj' -exec sed -i 's,<DebugType>none,<DebugType>pdbonly,g' {} \;
	cd ProjectTemplates/MonoDevelop/MonoDevelop.MonoGame/MonoDevelop.MonoGame
	sed -i -e "s,assemblies/WindowsGL,/usr/lib/monogame,g" -e "s,\"3\.0\",\"${_mdver}\",g" MonoDevelop.MonoGame.addin.xml
}

build() {
	cd "${srcdir}/${pkgname%-*}"
  mono Protobuild.exe
  nant build_linux
  cd ProjectTemplates/MonoDevelop/MonoDevelop.MonoGame
  xbuild MonoDevelop.MonoGame.sln /p:Configuration=ReleaseLinux
  cd ../../../
  xbuild MonoGame.Framework.Linux.sln /p:Configuration=Release
}

package() {
	cd "${srcdir}/${pkgname%-*}/MonoGame.ContentPipeline"
  install -Dm644 MonoGame.ContentPipeline.targets "$pkgdir/usr/lib/mono/xbuild/MonoGame.ContentPipeline.targets"
  cd ../MonoGame.Framework/bin/Linux/AnyCPU/Release
  find . -name 'MonoGame.Framework.dll*' -exec install -Dm644 {} "$pkgdir/usr/lib/monogame/"{} \;
  find . -name 'Lidgren.Network.dll*' -exec install -m644 {} "$pkgdir/usr/lib/monogame/"{} \;
  find . -name 'Tao.Sdl.dll*' -exec install -m644 {} "$pkgdir/usr/lib/monogame/"{} \;
  find . -name '*.mgfxo' -exec install -m644 {} "$pkgdir/usr/lib/monogame/"{} \;
  cd "${srcdir}/${pkgname%-*}/MonoGame.Framework.Content.Pipeline/bin/Linux/AnyCPU/Release"
  find . -name 'MonoGame.Framework.Content.Pipeline.dll*' -exec install -m644 {} "$pkgdir/usr/lib/monogame/"{} \;
  find . -name 'Nvidia.TextureTools.dll*' -exec install -m644 {} "$pkgdir/usr/lib/monogame/"{} \;
  install -m644 ManagedPVRTC.dll "$pkgdir/usr/lib/monogame/"
  cd "${srcdir}/${pkgname%-*}/ProjectTemplates/MonoDevelop/MonoDevelop.MonoGame/MonoDevelop.MonoGame/bin/Linux/Release"
  find . -type f -exec install -Dm644 {} "$pkgdir/usr/lib/monodevelop/AddIns/MonoDevelop.MonoGame/"{} \;
  cd "${srcdir}/${pkgname%-*}/Tools/MGCB/bin/Linux/AnyCPU/Release"
  find . -name 'MGCB.Linux.exe*' -exec install -m644 {} "$pkgdir/usr/lib/monogame/"{} \;
  cd "$pkgdir/usr/lib/monogame"
  gacutil -i Tao.Sdl.dll -root "$pkgdir/usr/lib"
  install -Dm644 "${srcdir}/${pkgname%-*}/LICENSE.txt" "$pkgdir/usr/share/licenses/monogame/LICENSE.txt"
  install -Dm755 "$srcdir/mgcb.sh" "$pkgdir/usr/bin/mgcb"
  install -Dm644 "$srcdir/monogame.pc.in" "$pkgdir/usr/lib/pkgconfig/monogame.pc"
  sed -i "s|@VERSION@|$pkgver|" "$pkgdir/usr/lib/pkgconfig/monogame.pc"
}
