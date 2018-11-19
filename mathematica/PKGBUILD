# Maintainer: Joshua Ellis <josh@jpellis.me>
# Contributor: Anish Tondwalkar <anish@tjhsst.edu>
# Contributor: Ghost91 <m_graeb11@cs.uni-kl.de>
# Contributor: Michael Pusterhofer <pusterhofer at student dot tugraz dot at>
# Contributor: Raphael Scholer <rscholer@gmx.de>
# Contributor: kjslag <kjslag at gmail dot com>
# Contributor: teratomata <teratomat@gmail.com>

pkgname=mathematica
pkgver=11.3.0
pkgrel=3
pkgdesc="A computational software program used in scientific, engineering, and mathematical fields and other areas of technical computing."
arch=('i686' 'x86_64')
url="http://www.wolfram.com/mathematica/"
license=('proprietary')
depends=(
    'openmp'
)
optdepends=(
    ## The following list of dependencies was inferred from namcap's output.  If
    ## you believe there is an error, please let me know.  Also feel free to
    ## contribute description to dependencies if you know what they do.
    'alsa-lib'
    'atk'
    'cairo'
    'clucene'
    'cuda'
    'curl'
    'espeak'
    'ffmpeg'
    'fluidsynth'
    'fontconfig'
    'freetype2'
    'gdk-pixbuf2'
    'glib2'
    'glu'
    'gmime'
    'gmp'
    'gtk2'
    'harfbuzz'
    'icu'
    'intel-mkl'
    'java-environment'
    'lame'
    'lcms2'
    'leptonica'
    'libbson'
    'libffi'
    'libjpeg-turbo'
    'libmad'
    'libmongoc'
    'libnet'
    'libogg'
    'libpng12'
    'libselinux'
    'libsm'
    'libssh2'
    'libutil-linux'
    'libwebp'
    'libx11'
    'libxml2'
    'libxslt'
    'libxtst'
    'libxxf86vm'
    'mesa-demos: for improved graphics output'
    'ncurses'
    'nvidia-utils'
    'opencv'
    'openssl-1.0'
    'pango'
    'pixman'
    'portaudio'
    'r'
    'tesseract'
    'zlib'
)
source=("local://Mathematica_${pkgver}_LINUX.sh" "duplicate-libs.txt")
md5sums=('623f9fa3d34ded6997c7b9f1505097c0'
         'e442aa2286a9d93e932076c974517dd7')
options=("!strip")

## To build this package you need to place the mathematica-installer into your
## startdir If you don't own the installer you can download a trial version at
## http://www.wolfram.com/mathematica/trial

## The documentation takes up the majority of the disk space.  If you do not wish
## to keep it, uncomment the relevant lines at the bottom of this PKGBUILD.

## The final package can be very large (especially if documentation is kept) and
## compression can be quite slow.  In most cases, the package is installed
## straight away and the package need not be kept, so compression is disabled.
PKGEXT='.pkg.tar'

prepare() {
    if df "${srcdir}" | grep -q tmpfs; then
        warning "Building Mathematica takes more than 8GB of space."
        warning "Building in a tmpfs (e.g. /tmp when mounted into RAM) may not work."
    fi

    if [ $(echo "${srcdir}" | wc -w) -ne 1 ]; then
        msg2 "ERROR: The Mathematica installer doesn't support directory names with spaces."
        msg2 "Try building from a directory without spaces."
        msg2 "Current build directory: ${srcdir}"
        false
    fi

    chmod +x ${srcdir}/Mathematica_${pkgver}_LINUX.sh
}

package() {
    msg2 "Running Mathematica installer"
    # https://reference.wolfram.com/language/tutorial/InstallingMathematica.html#650929293
    sh ${srcdir}/Mathematica_${pkgver}_LINUX.sh -- \
             -execdir=${pkgdir}/usr/bin \
             -targetdir=${pkgdir}/opt/Mathematica \
             -auto
    msg2 "Errors related to 'xdg-icon-resource' and 'xdg-desktop-menu' are to be expected during Mathematica's installation."

    msg2 "Fixing symbolic links"
    cd ${pkgdir}/opt/Mathematica/Executables
    rm wolframscript
    if [ "${CARCH}" = "x86_64" ]; then
        ln -s /opt/Mathematica/SystemFiles/Kernel/Binaries/Linux-x86-64/wolframscript
    else
        ln -s /opt/Mathematica/SystemFiles/Kernel/Binaries/Linux/wolframscript
    fi
    cd ${pkgdir}/usr/bin
    rm *
    ln -s /opt/Mathematica/Executables/math
    ln -s /opt/Mathematica/Executables/mathematica
    ln -s /opt/Mathematica/Executables/Mathematica
    ln -s /opt/Mathematica/Executables/MathKernel
    ln -s /opt/Mathematica/Executables/mcc
    ln -s /opt/Mathematica/Executables/wolfram
    ln -s /opt/Mathematica/Executables/WolframKernel
    if [ "${CARCH}" = "x86_64" ]; then
        ln -s /opt/Mathematica/SystemFiles/Kernel/Binaries/Linux-x86-64/ELProver
        ln -s /opt/Mathematica/SystemFiles/Kernel/Binaries/Linux-x86-64/wolframscript
    else
        ln -s /opt/Mathematica/SystemFiles/Kernel/Binaries/Linux/ELProver
        ln -s /opt/Mathematica/SystemFiles/Kernel/Binaries/Linux/wolframscript
    fi

    msg2 "Setting up WolframScript"
    mkdir -p ${srcdir}/WolframScript
    mkdir -p ${pkgdir}/usr/share/
    cd ${srcdir}/WolframScript
    bsdtar -xf ${pkgdir}/opt/Mathematica/SystemFiles/Installation/wolframscript_1.2.0-36_amd64.deb data.tar.gz
    tar -xf data.tar.gz -C ${pkgdir}/usr/share/ --strip=3 ./usr/share/


    msg2 "Copying menu and mimetype information"
    mkdir -p \
          ${pkgdir}/usr/share/applications \
          ${pkgdir}/usr/share/desktop-directories \
          ${pkgdir}/usr/share/mime/packages
    cd ${pkgdir}/opt/Mathematica/SystemFiles/Installation
    desktopFile='wolfram-mathematica11.desktop'
    sed -Ei 's|^(\s*TryExec=).*|\1/usr/bin/Mathematica|g' $desktopFile
    sed -Ei 's|^(\s*Exec=).*|\1/usr/bin/Mathematica %F|g' $desktopFile
    printf 'Categories=Science;Math;NumericalAnalysis;DataVisualization;' >> $desktopFile
    cp $desktopFile ${pkgdir}/usr/share/applications/
    cp wolfram-all.directory ${pkgdir}/usr/share/desktop-directories/
    cp *.xml ${pkgdir}/usr/share/mime/packages/

    msg2 "Copying icons"
    mkdir -p ${pkgdir}/usr/share/icons/hicolor/{32x32,64x64,128x128}/{apps,mimetypes}
    cd ${pkgdir}/opt/Mathematica/SystemFiles/FrontEnd/SystemResources/X
    for i in 32 64 128; do
        cp App-${i}.png ${pkgdir}/usr/share/icons/hicolor/${i}x${i}/apps/wolfram-mathematica.png
        for mimetype in $(ls vnd.* | cut -d '-' -f1 | uniq); do
            cp ${mimetype}-${i}.png ${pkgdir}/usr/share/icons/hicolor/${i}x${i}/mimetypes/application-${mimetype}.png
        done
    done

    msg2 "Copying man pages"
    mkdir -p ${pkgdir}/usr/share/man/man1
    cd ${pkgdir}/opt/Mathematica/SystemFiles/SystemDocumentation/Unix
    cp *.1 ${pkgdir}/usr/share/man/man1

    msg2 "Fixing file permissions"
    chmod go-w -R ${pkgdir}/*

    if [ "${CARCH}" = "x86_64" ]; then
        msg2 "Removing files for i686"
        rm -rf \
           "${pkgdir}/opt/Mathematica/AddOns/Applications/DocumentationSearch/LibraryResources/Linux" \
           "${pkgdir}/opt/Mathematica/AddOns/Applications/StandardOceanData/LibraryResources/Linux" \
           "${pkgdir}/opt/Mathematica/SystemFiles/Activation/Linux" \
           "${pkgdir}/opt/Mathematica/SystemFiles/Autoload/PacletManager/LibraryResources/Linux" \
           "${pkgdir}/opt/Mathematica/SystemFiles/Components/HTTPHandling/Resources/Binaries/Linux" \
           "${pkgdir}/opt/Mathematica/SystemFiles/Components/MXNetLink/LibraryResources/Linux" \
           "${pkgdir}/opt/Mathematica/SystemFiles/Components/MachineLearning/Resources/Binaries/Linux" \
           "${pkgdir}/opt/Mathematica/SystemFiles/Components/NumericArrayUtilities/LibraryResources/Linux" \
           "${pkgdir}/opt/Mathematica/SystemFiles/Components/PredictiveInterface/Kernel/Predictions.mx/Linux" \
           "${pkgdir}/opt/Mathematica/SystemFiles/Components/PredictiveInterface/Kernel/PredictiveInterfaceCode.mx/Linux" \
           "${pkgdir}/opt/Mathematica/SystemFiles/Components/SemanticImport/Binaries/Linux" \
           "${pkgdir}/opt/Mathematica/SystemFiles/Components/SpellCorrect/LibraryResources/Linux" \
           "${pkgdir}/opt/Mathematica/SystemFiles/Components/TextSearch/Binaries/Linux" \
           "${pkgdir}/opt/Mathematica/SystemFiles/Components/WSMCore/SystemModeler/Mathematica/WSMLink/SystemFiles/Libraries/Linux" \
           "${pkgdir}/opt/Mathematica/SystemFiles/Components/WSMCore/SystemModeler/SystemFiles/Activation/Linux" \
           "${pkgdir}/opt/Mathematica/SystemFiles/Components/WSMCore/SystemModeler/SystemFiles/Libraries/Linux" \
           "${pkgdir}/opt/Mathematica/SystemFiles/Components/WSMCore/SystemModeler/SystemFiles/WSM/Binaries/Linux" \
           "${pkgdir}/opt/Mathematica/SystemFiles/Converters/Binaries/Linux" \
           "${pkgdir}/opt/Mathematica/SystemFiles/FrontEnd/Binaries/Linux" \
           "${pkgdir}/opt/Mathematica/SystemFiles/Graphics/Binaries/Linux" \
           "${pkgdir}/opt/Mathematica/SystemFiles/Java/Linux" \
           "${pkgdir}/opt/Mathematica/SystemFiles/Kernel/Binaries/Linux" \
           "${pkgdir}/opt/Mathematica/SystemFiles/Kernel/SystemResources/Linux" \
           "${pkgdir}/opt/Mathematica/SystemFiles/Libraries/Linux" \
           "${pkgdir}/opt/Mathematica/SystemFiles/Links/AudioFileStreamTools/LibraryResources/Linux" \
           "${pkgdir}/opt/Mathematica/SystemFiles/Links/AudioTools/LibraryResources/Linux" \
           "${pkgdir}/opt/Mathematica/SystemFiles/Links/CURLLink/LibraryResources/Linux" \
           "${pkgdir}/opt/Mathematica/SystemFiles/Links/CalendarTools/LibraryResources/Linux" \
           "${pkgdir}/opt/Mathematica/SystemFiles/Links/CloudObject/LibraryResources/Linux" \
           "${pkgdir}/opt/Mathematica/SystemFiles/Links/DTWTools/LibraryResources/Linux" \
           "${pkgdir}/opt/Mathematica/SystemFiles/Links/FDLLink/LibraryResources/Linux" \
           "${pkgdir}/opt/Mathematica/SystemFiles/Links/GIFTools/LibraryResources/Linux" \
           "${pkgdir}/opt/Mathematica/SystemFiles/Links/GeometryTools/LibraryResources/Linux" \
           "${pkgdir}/opt/Mathematica/SystemFiles/Links/HDF5Tools/LibraryResources/Linux" \
           "${pkgdir}/opt/Mathematica/SystemFiles/Links/IPOPTLink/LibraryResources/Linux" \
           "${pkgdir}/opt/Mathematica/SystemFiles/Links/JLink/Kernel/SystemResources/Linux" \
           "${pkgdir}/opt/Mathematica/SystemFiles/Links/JLink/SystemFiles/Libraries/Linux" \
           "${pkgdir}/opt/Mathematica/SystemFiles/Links/JSONTools/LibraryResources/Linux" \
           "${pkgdir}/opt/Mathematica/SystemFiles/Links/LibraryLink/LibraryResources/Linux" \
           "${pkgdir}/opt/Mathematica/SystemFiles/Links/LightGBMLink/LibraryResources/Linux" \
           "${pkgdir}/opt/Mathematica/SystemFiles/Links/MIDITools/LibraryResources/Linux" \
           "${pkgdir}/opt/Mathematica/SystemFiles/Links/MIMETools/LibraryResources/Linux" \
           "${pkgdir}/opt/Mathematica/SystemFiles/Links/MP3Tools/LibraryResources/Linux" \
           "${pkgdir}/opt/Mathematica/SystemFiles/Links/MQTTLink/LibraryResources/Linux" \
           "${pkgdir}/opt/Mathematica/SystemFiles/Links/MQTTLink/Resources/Binaries/Linux" \
           "${pkgdir}/opt/Mathematica/SystemFiles/Links/MathLink/DeveloperKit/Linux" \
           "${pkgdir}/opt/Mathematica/SystemFiles/Links/MongoLink/LibraryResources/Linux" \
           "${pkgdir}/opt/Mathematica/SystemFiles/Links/OGGTools/LibraryResources/Linux" \
           "${pkgdir}/opt/Mathematica/SystemFiles/Links/OpenCVLink/LibraryResources/Linux" \
           "${pkgdir}/opt/Mathematica/SystemFiles/Links/OpenSURF/LibraryResources/Linux" \
           "${pkgdir}/opt/Mathematica/SystemFiles/Links/ProcessLink/LibraryResources/Linux" \
           "${pkgdir}/opt/Mathematica/SystemFiles/Links/RAWTools/LibraryResources/Linux" \
           "${pkgdir}/opt/Mathematica/SystemFiles/Links/RLink/SystemFiles/Libraries/Linux" \
           "${pkgdir}/opt/Mathematica/SystemFiles/Links/SVTools/LibraryResources/Linux" \
           "${pkgdir}/opt/Mathematica/SystemFiles/Links/SerialLink/LibraryResources/Linux" \
           "${pkgdir}/opt/Mathematica/SystemFiles/Links/SocketLink/LibraryResources/Linux" \
           "${pkgdir}/opt/Mathematica/SystemFiles/Links/SoundFileTools/LibraryResources/Linux" \
           "${pkgdir}/opt/Mathematica/SystemFiles/Links/SpeechSynthesisTools/LibraryResources/Linux" \
           "${pkgdir}/opt/Mathematica/SystemFiles/Links/StreamLink/LibraryResources/Linux" \
           "${pkgdir}/opt/Mathematica/SystemFiles/Links/SystemTools/LibraryResources/Linux" \
           "${pkgdir}/opt/Mathematica/SystemFiles/Links/TesseractTools/LibraryResources/Linux" \
           "${pkgdir}/opt/Mathematica/SystemFiles/Links/TetGenLink/LibraryResources/Linux" \
           "${pkgdir}/opt/Mathematica/SystemFiles/Links/TinkerForgeWeatherStationTools/Binaries/Linux" \
           "${pkgdir}/opt/Mathematica/SystemFiles/Links/TriangleLink/LibraryResources/Linux" \
           "${pkgdir}/opt/Mathematica/SystemFiles/Links/UUID/LibraryResources/Linux" \
           "${pkgdir}/opt/Mathematica/SystemFiles/Links/VernierLink/LibraryResources/Linux" \
           "${pkgdir}/opt/Mathematica/SystemFiles/Links/WSTP/DeveloperKit/Linux" \
           "${pkgdir}/opt/Mathematica/SystemFiles/Links/WebpTools/LibraryResources/Linux" \
           "${pkgdir}/opt/Mathematica/SystemFiles/Links/XMPTools/LibraryResources/Linux" \
           "${pkgdir}/opt/Mathematica/SystemFiles/Links/ZeroMQLink/LibraryResources/Linux"
    else
        msg2 "Removing files for x86_64"
        rm -rf \
           "${pkgdir}/opt/Mathematica/AddOns/Applications/DocumentationSearch/LibraryResources/Linux-x86-64" \
           "${pkgdir}/opt/Mathematica/AddOns/Applications/StandardOceanData/LibraryResources/Linux-x86-64" \
           "${pkgdir}/opt/Mathematica/SystemFiles/Activation/Linux-x86-64" \
           "${pkgdir}/opt/Mathematica/SystemFiles/Autoload/PacletManager/LibraryResources/Linux-x86-64" \
           "${pkgdir}/opt/Mathematica/SystemFiles/Components/HTTPHandling/Resources/Binaries/Linux-x86-64" \
           "${pkgdir}/opt/Mathematica/SystemFiles/Components/MXNetLink/LibraryResources/Linux-x86-64" \
           "${pkgdir}/opt/Mathematica/SystemFiles/Components/MachineLearning/Resources/Binaries/Linux-x86-64" \
           "${pkgdir}/opt/Mathematica/SystemFiles/Components/NumericArrayUtilities/LibraryResources/Linux-x86-64" \
           "${pkgdir}/opt/Mathematica/SystemFiles/Components/PredictiveInterface/Kernel/Predictions.mx/Linux-x86-64" \
           "${pkgdir}/opt/Mathematica/SystemFiles/Components/PredictiveInterface/Kernel/PredictiveInterfaceCode.mx/Linux-x86-64" \
           "${pkgdir}/opt/Mathematica/SystemFiles/Components/SemanticImport/Binaries/Linux-x86-64" \
           "${pkgdir}/opt/Mathematica/SystemFiles/Components/SpellCorrect/LibraryResources/Linux-x86-64" \
           "${pkgdir}/opt/Mathematica/SystemFiles/Components/TextSearch/Binaries/Linux-x86-64" \
           "${pkgdir}/opt/Mathematica/SystemFiles/Components/WSMCore/SystemModeler/Mathematica/WSMLink/SystemFiles/Libraries/Linux-x86-64" \
           "${pkgdir}/opt/Mathematica/SystemFiles/Components/WSMCore/SystemModeler/SystemFiles/Activation/Linux-x86-64" \
           "${pkgdir}/opt/Mathematica/SystemFiles/Components/WSMCore/SystemModeler/SystemFiles/Libraries/Linux-x86-64" \
           "${pkgdir}/opt/Mathematica/SystemFiles/Components/WSMCore/SystemModeler/SystemFiles/WSM/Binaries/Linux-x86-64" \
           "${pkgdir}/opt/Mathematica/SystemFiles/Components/WebUnit/Resources/DriverBinaries/ChromeDriver/Linux-x86-64" \
           "${pkgdir}/opt/Mathematica/SystemFiles/Components/WebUnit/Resources/DriverBinaries/GeckoDriver/Linux-x86-64" \
           "${pkgdir}/opt/Mathematica/SystemFiles/Converters/Binaries/Linux-x86-64" \
           "${pkgdir}/opt/Mathematica/SystemFiles/FrontEnd/Binaries/Linux-x86-64" \
           "${pkgdir}/opt/Mathematica/SystemFiles/Graphics/Binaries/Linux-x86-64" \
           "${pkgdir}/opt/Mathematica/SystemFiles/Java/Linux-x86-64" \
           "${pkgdir}/opt/Mathematica/SystemFiles/Kernel/Binaries/Linux-x86-64" \
           "${pkgdir}/opt/Mathematica/SystemFiles/Kernel/SystemResources/Linux-x86-64" \
           "${pkgdir}/opt/Mathematica/SystemFiles/Libraries/Linux-x86-64" \
           "${pkgdir}/opt/Mathematica/SystemFiles/Links/AudioFileStreamTools/LibraryResources/Linux-x86-64" \
           "${pkgdir}/opt/Mathematica/SystemFiles/Links/AudioTools/LibraryResources/Linux-x86-64" \
           "${pkgdir}/opt/Mathematica/SystemFiles/Links/CURLLink/LibraryResources/Linux-x86-64" \
           "${pkgdir}/opt/Mathematica/SystemFiles/Links/CalendarTools/LibraryResources/Linux-x86-64" \
           "${pkgdir}/opt/Mathematica/SystemFiles/Links/CloudObject/LibraryResources/Linux-x86-64" \
           "${pkgdir}/opt/Mathematica/SystemFiles/Links/DAALLink/LibraryResources/Linux-x86-64" \
           "${pkgdir}/opt/Mathematica/SystemFiles/Links/DTWTools/LibraryResources/Linux-x86-64" \
           "${pkgdir}/opt/Mathematica/SystemFiles/Links/FDLLink/LibraryResources/Linux-x86-64" \
           "${pkgdir}/opt/Mathematica/SystemFiles/Links/GIFTools/LibraryResources/Linux-x86-64" \
           "${pkgdir}/opt/Mathematica/SystemFiles/Links/GeometryTools/LibraryResources/Linux-x86-64" \
           "${pkgdir}/opt/Mathematica/SystemFiles/Links/HDF5Tools/LibraryResources/Linux-x86-64" \
           "${pkgdir}/opt/Mathematica/SystemFiles/Links/HTTPLink/LibraryResources/Linux-x86-64" \
           "${pkgdir}/opt/Mathematica/SystemFiles/Links/IMAQTools/LibraryResources/Linux-x86-64" \
           "${pkgdir}/opt/Mathematica/SystemFiles/Links/IPOPTLink/LibraryResources/Linux-x86-64" \
           "${pkgdir}/opt/Mathematica/SystemFiles/Links/JLink/Kernel/SystemResources/Linux-x86-64" \
           "${pkgdir}/opt/Mathematica/SystemFiles/Links/JLink/SystemFiles/Libraries/Linux-x86-64" \
           "${pkgdir}/opt/Mathematica/SystemFiles/Links/JSONTools/LibraryResources/Linux-x86-64" \
           "${pkgdir}/opt/Mathematica/SystemFiles/Links/LibraryLink/LibraryResources/Linux-x86-64" \
           "${pkgdir}/opt/Mathematica/SystemFiles/Links/LightGBMLink/LibraryResources/Linux-x86-64" \
           "${pkgdir}/opt/Mathematica/SystemFiles/Links/MIDITools/LibraryResources/Linux-x86-64" \
           "${pkgdir}/opt/Mathematica/SystemFiles/Links/MIMETools/LibraryResources/Linux-x86-64" \
           "${pkgdir}/opt/Mathematica/SystemFiles/Links/MP3Tools/LibraryResources/Linux-x86-64" \
           "${pkgdir}/opt/Mathematica/SystemFiles/Links/MQTTLink/LibraryResources/Linux-x86-64" \
           "${pkgdir}/opt/Mathematica/SystemFiles/Links/MQTTLink/Resources/Binaries/Linux-x86-64" \
           "${pkgdir}/opt/Mathematica/SystemFiles/Links/MathLink/DeveloperKit/Linux-x86-64" \
           "${pkgdir}/opt/Mathematica/SystemFiles/Links/MongoLink/LibraryResources/Linux-x86-64" \
           "${pkgdir}/opt/Mathematica/SystemFiles/Links/OGGTools/LibraryResources/Linux-x86-64" \
           "${pkgdir}/opt/Mathematica/SystemFiles/Links/OpenCLLink/LibraryResources/Linux-x86-64" \
           "${pkgdir}/opt/Mathematica/SystemFiles/Links/OpenCVLink/LibraryResources/Linux-x86-64" \
           "${pkgdir}/opt/Mathematica/SystemFiles/Links/OpenSURF/LibraryResources/Linux-x86-64" \
           "${pkgdir}/opt/Mathematica/SystemFiles/Links/ProcessLink/LibraryResources/Linux-x86-64" \
           "${pkgdir}/opt/Mathematica/SystemFiles/Links/RAWTools/LibraryResources/Linux-x86-64" \
           "${pkgdir}/opt/Mathematica/SystemFiles/Links/RLink/SystemFiles/Libraries/Linux-x86-64" \
           "${pkgdir}/opt/Mathematica/SystemFiles/Links/SVTools/LibraryResources/Linux-x86-64" \
           "${pkgdir}/opt/Mathematica/SystemFiles/Links/SecureShellLink/LibraryResources/Linux-x86-64" \
           "${pkgdir}/opt/Mathematica/SystemFiles/Links/SerialLink/LibraryResources/Linux-x86-64" \
           "${pkgdir}/opt/Mathematica/SystemFiles/Links/SocketLink/LibraryResources/Linux-x86-64" \
           "${pkgdir}/opt/Mathematica/SystemFiles/Links/SoundFileTools/LibraryResources/Linux-x86-64" \
           "${pkgdir}/opt/Mathematica/SystemFiles/Links/SpeechSynthesisTools/LibraryResources/Linux-x86-64" \
           "${pkgdir}/opt/Mathematica/SystemFiles/Links/SpeechVocoderTools/LibraryResources/Linux-x86-64" \
           "${pkgdir}/opt/Mathematica/SystemFiles/Links/StreamLink/LibraryResources/Linux-x86-64" \
           "${pkgdir}/opt/Mathematica/SystemFiles/Links/SystemTools/LibraryResources/Linux-x86-64" \
           "${pkgdir}/opt/Mathematica/SystemFiles/Links/TINSLink/LibraryResources/Linux-x86-64" \
           "${pkgdir}/opt/Mathematica/SystemFiles/Links/TesseractTools/LibraryResources/Linux-x86-64" \
           "${pkgdir}/opt/Mathematica/SystemFiles/Links/TetGenLink/LibraryResources/Linux-x86-64" \
           "${pkgdir}/opt/Mathematica/SystemFiles/Links/TinkerForgeWeatherStationTools/Binaries/Linux-x86-64" \
           "${pkgdir}/opt/Mathematica/SystemFiles/Links/TriangleLink/LibraryResources/Linux-x86-64" \
           "${pkgdir}/opt/Mathematica/SystemFiles/Links/UUID/LibraryResources/Linux-x86-64" \
           "${pkgdir}/opt/Mathematica/SystemFiles/Links/VernierLink/LibraryResources/Linux-x86-64" \
           "${pkgdir}/opt/Mathematica/SystemFiles/Links/WSTP/DeveloperKit/Linux-x86-64" \
           "${pkgdir}/opt/Mathematica/SystemFiles/Links/WebpTools/LibraryResources/Linux-x86-64" \
           "${pkgdir}/opt/Mathematica/SystemFiles/Links/XLTools/LibraryResources/Linux-x86-64" \
           "${pkgdir}/opt/Mathematica/SystemFiles/Links/XMPTools/LibraryResources/Linux-x86-64" \
           "${pkgdir}/opt/Mathematica/SystemFiles/Links/ZeroMQLink/LibraryResources/Linux-x86-64"
    fi

    msg2 "Removing clashing bundled libraries"
    ## The following script will determine whether a library is provided by
    ## another package:
    ##
    ## find /opt/Mathematica -type f -name "*.so*" \
    ##     | parallel 'bash -c "pkg=\"\$(pacman -Fsq {/})\" ; if [[ -n \"\$pkg\" ]] ; then echo \".{} found in \$pkg\" ; fi"'
    ##
    ## Note that replacing *all* libraries with the system versions is a bad
    ## idea.  At this stage, only duplicated libraries in
    ## `./opt/Mathematica/SystemFiles/Libraries/Linux-x86-64/` are removed
    ## (except for Qt libraries which Mathematica expects).
    cd "${pkgdir}"
    while read lib ; do
        rm $lib
    done < "${srcdir}/duplicate-libs.txt"

    ## The documentation takes up the majority of the disk space (4.7G+).  If you
    ## do not wish to have the documentation installed, uncomment the following
    ## lines.
    # msg2 "Removing documentation"
    # rm -rf "${pkgdir}/opt/Mathematica/Documentation"
}

# Local Variables:
# mode: sh
# End:
