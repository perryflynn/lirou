# systemd

## Dependencies

`After=`  
This option only sets the order of the units, it doesn't guarantee that the service has finished starting up.

`Wants=`  
This option allows your unit to start only after another unit has finished starting up. (Doesn't matter if it started successfully or not)

`Requires=`  
Just like `Wants=`, however, this will make your unit start only after the dependencies have successfully started.

Inversed:

`After=` is inversed by `Before=`  
`Wants=` is inversed by `WantedBy=`  
`Requires=` is inversed by `RequiredBy=`  

https://askubuntu.com/a/1024921/443450

## Dispatcher

https://manpages.debian.org/testing/networkd-dispatcher/networkd-dispatcher.8.en.html
