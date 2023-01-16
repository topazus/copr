# $$ is the current shell process id (bash, zsh, sh, etc)
echo $$
# /proc/[pid]/stat is status information about the current shell process
cat /proc/$(echo $$)/stat

cat /proc/$(echo $$)/stat | cut -d \  -f 4
# cut -d ' ' -f 4 will get the first 4th text split by space
cat /proc/$(echo $$)/stat | cut -d " "  -f 4

ps -o 'ppid='
ps -o 'ppid=' -p $$
ps -o comm= -p $$

# path to executarble
ps -o 'cmd=' -p $(ps -o 'ppid=' -p $$)

# terminal name
ps -p $PPID -o comm=
basename "/"$(ps -o cmd -f -p $(cat /proc/$(echo $$)/stat | cut -d \  -f 4) | tail -1 | sed 's/ .*$//')
