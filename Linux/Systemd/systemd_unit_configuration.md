# Systemd service unit configuration
Systemd unit represents a system resource like device, socket, application etc. Unit files contain the configuration to operate on the unit. Every unit file consists of three sections. Unit and Install sections are applicable to all unit files. While the third section changes based on the unit. Supported sections are
* Service
* Socket
* Mount
* Automount
* Swap
* Path
* Timer
* Slice

## Unit configuration file
```Bash
[Unit]
Directive=value

[Service | Socket | Mount | Automount | Swap | Path | Timer | Slice]
Directive=value

[Install]
Directive=value
```

## Unit section directives(Covers commonly used directives)
* Description - unit file description that summarizes basic functionality of the unit file.
* Documentation - unit file documentation.
* After - Units mentioned in this section will be started before the current unit. For instance, start the current unit after network target is up.
* Before - Units mentioned in this section will be started after the current unit.
* Wants - represents a weak dependency. All units mentioned in this directive will be started along with the current unit. Current unit does not fail though the wanted units might have failed to start.
* Requires - represents a strict dependency. Current unit is marked failed when atleast one of the required units have failed to start.

## Install section directives
Optional section. Units that need to be enabled will have this section.
* WantedBy commonly used directive with value **multi-user.target**

## Service section directives
* Type
* BusName
* User
* Group
* ExecStart 
* ExecStartPre
* ExecStartPost
* ExecStop
* ExecStopPost
* ExecReload
* TimeoutStartSec
* TimeoutStopSec
* TimeoutSec
* Restart
* RestartSec
* GuessMainPID
* RemainAfterExit
* PIDFile

## References:
* [Systemd unit section man](https://www.freedesktop.org/software/systemd/man/systemd.unit.html)
* [Systemd service section man](https://www.freedesktop.org/software/systemd/man/systemd.service.html)
* [Systemd units and Unit files](https://www.digitalocean.com/community/tutorials/understanding-systemd-units-and-unit-files)