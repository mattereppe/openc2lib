import openc2
import acme_underscore_first2.properties

@openc2.v10.CustomTarget("x-acme:_container", [("_container", acme_underscore_first2.properties.AcmeProperty())])
class ContainerTarget(object):
    pass

@openc2.v10.CustomTarget("x-acme:features", [("features", acme_underscore_first2.properties.AcmeProperty())])
class FeaturesTarget(object):
    pass

