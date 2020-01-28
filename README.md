# ev3devrpyc

The ev3devrpyc package allows you to remotely steer a real EV3 from your PC.

You only need to import the 'ev3devrpyc' module at the beginning of your python program 
before the ev3dev2 api is loaded. 

Then the 'ev3devrpyc' module loads a special importer which instead of loading the ev3dev 
modules from the simulator it proxies the ev3dev modules on a remote EV3. 
So when doing API calls to this proxied module all these calls are forwarded to the EV3.

For an example see: https://github.com/ev3dev-python-tools/thonny-ev3dev/wiki/Example

Note: normally the 'ev3dev2' package on a PC controls a simulated EV3 in the ev3dev2simulator, but by importing 
the 'ev3devrpyc' module a special importer is installed which doesn't load the 'ev3dev2' package anymore. Instead it loads a proxy module to the ev3dev module on the EV3 itself.
