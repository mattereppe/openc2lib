import openc2
import stix2
import json
import collections


@openc2.properties.CustomProperty(
    "x-acme",
    [
        ("container", stix2.properties.StringProperty()),
    ],
)
class CustomTargetProperty(object):
    pass

#@openc2.properties.CustomProperty(
#    "x-acme",
#    [
#        ("cazzo", openc2.properties.StringProperty()),
#    ],
#)
#class ContainerProperty(object):
#    pass

@openc2.v10.CustomTarget("x-acme:id", [("id", CustomTargetProperty())])
class CustomTarget(object):
    pass


@openc2.v10.CustomArgs("whatever-who-cares", [("custom_args", CustomTargetProperty())])
class CustomArgs(object):
    pass


@openc2.v10.CustomActuator(
    "x-acme-widget",
    [
        ("name", stix2.properties.StringProperty(required=True)),
        ("version", CustomTargetProperty()),
    ],
)
class AcmeWidgetActuator(object):
    pass


def main():
    print("=== Creating Command")
    tp = CustomTargetProperty(container="target")
    print("target property", tp)
    t = CustomTarget(id=tp)
    print("target", t)
    args = CustomArgs(custom_args=CustomTargetProperty(container="args"))
    print("args", args)
    act = AcmeWidgetActuator(
        name="hello", version=CustomTargetProperty(container="actuator")
    )
    print("actuator", act)
    cmd = openc2.v10.Command(action="query", target=t, args=args, actuator=act)

    d = json.loads(cmd.serialize())
    print("=== COMMAND START ===")
    print(d)
    print("=== COMMAND END ===")
    print()

    print("=== Parsing command back to command ===")
    cmd2 = openc2.v10.Command(**d)
    print("=== COMMAND START ===")
    print(cmd2)
    print("=== COMMAND END ===")

    assert cmd == cmd2


if __name__ == "__main__":
    main()
