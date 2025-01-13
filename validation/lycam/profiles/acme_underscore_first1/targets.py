import openc2
import acme_underscore_first1.properties

@openc2.v10.CustomTarget("x-_acme:container", [("container", acme_underscore_first1.properties.AcmeProperty())])
class ContainerTarget(object):
    pass

@openc2.v10.CustomTarget("x-_acme:features", [("features", acme_underscore_first1.properties.AcmeProperty())])
class FeaturesTarget(object):
    pass

