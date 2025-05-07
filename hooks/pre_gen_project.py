import cookiecutter

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

license = cookiecutter.license
cookiecutter.license_classifier = LICENSE_CLASSIFIERS.get(license, license)
