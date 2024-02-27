# .bashrc

# Source global definitions
if [ -f /etc/bashrc ]; then
	. /etc/bashrc
fi

# User specific environment
if ! [[ "$PATH" =~ "$HOME/.local/bin:$HOME/bin:" ]]
then
    PATH="$HOME/.local/bin:$HOME/bin:$PATH"
fi
export PATH

# Uncomment the following line if you don't like systemctl's auto-paging feature:
# export SYSTEMD_PAGER=

# User specific aliases and functions
if [ -d ~/.bashrc.d ]; then
	for rc in ~/.bashrc.d/*; do
		if [ -f "$rc" ]; then
			. "$rc"
		fi
	done
fi

unset rc
alias vi="nvim"
alias p="poweroff"
alias u="sudo dnf up -y"
alias r="reboot"
alias e="exit"
alias n=" brave-browser-beta --new-window https://www.notion.so/Gaining-respect-2ecdc98c575a41a5a664d3b5e35a10ad"
alias jg="sh /home/vmishra/Desktop/public_html/run.sh"
alias master="sh /home/vmishra/.ssh/scripts/master.sh"
alias r1="sh /home/vmishra/.ssh/scripts/rpi1.sh"

alias rs="node "/home/vmishra/Desktop/snm/server.js""

