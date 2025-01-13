import openc2
import acme_specialchar2.properties

@openc2.v10.CustomTarget("x-acme:contai$ner", [("contai$ner", acme_specialchar2.properties.AcmeProperty())])
class ContainerTarget(object):
    pass

@openc2.v10.CustomTarget("x-acme:features", [("features", acme_specialchar2.properties.AcmeProperty())])
class FeaturesTarget(object):
    pass

