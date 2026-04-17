#!/usr/bin/python

import vdf
import re

d = vdf.load(open("compatibilitytool.vdf"))

t = d["compatibilitytools"]["compat_tools"]
RE = re.compile(r"^GE-Proton.*$")
d["compatibilitytools"]["compat_tools"] = { RE.sub("Proton-GE", k): v for k, v in d["compatibilitytools"]["compat_tools"].items() }
d["compatibilitytools"]["compat_tools"]["Proton-GE"]["display_name"] = re.sub(r"^GE-Proton(\d+)-(\d+)$", r"Proton GE \1.\2", d["compatibilitytools"]["compat_tools"]["Proton-GE"]["display_name"])

vdf.dump(d, open("compatibilitytool.vdf",'w'), pretty=True)
