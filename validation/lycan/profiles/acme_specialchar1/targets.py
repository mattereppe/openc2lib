import openc2
import acme_specialchar1.properties

@openc2.v10.CustomTarget("x-acm&e:container", [("container", acme_specialchar1.properties.AcmeProperty())])
class ContainerTarget(object):
    pass

@openc2.v10.CustomTarget("x-acm&e:features", [("features", acme_specialchar1.properties.AcmeProperty())])
class FeaturesTarget(object):
    pass

