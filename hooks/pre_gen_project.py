LICENSE_CLASSIFIERS = {
    'MIT': 'MIT License',
    'BSD-2-Clause': 'BSD License',
    'BSD 3-Clause': 'BSD License',
    'Apache-2.0': 'Apache Software License',
    'GPL-3.0-or-later': 'GNU General Public License v3 or later (GPLv3+)',
    'LGPL-3.0-or-later': 'GNU Lesser General Public License v3 or later (LGPLv3+)',
    'ISC': 'ISC License (ISCL)',
    'Unlicense': 'The Unlicense (Unlicense)',
}

LICENSE_SPDX = {
    'MIT License': 'MIT',
    'BSD 2-Clause License': 'BSD-2-Clause',
    'BSD 3-Clause License': 'BSD-3-Clause',
    'Apache License Version 2.0': 'Apache-2.0',
    'GNU General Public License Version 3': 'GPL-3.0-or-later',
    'ISC License': 'ISC',
    'Unlicense': 'Unlicense',
}

license = '{{ cookiecutter.license }}'
_ = '{{ cookiecutter.update({"license_classifier": LICENSE_CLASSIFIERS.get(license, license)}) }}'
_ = '{{ cookiecutter.update({"license_spdx": LICENSE_SPDX.get(license, license)}) }}'
