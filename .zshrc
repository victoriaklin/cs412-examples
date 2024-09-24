autoload -U colors && colors
export PS1="%F{214}%K{000}%m%F{015}%K{000}:%F{039}%K{000}%~%F{015}%K{000}\$ "


# to choose color, wrap text with %F{<color>} ... %f NOTE: can use hex codes for <color>
export PROMPT="%(?.%F{10}✓.%F{9}x)%f %F{200}%n%f %F{177}[%~]%f %F{87}$%f "


# LOML's
#export PROMPT="%(?.%F{10}✓.%F{9}x)%f %F{189}%n%f [%F{49}%~%f] %F{195}>%f "

export PATH="/usr/local/bin:$PATH"
