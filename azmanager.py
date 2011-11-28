# vim: tabstop=4 shiftwidth=4 softtabstop=4

# Copyright 2011 OpenStack, LLC.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

"""Extra Manager to limit networks by availability zone."""

from nova import flags
from nova.network import manager


FLAGS = flags.FLAGS


class AZDHCPManager(manager.FlatDHCPManager):
    """Extends FlatDHCPManager to limit networks to availability zone."""

    def _get_networks_for_instance(self, context, instance_id, project_id,
                                   requested_networks=None):
        supercls = super(manager.FlatDHCPManager, self)
        networks = supercls._get_networks_for_instance(context,
                                                       instance_id,
                                                       project_id,
                                                       requested_networks)
        # NOTE(vish): expects label to be set to the name of the availability
        #             zone.  This is easier than adding a new field to the
        #             database.
        return [network for network in networks if
                network['label'] == FLAGS.node_availability_zone]