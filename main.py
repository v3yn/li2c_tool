import argparse

import device_com.devices


def _generate_argparser() -> argparse.ArgumentParser:
    arg_desc = '''\
    Configure and communicate with connected TXS modules.
    -----------------------------------------------------
    Stimulate test signals and set configuration data
    through the I2C serial data transfer protocol.
    '''
    parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter,
                                     prog="LI2C Tool", description=arg_desc,
                                     epilog="(WARNING: CURRENTLY IN NON-FUNCTIONAL STATE!)")

    parser.add_argument("-d", "--devices",
                        help="generates list of available connected I2C devices",
                        action="store_true")
    # TODO: open connection, read, write etc.

    return parser


if __name__ == '__main__':
    parser = _generate_argparser()
    args = parser.parse_args()

    parser.print_help()

    if args.devices:
        device_com.devices.list_devices()
