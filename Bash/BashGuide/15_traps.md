# Traps

## Signals

signals - sent from one process to another

| Signal | Name    | Effect         | Trappable |
| ------ | ------- | -------------- | --------- |
| 0      | EXIT    | process exited | yes       |
| 1      | SIGHUP  | Hangup         | yes       |
| 2      | SIGINT  | Interrupt      | yes       |
| 3      | SIGQUIT | Quit           | yes       |
| 9      | SIGKILL | Kill           | no        |
| 15     | SIGTERM | Terminate      | yes       |
| 18     | SIGCONT | Continue       | yes       |
| 19     | SIGSTOP | Stop           | no        |
| 20     | SIGTSTP | Terminal Stop  | yes       |

* all signals can be listed using `kill -l` or `trap -l`

`kill -SIGNUM PID` kills the process with PID by sending the signal SIGNUM.

While killing a process, start with graceful signal which is trappable like **SIGINT**, followed by **SIGTERM** and finally **SIGKILL**. Gracefull kill helps cleanup resources, child processes of the process to be killed.

## Process management

Useful commands to find details of a process

* jobs
* pgrep
* ps
* pidof

commands to kill the process

* kill - can use only PID to kill
* pkill - can determine PID based on process name, owner etc
* killall - can determine PID based on process name, owner etc

## Traps (Signal handlers)

Provides a way to catch signals and handle them. Bash provides  **trap** builtin. If no trap specified in the script, default action corresponding to that signal will be performed. SIGINT with no trap will kill the process.

```Bash
# Syntax
trap COMMAND SIGNAL

# example
# no command execution trap
# statements executing following this trap statement will have the "command" executed on receiving the signal for which trap is configured.
trap '' HUP INT QUIT TERM
# or
trap '' 1 2 3 15

# attempt to trap signal 9(KILL) and 19(STOP) will have no effect as these signals are untrappable.

# Reset the trap to return to its default behaviour
trap - HUP INT QUIT TERM
# or
trap - 1 2 3 15

```

**Signals are handled once the current foreground process terminates.**

```Bash
echo "PID is: $$"
trap 'echo "Cleaning up" && exit 1' INT
sleep 60  # sleep for 60 seconds
```

If the script has entered sleep command, sending **SIGINT** will be handled only after the sleep command execution is completed.

Trap handling is local to the script and **not system wide**.

Traps are designed for cleaning up of tasks executing in the background.

```Bash
echo "PID is: $$"
bg_pid=

function cleanup() {
  if [[ -n $bg_pid ]]
  then
    echo "Cleaning up"
    kill $bg_pid

    # It is a good practice to kill the script with the same signal.
    # reset the behaviour once cleanup is done.
    trap - INT
    # kills the script with the signal received
    # so that the exit code will reflect the same
    # this is considered as a good practice.
    kill -INT $$
  fi

}

trap cleanup INT
sleep 600 &  # sleep for 600 seconds
bg_pid="$!"
echo "Sleep PID is: $bg_pid"
wait
```

## Trap on Exit signal

Very useful one

```Bash
cleanup() {

}

# this trap ensures on script abnormal exit
# cleanup will be invoked.
# For a successful exit after all the actions are completed, trap handler for exit is reset to default.
trap cleanup EXIT
# actions
trap - EXIT
```

---

## References

* [Bash Guide by Joseph Deveau](https://www.amazon.in/BASH-Guide-Joseph-DeVeau-ebook/dp/B01F8AZ1LE/ref=sr_1_4?keywords=bash&qid=1564983319&s=digital-text&sr=1-4)
* [Bash exit traps](http://redsymbol.net/articles/bash-exit-traps/)
