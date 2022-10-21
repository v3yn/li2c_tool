LI2C Tool
=========
Communicate with TXS module connected through FTDI USB to I2C/UART adapter.

"Master" and "Slave" will be referred to as "Controller" and "Target" in this program, as per I2C version 7.

It makes more sense that way.


Developer Notes
---------------
### Notable Errors
- ValueError might be returned when trying to open connection/list devices 
    if access to USB device is not allowed
- In this case, run Python as `sudo`

### Dependencies & Requirements
- Stick to as few dependencies as possible. 
- Argparse for CLI, PyFtdi for communicating with interface
- Won't run on Windows due to FTDI drivers
    - In the future, maybe use Facade (or whatever else is appropriate) 
        design pattern for OS compatibility?

### Environment setup
- When using WSL, USB devices need to be attached using usbipd
  - usbipd wsl attach -a -b 1-2
  - usbipd wsl list