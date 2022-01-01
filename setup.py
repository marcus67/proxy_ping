# -*- coding: utf-8 -*-

#    Copyright (C) 2019  Marcus Rickert
#
#    See https://github.com/marcus67/proxy_ping
#
#    This program is free software; you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation; either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License along
#    with this program; if not, write to the Free Software Foundation, Inc.,
#    51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

from os import path

from setuptools import setup

import proxy_ping.settings

this_directory = path.abspath(path.dirname(__file__))

with open(path.join(this_directory, 'requirements.txt')) as f:
    install_requires = f.read().splitlines()

setup_params = {
    # standard setup configuration

    "install_requires": install_requires,
    "packages": ['proxy_ping', 'proxy_ping.test'],
    "include_package_data": True,
    "scripts": [
        "run_proxy_ping.py",
        "run_proxy_ping_test_suite.py",
    ],
    "long_description": "Tool to ping hosts behind a proxy host.",
}

extended_setup_params = {
    # additional setup configuration used by CI stages

    "docker_registry_user": "marcusrickert",
    # Docker image contexts to be built. The second entry of the tuple denotes if the resulting image is to be uploaded
    "docker_contexts": [('proxy-ping', True)
                        ],

    # technical name used for e.g. directories, PIP-package, and users
    "create_user": True,
    "create_group": True,
    #"user_group_mappings": [("proxy-ping", "audio")],
    "deploy_systemd_service": True,
    # "deploy_tmpfile_conf": True,
    #"deploy_sudoers_file": True,
    #"deploy_apparmor_file": True,
    "contributing_setups": ["python_base_app", "some_flask_helpers"],
    "publish_debian_package": proxy_ping.settings.SOURCEFORGE_CHANNELS,
    "publish_docker_images": proxy_ping.settings.DOCKER_CHANNELS,
    "publish_latest_docker_image": proxy_ping.settings.RELEASE_BRANCH_NAME,
    "debian_extra_files": [
        ("etc/proxy-ping.template.config", "etc/proxy-ping/proxy-ping.template.config"),
    ],
    "debian_templates": [
        ("/etc/proxy-ping/proxy-ping.template.config", "/etc/proxy-ping/proxy-ping.config")
    ],
    #"build_pypi_package": True,
    #"publish_pypi_package": { 'release': ( 'https://upload.pypi.org/legacy/', 'PYPI_API_TOKEN' ),
    #                          'main': ( 'https://test.pypi.org/legacy/', 'TEST_PYPI_API_TOKEN') },
    #"generate_generic_install": True,
    "analyze": True,
    "analyze_extra_exclusions": "vagrant/**",
    "script_timeout": 30,
}

setup_params.update(proxy_ping.settings.settings)
extended_setup_params.update(proxy_ping.settings.extended_settings)
extended_setup_params.update(setup_params)

if __name__ == '__main__':
    setup(**setup_params)
