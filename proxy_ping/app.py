# -*- coding: utf-8 -*-

# Copyright (C) 2021  Marcus Rickert
#
# See https://github.com/marcus67/proxy_ping
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

import os.path

from proxy_ping import constants
from proxy_ping import status_server
from proxy_ping import api_view_handler

from python_base_app import base_app
from python_base_app import configuration
from python_base_app import pinger

APP_NAME = 'ProxyPing'
DIR_NAME = 'proxy-ping'
PACKAGE_NAME = 'proxy_ping'

class AppConfigModel(base_app.BaseAppConfigModel):

    def __init__(self):
        super(AppConfigModel, self).__init__(APP_NAME)

        self.check_interval = base_app.DEFAULT_TASK_INTERVAL


def get_argument_parser(p_app_name):
    parser = base_app.get_argument_parser(p_app_name=p_app_name)
    return parser


class App(base_app.BaseApp):

    def __init__(self, p_pid_file, p_arguments, p_app_name):

        super(App, self).__init__(p_pid_file=p_pid_file, p_arguments=p_arguments, p_app_name=p_app_name,
                                  p_dir_name=constants.DIR_NAME, p_languages=constants.LANGUAGES)

        self._status_server = None
        self._pinger = None

    def prepare_configuration(self, p_configuration):

        status_server_section = status_server.StatusServerConfigModel()
        p_configuration.add_section(status_server_section)

        pinger_section = pinger.PingerConfigModel()
        p_configuration.add_section(pinger_section)

        self.app_config = AppConfigModel()
        p_configuration.add_section(self.app_config)

        return super(App, self).prepare_configuration(p_configuration=p_configuration)


    def prepare_services(self, p_full_startup=True):

        super().prepare_services(p_full_startup=p_full_startup)

        if not p_full_startup:
            return

        status_server_config = self._config[status_server.SECTION_NAME]

        if not status_server_config.is_active():
            msg = "Status server not fully configured -> exiting"
            raise configuration.ConfigurationException(msg)

        pinger_config = self._config[pinger.SECTION_NAME]
        self._pinger = pinger.Pinger(p_config=pinger_config)


        self._status_server = status_server.StatusServer(
            p_config=self._config[status_server.SECTION_NAME],
            p_package_name=PACKAGE_NAME,
            p_languages=constants.LANGUAGES,
            p_pinger=self._pinger
        )



    def run_special_commands(self, p_arguments):

        return False


    def start_services(self):

        if self._status_server is not None:
            self._status_server.start_server()

    def stop_services(self):

        fmt = "Shutting down services -- START"
        self._logger.info(fmt)

        if self._status_server is not None:
            self._status_server.stop_server()
            self._status_server = None

        fmt = "Shutting down services -- END"
        self._logger.info(fmt)


def main():
    parser = get_argument_parser(p_app_name=APP_NAME)

    return base_app.main(p_app_name=APP_NAME, p_app_class=App, p_argument_parser=parser)


if __name__ == '__main__':
    exit(main())
