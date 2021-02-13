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

from proxy_ping import constants
from proxy_ping import api_view_handler
from python_base_app import base_web_server
from some_flask_helpers import blueprint_adapter



SECTION_NAME = "StatusServer"

TEMPLATE_REL_DIR = "templates"

FORM_ID_CSRF = 'csrf'

class StatusServerConfigModel(base_web_server.BaseWebServerConfigModel):

    def __init__(self):
        super().__init__(p_section_name=SECTION_NAME)
        self.port = constants.DEFAULT_PORT


class StatusServer(base_web_server.BaseWebServer):

    def __init__(self,
                 p_config,
                 p_package_name,
                 p_pinger,
                 p_languages=None):
        super(StatusServer, self).__init__(
            p_config=p_config,
            p_name="Web Server",
            p_package_name=p_package_name)

        self._languages = p_languages
        self._pinger = p_pinger

        if self._languages is None:
            self._languages = {'en': "English"}

        self._api_view_handler = api_view_handler.ApiViewHandler(p_app=self._app, p_pinger=self._pinger)

    def destroy(self):
        self._api_view_handler.destroy()
        super().destroy()
