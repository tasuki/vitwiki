# WeeChat

Basic basics...

## Setup

### Load [the theme](weechat/tasuki.theme)
```
/script load theme.py
/theme installfile /home/vita/.weechat/themes/themes/tasuki.theme
```

#### Active buffer less offensive background
```
/set buflist.format.buffer_current "${color:,white}${format_buffer}"
```

### Don't spam join/part/quit messages
```
/filter add joinquit * irc_join,irc_part,irc_quit *
```

## Join channels
```
/set irc.server.freenode.autojoin "#handshake,#haskell,#idris,#manjaro,#ubuntu,#vimwiki,#yesod"
```

## Leave channels
```
/part
/buffer close
```
