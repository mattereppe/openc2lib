import openc2
import acme_noprofile.properties

@openc2.v10.CustomTarget(":container", [("container", acme_noprofile.properties.AcmeProperty())])
class ContainerTarget(object):
    pass

@openc2.v10.CustomTarget("features", [("features", acme_noprofile.properties.AcmeProperty())])
class FeaturesTarget(object):
    pass

