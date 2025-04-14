from otupy.profiles.ctxd.data.application import Application
from otupy.profiles.ctxd.data.cloud import Cloud
from otupy.profiles.ctxd.data.container import Container
from otupy.profiles.ctxd.data.iot import IOT
from otupy.profiles.ctxd.data.network import Network
from otupy.profiles.ctxd.data.vm import VM
from otupy.profiles.ctxd.data.web_service import WebService
from otupy.types.base import Choice
from otupy.core.extensions import Register


class ServiceType(Choice):
    
    register = Register({'application': Application, 'vm': VM, 'container': Container, 'web_service': WebService,
                         'cloud': Cloud, 'network': Network, 'iot': IOT})
    #Il tipo Hostname è utilizzabile per reverse-dns

    def __init__(self, service_type):
        super().__init__(service_type)
