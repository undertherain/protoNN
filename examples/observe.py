# this example shows different ways to track a parameter

import logging
import protonn.parameters

logging.basicConfig(level=logging.DEBUG)


@protonn.parameters.view
def do_something():
    parameter_1 = 42  # type: Observed
    print(parameter_1)


def main():
    do_something()
    protonn.parameters.dump()


if __name__ == "main":
    main()
