# Maintainer: Stephen Cox: stephencoxmail -at- gmail com
# Previous Maintainers: Ignat Harczuk: ignathe -at- gmail com and Mark Wells: mwellsa -at- gmail com
# Contributor: simone riva: siomone.rva -a- gmail com
# Intel Parallel Studio XE 2019 for Linux - ( Intel compiler icc suite )
##########################################################################
# this PKGBUILD splits the main Parallel Studio XE package in 9 sub-packages:
#
# intel-compiler-base:          Intel C/C++ compiler and base libs
# intel-fortran-compiler:       Intel Fortran compiler and base libs"
# intel-ipp:                    Intel Integrated Performance Primitives
# intel-mkl:                    Intel Math Kernel Library (Intel® MKL)
# intel-mpi:                    Intel Message passing interface (MPI)
# intel-tbb_psxe:               Intel Threading Building Blocks (TBB)
# intel-vtune:                  Intel Vtune Amplifier
# intel-advisor:                Intel Advisor
# intel-inspector:              Intel Inspector
###########################################################################

# Parallel Studio XE
# Copyright (C) 2016       Ignat Harczuk
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

pkgbase="intel-parallel-studio-xe"
pkgname=('intel-compiler-base' 'intel-fortran-compiler' 'intel-ipp' 'intel-mkl' 'intel-mpi' 'intel-tbb_psxe' 'intel-advisor' 'intel-vtune-amplifier' 'intel-inspector' )
PKGEXT='.pkg.tar.lzo'
packager="Ignat Harczuk"

########################################
#OPTIONS begin
# set to true if you want to remove documentations and examples form the packages.
#_remove_docs=TRUE
_remove_docs=true

# set to true if you want to remove the static objects from the libs.
#_remove_static_objects_mkl=true
_remove_static_objects_mkl=false

#_remove_static_objects_ipp=true
_remove_static_objects_ipp=false
########################################

_year='2019'
_v_a='1'
_v_b='144'
# year, version a and version b found in /opt/intel/compilers_and_libraries_YEAR_A_B

_update='1'

pkgrel=1


_sp='cluster_edition'
_icc_ver='19.0.1'
_mpi_ver='2019.1.144'
_mkl_ver='2019.1.144'
_tbb_ver='2019.1.144'
_vtune_ver='2019.1.0.579888'
_inspector_ver='2019.1.0.579146'
_advisor_ver='2019.1.0.579143'

_vtune_man_ver='2019.1.0.579888'
_inspector_man_ver='2019.1.0.5579146'
_advisor_man_ver='2019.1.0.579143'


pkgver=${_year}.${_v_a}.${_v_b}

_dir_nr='14850'
_mpi_dir_nr='14879'

options=(strip libtool staticlibs)

url="http://software.intel.com/en-us/articles/non-commercial-software-download/"
arch=('x86_64')
license=('custom')
makedepends=('libarchive' 'sed' 'gzip' 'lzop')

_parallel_studio_xe_dir="parallel_studio_xe${_year:+_${_year}}${_update:+_update${_update}}${_sp:+_${_sp}}"

source=(
  "http://registrationcenter-download.intel.com/akdlm/irc_nas/tec/${_dir_nr}/${_parallel_studio_xe_dir}.tgz"
  "http://registrationcenter-download.intel.com/akdlm/irc_nas/tec/${_mpi_dir_nr}/l_mpi_${_year}.${_v_a}.${_v_b}.tgz"
  'intel_compilers.sh'
  'intel_vtune-amplifier.sh'
  'intel_advisor.sh'
  'intel_inspector.sh'
  'intel-composer.install'
  'intel-compiler-base.conf'
  'intel-fortran.conf'
  'intel-openmp.conf'
  'intel-mkl.conf'
  'intel-mpi.conf'
  'intel-ipp.conf'
  'intel-tbb.conf'
  'intel-mkl.sh'
  'intel-mkl.install'
  'intel-mkl-th.conf'
  'intel-tbb.install'
  'EULA.txt'
)


sha256sums=('3a1eb39f15615f7a2688426b9835e5e841e0c030f21dcfc899fe23e09bd2c645'
            'dac86a5db6b86503313742b17535856a432955604f7103cb4549a9bfc256c3cd'
            '75fcdfc246949341afddcf51b2037f606f25612a04c199ac1a743247aa7c4ea5'
            '278f9545d14c1fbec737bbfbcafb1b9090d35aab0dfeddc99d4c6e296b56057b'
            'e3103fb1c5e2ec9f0cc4090abb7e273563e735d88e185f527c66b2aebd52e733'
            '3978b721722db7e3127828caf00e6e98539724daffd0a0bdaa287b27bc61b97a'
            '3f96dec03111e69d16bb363acf4d0570e8a9526c09e5e542a7558f1b26d043ef'
            '31ac4d0f30a93fe6393f48cb13761d7d1ce9719708c76a377193d96416bed884'
            '6151bc273b6f741a4ce93d8160b6f167c8ad499dbc6e8e3f6e08d48571d6a52a'
            '99cc9683cc75934cc21bb5a09f6ad83365ee48712719bfd914de9444695eed13'
            'a856326362e9b80c19dc237cbf66bf3d96a69bd7ad1baff99ec9849f8208348c'
            'ed02ea4a0ebc9c32b53155bc5e442c46257f8185ae17833be0b975558bbc951a'
            'da6f41c2e002c9a793c75a18c8d1c85ef7ef5bf83a7a0a158ff144481491aac8'
            '5d3ac1ba31d7fc5795821d95b17956b0c977c8f3576b02f664f8ebf476213a43'
            '5e68c529c65cac54218026c869e54b2ddb268179725fc1e6b56d920470dad999'
            '11398c0ae2e2011902b1d6356d916d41bb8b54d39d090c6c83630f4b0e84e93a'
            'e515cb28bf40cdb0db818db6a2688a0028575153a1b9d5acfb0bc5f13fe45722'
            'fde83eb0071a5bd2887de127b56cc573a254e30131ec7b2d956987512c3e90c2'
            '228ac25e147adb9b872e1a562e522d2fd48809ccae89b765112009896a6d55a5')

#_archive=l_ccompxe${_comp}_p_${pkgver}
if [ "$CARCH" = "i686" ]; then
  _i_arch='ia32'
  _i_arch2='i486'

  _not_arch='intel64'
  _not_arch2='x86_64'
else
  _i_arch='intel64'
  _i_arch2='x86_64'

  _not_arch='ia32'
  _not_arch2='i486'
fi


extract_rpms() {
  cd $2
  for rpm_file in ${rpm_dir}/$1 ; do
    echo -e "    Extracting: ${rpm_file}"
    bsdtar -xf ${rpm_file}
  done
}

extract_mpi_rpms() {
  cd $2
  for rpm_file in ${mpi_rpm_dir}/$1 ; do
    echo -e "    Extracting: ${rpm_file}"
    bsdtar -xf ${rpm_file}
  done
}

set_build_vars() {
  _pkg_ver=${pkgver}
  _composer_xe_dir="compilers_and_libraries_${_year}.${_v_a}.${_v_b}"
  rpm_dir=${srcdir}/${_parallel_studio_xe_dir}/rpm
  mpi_rpm_dir=${srcdir}/l_mpi_${_year}.${_v_a}.${_v_b}/rpm
  xe_build_dir=${srcdir}/cxe_build
  base_dir=${srcdir}/..
  _man_dir=${xe_build_dir}/usr/share/man/man1
}


build() {

  set_build_vars
  echo ${xe_build_dir}

  #  clean the builds dirs
  if [ -d ${srcdir}/opt ] ; then
    rm -rf ${srcdir}/opt
  fi

  if [ -d ${srcdir}/etc ] ; then
    rm -rf ${srcdir}/etc
  fi

  if [ -d ${srcdir}/usr ] ; then
    rm -rf ${srcdir}/usr
  fi

  if [ -d ${xe_build_dir} ] ; then
    rm -rf ${xe_build_dir}
  fi

  echo ${srcdir}

  mkdir -p ${xe_build_dir}

  # START !
  cd ${xe_build_dir}
  mkdir -p ${xe_build_dir}/etc/profile.d

  if [ "$CARCH" = "i686" ]; then
    sed 's/<arch>/ia32/' < ${srcdir}/intel_compilers.sh > ${xe_build_dir}/etc/profile.d/intel_compilers.sh
  else
    sed 's/<arch>/intel64/' < ${srcdir}/intel_compilers.sh > ${xe_build_dir}/etc/profile.d/intel_compilers.sh
  fi

  chmod a+x ${xe_build_dir}/etc/profile.d/intel_compilers.sh

  mkdir -p ${xe_build_dir}/etc/ld.so.conf.d

  _cnt=0
  for files in ${base_dir}/*.lic ; do
    _lic_file[_cnt]=${files}
    _cnt=$(($_cnt+1))
  done


  echo -e ""
  echo -e "-----------------------------------------------------------------------------------"
  mkdir -p ${xe_build_dir}/opt/intel/licenses
  if [ -f "${_lic_file[0]}" ]; then
    cp ${base_dir}/*.lic ${xe_build_dir}/opt/intel/licenses
    echo -e "\e[1mFound license files in ${base_dir}."
    echo -e "These will be installed into /opt/intel/licenses ...\e[0m"
  else
    echo -e "\e[1mNo license files found in ${base_dir}."
    echo -e "Remember to place license files in one of these locations:"
    echo -e "    /opt/intel/licenses"
    echo -e "    ~/Licenses"
    echo -e "Or the compiler will not work!\e[0m"
  fi
  echo -e "-----------------------------------------------------------------------------------"
  echo -e ""

  cp ${srcdir}/${_parallel_studio_xe_dir}/license.txt ${xe_build_dir}/opt/intel/license.txt

  echo -e ""
  echo -e "-----------------------------------------------------------------------------------"
  echo -e "\e[1mIMPORTANT - READ BEFORE COPYING, INSTALLING, OR USING.\e[0m"
  echo -e ""
  echo -e "Do not copy, install, or use the \"Materials\" provided under this license agreement (\"Agreement\"), until you"
  echo -e "have carefully read the following terms and conditions."
  echo -e ""
  echo -e "By copying, installing, or otherwise using the Materials, you agree to be bound by the terms of this"
  echo -e "Agreement. If you do not agree to the terms of this Agreement, do not copy, install, or use the Materials."
  echo -e " - A copy of the EULA has been copied in the PKGBUILD directory; plase read carefully the terms and "
  echo -e " - conditions of the Intel license before installing the packages. "
  echo -e "-----------------------------------------------------------------------------------"
  echo -e ""
  echo -e "-----------------------------------------------------------------------------------"
  echo -e " ATTENTION: This PKGBUILD may need up to 20 minutes if you use XZ as a compressor!"
  echo -e "    - The build of the packages: intel-mkl and intel-ipp is particularly slow - "
  echo -e "-----------------------------------------------------------------------------------"
  echo -e ""
  echo -e ""
  echo -e "-----------------------------------------------------------------------------------"
  echo -e " \e[1m\e[5mATTENTION: \e[0m \e[1m\e[31mThis PKGBUILD works with yaourt, "
  echo -e "but consumes a lot of RAM! \e[0m "
  echo -e " Using the makepkg command for building this package is recommended."
  echo -e "-----------------------------------------------------------------------------------"
  echo -e ""
  echo -e ""
  echo -e "-----------------------------------------------------------------------------------"
  echo -e "\e[1m #################### \e[0m"
  echo -e "\e[1m ##### Options: ##### \e[0m"
  if  ${_remove_docs} ; then
    echo -e " Remove Documentation: YES "
  else
    echo -e " Remove Documentation: NO "
  fi

  if  ${_remove_static_objects_mkl} ; then
    echo -e ""
    echo -e "\e[1m Remove Static Objects from MKL: YES \e[0m \e[1m\e[5m\e[31m ATTENTION !!!! \e[0m "
    echo -e "\e[1m If your software is based on the static objects edit the option at the line 50 of this PKGBUILD \e[0m "
  else
    echo -e " Remove Static Objects: NO "
  fi
  echo -e "-----------------------------------------------------------------------------------"
  echo -e ""
  if  ${_remove_static_objects_ipp} ; then
    echo -e ""
    echo -e "\e[1m Remove Static Objects from IPP: YES \e[0m \e[1m\e[5m\e[31m ATTENTION !!!! \e[0m "
    echo -e "\e[1m If your software is based on the static objects edit the option at the line 50 of this PKGBUILD \e[0m "
  else
    echo -e " Remove Static Objects: NO "
  fi
  echo -e "-----------------------------------------------------------------------------------"
  echo -e ""
  echo -e ""


  cd ${xe_build_dir}/opt/intel
  ln -s ./${_composer_xe_dir} composerxe

  ln -s ./composerxe/linux/bin/${_i_arch} bin
  ln -s ./composerxe/linux/pkg_bin pkg_bin

  ln -s ./composerxe/linux/ipp/ ipp
  ln -s ./composerxe/linux/compiler/lib/${_i_arch} lib
  # ln -s ./composerxe/linux/debugger/lib/${_i_arch} debugger_lib
  # ln -s ./composerxe/linux/man/ man
  ln -s ./composerxe/linux/mkl/ mkl
  ln -s ./composerxe/linux/tbb/ tbb

  _current_dir=`pwd`
  if [ -d ${pkgdir}/opt ] ; then
    cd ${pkgdir}
    rm -rf opt
    cd $_current_dir
  fi ;

  cd  ${srcdir}/${_parallel_studio_xe_dir}/rpm
  rm -v -f *.${_not_arch2}.rpm
  cd $_current_dir
}


package_intel-compiler-base() {

  set_build_vars

  pkgdesc="Intel C/C++ $_icc_ver"
  pkgver=${_pkg_ver}
  install=intel-composer.install

  echo -e " # intel_compiler-base: Start Building"

  mkdir -p ${xe_build_dir}/opt
  mkdir -p ${xe_build_dir}/etc/profile.d
  mkdir -p ${_man_dir}


  cp ${srcdir}/intel-compiler-base.conf ${xe_build_dir}/etc/ld.so.conf.d
  cd ${xe_build_dir}
  echo -e " # intel_compiler-base: Extracting RPMS"

  extract_rpms 'intel-icc*.rpm'  $xe_build_dir
  extract_rpms 'intel-comp*.rpm'  $xe_build_dir
  extract_rpms 'intel-openmp*.rpm'  $xe_build_dir
  extract_rpms 'intel-c-*.rpm'  $xe_build_dir


  echo -e " # intel_compiler-base: Editing variables"
  cd ${xe_build_dir}/opt/intel/${_composer_xe_dir}/linux/bin

  #rm uninstall.sh
  rm *.csh

  for f in *.sh ; do
    sed -i 's/<PRODDIR>/\/opt\/intel/g' $f
    sed -i 's/<INSTALLDIR>/\/opt\/intel\/composerxe\/linux/g' $f
  done

  cd $_i_arch
  sed -i 's/<INSTALLDIR>/\/opt\/intel\/composerxe\/linux/g' loopprofileviewer.sh
  chmod a+x loopprofileviewer.sh
  rm loopprofileviewer.csh

  if $_remove_docs ; then
    echo -e " # intel_compiler-base: Remove docs"
    rm -rf ${xe_build_dir}/opt/intel/${_composer_xe_dir}/linux/documentation
    rm -rf ${xe_build_dir}/opt/intel/${_composer_xe_dir}/linux/Documentation
    rm -rf ${xe_build_dir}/opt/intel/${_composer_xe_dir}/linux/Samples
  fi

  echo -e " # intel_compiler-base: Coping man pages"
  mv ${xe_build_dir}/opt/intel/documentation_${_year}/en/man/common/man1/*.1 ${_man_dir}

  cd ${_man_dir}
  for f in *.1 ; do
    gzip $f
  done

  cd ${xe_build_dir}

  echo -e " # intel_compiler-base: Move package"
  mv ${xe_build_dir}/opt ${pkgdir}
  mv ${xe_build_dir}/etc ${pkgdir}
  mv ${xe_build_dir}/usr ${pkgdir}
}

package_intel-fortran-compiler() {

  set_build_vars

  pkgdesc="Intel Fortran compiler $_icc_ver"
  pkgver=${_pkg_ver}
  depends=('intel-compiler-base')
  install=intel-composer.install

  echo -e " # intel-fortran-compiler: Start Building"

  mkdir -p ${xe_build_dir}/opt
  mkdir -p ${xe_build_dir}/etc/profile.d
  mkdir -p ${xe_build_dir}/etc/ld.so.conf.d
  mkdir -p ${_man_dir}

  if [ "$CARCH" = "i686" ]; then
    sed 's/<arch>/ia32/' < ${srcdir}/intel-fortran.conf > ${xe_build_dir}/etc/ld.so.conf.d/intel-fortran.conf
  else
    sed 's/<arch>/intel64/' < ${srcdir}/intel-fortran.conf > ${xe_build_dir}/etc/ld.so.conf.d/intel-fortran.conf
  fi

  cd ${xe_build_dir}

  echo -e " # intel-fortran-compiler: Extracting RPMS"

  extract_rpms 'intel-ifort*.rpm'  $xe_build_dir

  echo -e " # intel-fortran-compiler: Editing variables"
  cd ${xe_build_dir}/opt/intel/${_composer_xe_dir}/linux/bin

  rm *.csh

  #Remove duplicate logo and .css found in intel base
  rm ${xe_build_dir}/opt/intel/documentation_${_year}/en/compiler_f/ps${_year}/resources/intel_gsp_styles.css
  rm ${xe_build_dir}/opt/intel/documentation_${_year}/en/compiler_f/ps${_year}/resources/intel_logo.png

  if $_remove_docs ; then
    echo -e " # intel-fortran-compiler: Remove documentation"
    rm -rf ${xe_build_dir}/opt/intel/${_composer_xe_dir}/linux/documentation
    rm -rf ${xe_build_dir}/opt/intel/${_composer_xe_dir}/linux/Documentation
    rm -rf ${xe_build_dir}/opt/intel/${_composer_xe_dir}/linux/Samples
  fi

  echo -e " # intel-fortran-compiler: Coping man pages"
  mv ${xe_build_dir}/opt/intel/documentation_${_year}/en/man/common/man1/*.1 ${_man_dir}


  cd ${_man_dir}
  for f in *.1 ; do
    gzip $f
  done

  # Remove duplicate headers found in intel base
  rm ${xe_build_dir}/opt/intel/${_composer_xe_dir}/linux/compiler/include/omp_lib.f90
  rm ${xe_build_dir}/opt/intel/${_composer_xe_dir}/linux/compiler/include/intel64/omp_lib.mod
  rm ${xe_build_dir}/opt/intel/${_composer_xe_dir}/linux/compiler/include/intel64/omp_lib_kinds.mod
  cd ${xe_build_dir}

  echo -e " # intel-fortran-compiler: Move package"
  mv ${xe_build_dir}/opt ${pkgdir}
  mv ${xe_build_dir}/etc ${pkgdir}
  mv ${xe_build_dir}/usr ${pkgdir}
}

package_intel-ipp() {

  set_build_vars

  pkgdesc="Intel Integrated Performance Primitives $_ipp_ver"
  pkgver=${_pkg_ver}
  install=intel-composer.install

  echo -e " # intel-ipp: Start Building"

  mkdir -p ${xe_build_dir}/opt

  mkdir -p ${xe_build_dir}/etc/ld.so.conf.d

  if [ "$CARCH" = "i686" ]; then
    sed 's/<arch>/ia32/' < ${srcdir}/intel-ipp.conf > ${xe_build_dir}/etc/ld.so.conf.d/intel-ipp.conf
  else
    sed 's/<arch>/intel64/' < ${srcdir}/intel-ipp.conf > ${xe_build_dir}/etc/ld.so.conf.d/intel-ipp.conf
  fi

  cd ${xe_build_dir}
  echo -e " # intel-ipp: Extracting RPMS"

  extract_rpms 'intel-ipp-*.rpm'  $xe_build_dir

  echo -e " # intel-ipp: Editing variables"
  cd ${xe_build_dir}/opt/intel/${_composer_xe_dir}/linux/ipp/bin
  rm ippvars.csh
  sed -i 's/<INSTALLDIR>/\/opt\/intel\/composerxe\/linux/g' ippvars.sh

  if ${_remove_docs} ; then
    echo -e " # intel-ipp: Remove documentation"
    rm -rf ${xe_build_dir}/opt/intel/${_composer_xe_dir}/linux/Documentation
  fi

  if ${_remove_static_objects_ipp} ; then
    echo -e " # intel-ipp: Remove static objects"
    rm -f ${xe_build_dir}/opt/intel/${_composer_xe_dir}/linux/ipp/lib/${_i_arch}/libipp*.a
    rm -f ${xe_build_dir}/opt/intel/${_composer_xe_dir}/linux/ipp/lib/${_i_arch}/nonpic/libipp*.a
    rmdir ${xe_build_dir}/opt/intel/${_composer_xe_dir}/linux/ipp/lib/${_i_arch}/nonpic/
  fi

  echo -e " # intel-ipp: Move package"
  mv ${xe_build_dir}/opt ${pkgdir}
  mv ${xe_build_dir}/etc ${pkgdir}
}

package_intel-mkl() {

  set_build_vars

  pkgdesc="Intel Math Kernel Library (Intel® MKL) $_mkl_ver"
  pkgver=${_pkg_ver}
  install=intel-mkl.install
  backup=('etc/intel-mkl-th.conf')

  echo -e " # intel-mkl: Start Building"

  mkdir -p ${xe_build_dir}/opt
  mkdir -p ${xe_build_dir}/etc/ld.so.conf.d
  mkdir -p ${xe_build_dir}/etc/profile.d

  cp ${srcdir}/intel-mkl.sh ${xe_build_dir}/etc/profile.d/
  chmod a+x ${xe_build_dir}/etc/profile.d/intel-mkl.sh

  cp ${srcdir}/intel-mkl-th.conf ${xe_build_dir}/etc/

  if [ "$CARCH" = "i686" ]; then
    sed 's/<arch>/ia32/' < ${srcdir}/intel-mkl.conf > ${xe_build_dir}/etc/ld.so.conf.d/intel-mkl.conf
  else
    sed 's/<arch>/intel64/' < ${srcdir}/intel-mkl.conf > ${xe_build_dir}/etc/ld.so.conf.d/intel-mkl.conf
  fi

  cd ${xe_build_dir}

  echo -e " # intel-mkl: Extracting RPMS"
  extract_rpms 'intel-mkl-*.rpm'  $xe_build_dir

  echo -e " # intel-mkl: Editing variables"
  cd ${xe_build_dir}/opt/intel/${_composer_xe_dir}/linux/mkl/bin
  rm mklvars.csh
  sed -i 's/<INSTALLDIR>/\/opt\/intel\/composerxe\/linux/g' mklvars.sh

  rm -rf ./${_not_arch}

  if ${_remove_docs} ; then
    echo -e " # intel-mkl: remove documentation"
    rm -rf ${xe_build_dir}/opt/intel/${_composer_xe_dir}/linux/mkl/examples
    rm -rf ${xe_build_dir}/opt/intel/${_composer_xe_dir}/linux/mkl/benchmarks
  fi

  if ${_remove_static_objects_mkl} ; then
    echo -e " # intel-mkl: remove static objects"
    rm -f ${xe_build_dir}/opt/intel/${_composer_xe_dir}/linux/mkl/lib/${_i_arch}/libmkl_*.a
    rm -f ${xe_build_dir}/opt/intel/${_composer_xe_dir}/linux/mkl/lib/mic/libmkl_*.a
  fi

  echo -e " # intel-mkl: Move package"
  mv ${xe_build_dir}/opt ${pkgdir}
  mv ${xe_build_dir}/etc ${pkgdir}
}

package_intel-mpi() {

  set_build_vars

  pkgdesc="Intel MPI library $_mpi_ver"
  pkgver=${_pkg_ver}

  echo -e " # intel-mpi: Start Building "

  mkdir -p ${xe_build_dir}/opt
  mkdir -p ${xe_build_dir}/bin
  mkdir -p ${xe_build_dir}/etc/ld.so.conf.d

  if [ "$CARCH" = "i686" ]; then
    sed 's/<arch>/ia32/' < ${srcdir}/intel-mpi.conf > ${xe_build_dir}/etc/ld.so.conf.d/intel-mpi.conf
  else
    sed 's/<arch>/intel64/' < ${srcdir}/intel-mpi.conf > ${xe_build_dir}/etc/ld.so.conf.d/intel-mpi.conf
  fi

  cd ${xe_build_dir}

  echo -e " # intel-mpi: Extracting RPMS "
  extract_rpms 'intel-mpi-*.rpm'  $xe_build_dir
  extract_mpi_rpms 'intel-mpi-sdk-*.rpm'  $xe_build_dir

  echo -e " # intel-mpi: Editing variables "
  cd ${xe_build_dir}/opt/intel/${_composer_xe_dir}/linux/mpi/${_i_arch}/bin
  rm mpivars.csh

  #for i in mpd* mpi*    no mpd longer since 2017?
  for i in mpi*
  do
    sed -i 's/I_MPI_SUBSTITUTE_INSTALLDIR/\/opt\/intel\/composerxe\/linux\/mpi/g' $i
  done

  chmod a+x mpivars.sh

  rm -rf ${xe_build_dir}/opt/intel/${_composer_xe_dir}/linux/mpi_2019
  rm -rf ${xe_build_dir}/opt/intel/${_composer_xe_dir}/licensing/mpi_2019

  echo -e " # intel-mpi: Move package "
  mv ${xe_build_dir}/opt ${pkgdir}
  mv ${xe_build_dir}/etc ${pkgdir}
}

package_intel-tbb_psxe() {

  set_build_vars

  pkgdesc="Intel Threading Building Blocks (TBB) $_tbb_ver"
  pkgver=${_pkg_ver}
  install=intel-tbb.install

  echo -e " # intel-tbb: Start Building "

  mkdir -p ${xe_build_dir}/opt
  mkdir -p ${xe_build_dir}/etc/ld.so.conf.d

  if [ "$CARCH" = "i686" ]; then
    sed 's/<arch>/ia32/' < ${srcdir}/intel-tbb.conf > ${xe_build_dir}/etc/ld.so.conf.d/intel-tbb.conf
    sed -i 's/<INSTALLDIR>/\/opt\/intel\/composerxe/g' ${xe_build_dir}/etc/ld.so.conf.d/intel-tbb.conf
  else
    sed 's/<arch>/intel64/' < ${srcdir}/intel-tbb.conf > ${xe_build_dir}/etc/ld.so.conf.d/intel-tbb.conf
    sed -i 's/<INSTALLDIR>/\/opt\/intel\/composerxe/g' ${xe_build_dir}/etc/ld.so.conf.d/intel-tbb.conf
  fi

  cd ${xe_build_dir}

  echo -e " # intel-tbb: Extracting RPMS "
  extract_rpms 'intel-tbb-*.rpm'  $xe_build_dir


  echo -e " # intel-tbb: Editing variables "
  cd ${xe_build_dir}/opt/intel/${_composer_xe_dir}/linux/tbb/bin
  rm tbbvars.csh

  sed -i 's/SUBSTITUTE_INSTALL_DIR_HERE/\/opt\/intel\/composerxe\/linux\/tbb/g' tbbvars.sh

  chmod a+x tbbvars.sh

  echo -e " # intel-tbb: Remove unneeded libs and bin "
  rm -rf ${xe_build_dir}/opt/intel/${_composer_xe_dir}/linux/tbb/bin/${_not_arch}
  rm -rf ${xe_build_dir}/opt/intel/${_composer_xe_dir}/linux/tbb/lib/${_not_arch}

  if $_remove_docs ; then
    echo -e " # intel-tbb: remove documentation "
    rm -rf ${xe_build_dir}/opt/intel/${_composer_xe_dir}/linux/Documentation
    rm -rf ${xe_build_dir}/opt/intel/${_composer_xe_dir}/linux/tbb/examples
  fi

  echo -e " # intel-tbb: Move package "
  mv ${xe_build_dir}/opt ${pkgdir}
  mv ${xe_build_dir}/etc ${pkgdir}
}

package_intel-vtune-amplifier() {

  set_build_vars

  pkgdesc="Performance profiler for serial and parallel performance analysis $_vtune_ver"
  pkgver=${_pkg_ver}
  depends=('pangox-compat')

  echo -e " # intel-vtune-amplifier: Start building"
  mkdir -p ${xe_build_dir}/opt
  mkdir -p ${xe_build_dir}/etc/ld.so.conf.d
  mkdir -p ${xe_build_dir}/etc/profile.d
  mkdir -p ${_man_dir}

  echo -e " # intel-vtune-amplifier: Editing variables "
  if [ "$CARCH" = "i686" ]; then
    sed -i 's/<arch>/bin32/g' ${srcdir}/intel_vtune-amplifier.sh
  else
    sed -i 's/<arch>/bin64/g' ${srcdir}/intel_vtune-amplifier.sh
  fi
  cp ${srcdir}/intel_vtune-amplifier.sh ${xe_build_dir}/etc/profile.d/
  chmod a+x ${xe_build_dir}/etc/profile.d/intel_vtune-amplifier.sh

  cd ${xe_build_dir}
  echo -e " # intel-vtune-amplifier: Extracting RPMS "
  extract_rpms 'intel-vtune-amplifier-*.rpm'  $xe_build_dir

  echo -e " # intel-vtune-amplifier: Coping man pages"
  if [[ -d ${xe_build_dir}/opt/intel/vtune_amplifier_xe_${_year}.${_vtune_man_ver}/man/man1 ]]
  then
    mv ${xe_build_dir}/opt/intel/vtune_amplifier_xe_${_year}.${_vtune_man_ver}/man/man1/*.1 ${_man_dir}
    cd ${_man_dir}
    for f in *.1 ; do
      gzip $f
    done
  fi


  if $_remove_docs ; then
    echo -e " # intel-vtune-amplifier: remove documentation "
    rm -rf ${xe_build_dir}/opt/intel/vtune_amplifier_xe_${_year}.${_vtune_ver}/samples
    rm -rf ${xe_build_dir}/opt/intel/vtune_amplifier_xe_${_year}.${_vtune_ver}/documentation
  fi

  echo -e " # intel-vtune-amplifier: Move package"
  mv ${xe_build_dir}/opt ${pkgdir}
  mv ${xe_build_dir}/etc ${pkgdir}
  mv ${xe_build_dir}/usr ${pkgdir}
}

package_intel-advisor() {

  set_build_vars

  pkgdesc="Threading design and prototyping tool for software architects $_advisor_ver"
  pkgver=${_pkg_ver}
  conflicts=( 'intel-advisor-xe' )

  echo -e " # intel-advisor: Start building"
  mkdir -p ${xe_build_dir}/opt
  mkdir -p ${xe_build_dir}/etc/ld.so.conf.d
  mkdir -p ${xe_build_dir}/etc/profile.d
  mkdir -p ${_man_dir}

  echo -e " # intel-advisor: Editing variables "
  if [ "$CARCH" = "i686" ]; then
    sed -i 's/<arch>/bin32/g' ${srcdir}/intel_advisor.sh
  else
    sed -i 's/<arch>/bin64/g' ${srcdir}/intel_advisor.sh
  fi
  cp ${srcdir}/intel_advisor.sh ${xe_build_dir}/etc/profile.d/
  chmod a+x ${xe_build_dir}/etc/profile.d/intel_advisor.sh

  cd ${xe_build_dir}
  echo -e " # intel-advisor: Extracting RPMS "
  extract_rpms 'intel-advisor-*.rpm'  $xe_build_dir

  echo -e " # intel-advisor: Coping man pages"

  if [[ -d ${xe_build_dir}/opt/intel/advisor_${_year}.${_advisor_man_ver}/man/man1 ]]
  then
    mv ${xe_build_dir}/opt/intel/advisor_${_year}.${_advisor_man_ver}/man/man1/*.1 ${_man_dir}
    cd ${_man_dir}
    for f in *.1 ; do
      gzip $f
    done
  fi


  if $_remove_docs ; then
    echo -e " # intel-vtune-amplifier: remove documentation "
    rm -rf ${xe_build_dir}/opt/intel/advisor_${_year}.${_advisor_ver}/samples
    rm -rf ${xe_build_dir}/opt/intel/advisor_${_year}.${_advisor_ver}/documentation
  fi

  echo -e " # intel-advisor: Move package"
  mv ${xe_build_dir}/opt ${pkgdir}
  mv ${xe_build_dir}/etc ${pkgdir}
  mv ${xe_build_dir}/usr ${pkgdir}
}

package_intel-inspector() {
  set_build_vars
  pkgdesc="Memory and thread debugger $_inspector_ver"
  pkgver=${_pkg_ver}
  conflicts=('intel-inspector-xe')

  echo -e " # intel-inspector: Start building"
  mkdir -p ${xe_build_dir}/opt
  mkdir -p ${xe_build_dir}/etc/ld.so.conf.d
  mkdir -p ${xe_build_dir}/etc/profile.d
  mkdir -p ${_man_dir}

  echo -e " # intel-inspector: Editing variables "
  if [ "$CARCH" = "i686" ]; then
    sed -i 's/<arch>/bin32/g' ${srcdir}/intel_inspector.sh
  else
    sed -i 's/<arch>/bin64/g' ${srcdir}/intel_inspector.sh
  fi
  cp ${srcdir}/intel_inspector.sh ${xe_build_dir}/etc/profile.d/
  chmod a+x ${xe_build_dir}/etc/profile.d/intel_inspector.sh

  cd ${xe_build_dir}
  echo -e " # intel-inspector: Extracting RPMS "
  extract_rpms 'intel-inspector-*.rpm'  $xe_build_dir

  echo -e " # intel-inspector: Coping man pages"
  if [[ -d ${xe_build_dir}/opt/intel/inspector_${_year}.${_inspector_man_ver}/man/man1 ]]
  then
    mv ${xe_build_dir}/opt/intel/inspector_${_year}.${_inspector_man_ver}/man/man1/*.1 ${_man_dir}
    cd ${_man_dir}
    for f in *.1 ; do
      gzip $f
    done
  fi


  if $_remove_docs ; then
    echo -e " # intel-vtune-amplifier: remove documentation "
    rm -rf ${xe_build_dir}/opt/intel/inspector_${_year}.${_inspector_ver}/samples
    rm -rf ${xe_build_dir}/opt/intel/inspector_${_year}.${_inspector_ver}/documentation
  fi

  echo -e " # intel-inspector: Move package"
  mv ${xe_build_dir}/opt ${pkgdir}
  mv ${xe_build_dir}/etc ${pkgdir}
  mv ${xe_build_dir}/usr ${pkgdir}
}
pkgdesc="Intel C++ C and FORTRAN compiler - Intel Parallel Studio XE - Cluster Edition - icc icpc ifort ipp mkl"
depends=('bash' 'gcc')

