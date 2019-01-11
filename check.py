import os
import importlib.util
import shlex
import subprocess
import types
from typing import List
import sys

import yaml
import pycman.config
import pyalpm


class DependencyChecker:
    check_pass = {}
    REPO_ROOT = ""
    build_prefix_pkgs = {}

    def __init__(self):
        lilaclib = sys.modules['lilaclib'] = types.ModuleType('lilaclib')

        lilac_apis = [
            'aur_pre_build', 'aur_post_build',
            'pypi_pre_build', 'pypi_post_build',
            'vcs_update',
        ]

        for func_name in lilac_apis:
            setattr(lilaclib, func_name, None)

    def run(self, pkg_item: any):
        pkg_name = ""
        pkg_base = ""
        err_dep = []
        is_split = False

        if isinstance(pkg_item, tuple):
            pkg_base, pkg_name = pkg_item
            is_split = True
        else:
            pkg_name = pkg_base = pkg_item

        # Retrive the meta info from PKGBUILD, lilac.py, lilac.yaml
        # Note that lilac.yaml will be overridden by lilac.py
        package_info = self._get_pkgbuild_info(
            pkg_base, pkg_name, split=is_split)
        depends = package_info.get("depends")
        cn_deps, build_prefix = self._parse_lilac(pkg_base)

        if cn_deps is None:
            return []

        # Search all packages, Init pyalpm handle  from pacman.conf
        conf_path = os.path.join(
            "/usr/share/devtools/", "pacman-" + build_prefix.rstrip("-x86_64") + ".conf")
        handle = pycman.config.init_with_config(conf_path)
        syncdbs = handle.get_syncdbs()   # type: pyalpm.DB
        allpkgs = []

        if self.build_prefix_pkgs.get(build_prefix) is not None:
            allpkgs = self.build_prefix_pkgs.get(build_prefix)
        else:
            for db in syncdbs:
                allpkgs.extend(db.search(""))
            self.build_prefix_pkgs[build_prefix] = allpkgs


        if self.check_pass.get(pkg_item):
            return []

        for dep in depends:
            if self._dep_satisfied_in_syncdb(dep, allpkgs):
                continue
            if self._dep_satisfied_in_cn_repo(dep, cn_deps):
                continue
            err_dep.append(dep)

        if len(err_dep) == 0:
            self.check_pass[pkg_item] = True
        return err_dep

    def _get_pkgbuild_info(self, pkg_base, pkg_name, split=False) -> dict:
        info = {}
        pkgbuild_dir = os.path.join(self.REPO_ROOT, pkg_base, "PKGBUILD")
        deps = []
        provides = []
        pkgname = []
        info = {}

        # These are args we need to parse

        PARSE_ARGS = ["depends", "makedepends",
                      "pkgname", "provides", "depends_x86_64"]
        for arg in PARSE_ARGS:
            info[arg] = []

        if not split:
            cmd = shlex.split(
                "/bin/bash -c '{}/printpkgenv.sh {} 2>/dev/null'".format(self.REPO_ROOT, pkgbuild_dir))
        else:
            cmd = shlex.split(
                "/bin/bash -c '{}/printpkgenv.sh {} {} 2>/dev/null'".format(self.REPO_ROOT, pkgbuild_dir, pkg_name))

        proc = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                                encoding="UTF-8", stderr=None)

        if proc.returncode != 0 and proc.returncode is not None:
            raise Exception("PKGBUILD Parse error {}".format(proc.returncode))

        for line in proc.stdout:
            (k, _, v) = str(line).partition("=")
            v = v.lstrip("(").rstrip(")\n")  # type: str
            items = v.split(" ")
            if k in PARSE_ARGS:
                info[k] = []
                for item in items:
                    if item != "":
                        info[k].append(item)

        proc.communicate()

        info["depends"].extend(info.get("makedepends"))
        info["depends"].extend(info.get("depends_x86_64"))

        return info

    def _parse_lilac(self, pkg_base) -> (list, str):
        """ Read yaml first, and then read the py file, note that py will override the yaml """
        cn_deps = []
        build_prefix = ""
        lilac_py_path = os.path.join(self.REPO_ROOT, pkg_base, "lilac.py")
        lilac_yaml_path = os.path.join(self.REPO_ROOT, pkg_base, "lilac.yaml")
        try:
            _file = open(lilac_py_path, "r")
            _file.close()
        except FileNotFoundError:
            return (None, None)

        yaml_cn_deps, yaml_build_prefix = self._parse_lilac_yaml(
            lilac_yaml_path)
        py_cn_deps, py_build_prefix = self._parse_lilac_py(lilac_py_path)

        cn_deps = py_cn_deps if py_cn_deps is not None else yaml_cn_deps
        build_prefix = py_build_prefix if py_build_prefix is not None else yaml_build_prefix

        # If the vairables are not in any file, we set to default value
        if cn_deps is None:
            cn_deps = []
        if build_prefix is None or build_prefix == "":
            build_prefix = "extra-x86_64"

        return (cn_deps, build_prefix)

    def _parse_lilac_yaml(self, path):
        cn_deps = build_prefix = None
        build_prefix = ""
        try:
            _file = open(path, "r")
            yaml_obj = yaml.load(_file)
            if "depends" in yaml_obj:
                cn_deps = []
                depends = yaml_obj.get("depends")
                for depend in depends:
                    if isinstance(depend, dict):        # 'is' is different from 'isinstance'
                        for k, v in depend.items():
                            # cn_deps would contain either string or tuple
                            cn_deps.append((k, v))
                    else:
                        cn_deps.append(depend)
            _file.close()

            if "build_prefix" in yaml_obj:
                build_prefix = yaml_obj.get("build_prefix")
        except FileNotFoundError:
            pass
        return cn_deps, build_prefix

    def _parse_lilac_py(self, path):
        cn_deps = build_prefix = None
        spec = importlib.util.spec_from_file_location(
            "dumb" + ".pkg", path)
        mod = importlib.util.module_from_spec(spec)
        try:
            spec.loader.exec_module(mod)
        except Exception as e:
            pass

        try:
            assert mod.depends
            cn_deps = mod.depends
        except Exception as e:
            pass

        try:
            assert mod.build_prefix
            build_prefix = mod.build_prefix
        except Exception as e:
            pass
        return cn_deps, build_prefix

    def _dep_satisfied_in_syncdb(self, dep, packages: List[pyalpm.Package]):
        pkgobj = pyalpm.find_satisfier(packages, dep)
        if pkgobj is None:
            return False
        return True

    def _dep_satisfied_in_cn_repo(self, dep, cn_deps):
        # If the package is explictly list in cn_dep, we return true
        ok = False
        dep_need_check = None
        dep_name, _ = self._parse_dep_str(dep)
        if dep_name in cn_deps:
            dep_need_check = dep_name
            ok = True

        # TODO: deal with CN repo version string

        # We need to figure out provided packages
        if not ok:
            for cn_item in cn_deps:
                if not isinstance(cn_item, tuple):
                    provides = self._get_pkgbuild_info(
                        cn_item, cn_item, split=False).get("provides")
                    if dep_name in provides:
                        ok = True
                        dep_need_check = dep_name
                        break
                else:
                    # It's a tuple, which means split package
                    base, name = cn_item
                    info = self._get_pkgbuild_info(base, name, split=True)
                    # The split package might provide dep
                    provides = info.get("provides")
                    # The split package might be dep
                    pkgnames = info.get("pkgname")
                    if dep_name in provides or dep_name in pkgnames:
                        ok = True
                        dep_need_check = (base, name)
                        break

        if not ok:
            return False
        err_deps = self.run(dep_need_check)
        if len(err_deps) > 0:
            return False
        self.check_pass[dep_need_check] = True
        return True

    def _parse_dep_str(self, depstr)-> (str, str):
        name_index = -1
        ver_index = -1

        for k, v in enumerate(depstr):
            v: str
            if name_index == -1 and (v.isalpha() or v.isnumeric() or v in "@._+-"):
                continue
            if name_index != -1 and v in "><=":
                continue
            else:
                if name_index == -1:
                    name_index = k
                elif ver_index == -1:
                    ver_index = k
                    break
        if name_index == -1:
            return depstr, ""

        pkgname = depstr[0:name_index]
        pkgver = depstr[ver_index:]
        return pkgname, pkgver
