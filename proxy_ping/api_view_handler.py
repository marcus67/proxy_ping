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

import json
import flask

import proxy_ping
from some_flask_helpers import blueprint_adapter
from proxy_ping import constants
from python_base_app import log_handling

API_BLUEPRINT_NAME = "API"
API_BLUEPRINT_ADAPTER = blueprint_adapter.BlueprintAdapter()

class ApiViewHandler(object):

    def __init__(self, p_app, p_pinger):
        self._pinger = p_pinger
        self._logger = log_handling.get_logger(self.__class__.__name__)

        self._blueprint = flask.Blueprint(API_BLUEPRINT_NAME, proxy_ping.__name__)
        API_BLUEPRINT_ADAPTER.assign_view_handler_instance(p_blueprint=self._blueprint,
                                                           p_view_handler_instance=self)
        API_BLUEPRINT_ADAPTER.check_view_methods()
        p_app.register_blueprint(self._blueprint)

    @API_BLUEPRINT_ADAPTER.route_method(p_rule=constants.API_URL_PING, methods=["GET"])
    def ping(self):
        request = flask.request

        host = request.args.get(constants.API_URL_PARAM_HOST)

        if host is None:
            msg = "parameter '{param_name}' not specified"
            return flask.Response(msg.format(param_name=constants.API_URL_PARAM_HOST),
                                  status=constants.HTTP_STATUS_CODE_NOT_FOUND,
                                  mimetype='application/txt')

        delay = self._pinger.ping(p_host=host)

        if delay is None:
            return flask.Response("ERROR DURING PING",
                                  status=constants.HTTP_STATUS_CODE_NOT_FOUND,
                                  mimetype='application/txt')

        return flask.Response(str(delay),
                              mimetype='application/txt')

    def destroy(self):
        API_BLUEPRINT_ADAPTER.unassign_view_handler_instances()
