import openc2
import acme.properties

@openc2.v10.CustomTarget("x-acme:container", [("container", acme.properties.AcmeProperty())])
class ContainerTarget(object):
    pass

@openc2.v10.CustomTarget("x-acme:features", [("features", acme.properties.AcmeProperty())])
class FeaturesTarget(object):
    pass

