from openc2lib.profiles.ctxd.data.application import Application
from openc2lib.profiles.ctxd.data.cloud import Cloud
from openc2lib.profiles.ctxd.data.container import Container
from openc2lib.profiles.ctxd.data.iot import IOT
from openc2lib.profiles.ctxd.data.network import Network
from openc2lib.profiles.ctxd.data.vm import VM
from openc2lib.profiles.ctxd.data.web_service import WebService
from openc2lib.types.base import Choice
from openc2lib.core.extensions import Register


class ServiceType(Choice):
    
    register = Register({'application': Application, 'vm': VM, 'container': Container, 'web_service': WebService,
                         'cloud': Cloud, 'network': Network, 'iot': IOT})
    #Il tipo Hostname è utilizzabile per reverse-dns

    def __init__(self, service_type):
        super().__init__(service_type)
