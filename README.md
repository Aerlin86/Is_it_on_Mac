# Is_it_on_Mac
Check if given game is available for MacOS.<br>
->ver.0.2.4<-<br>
-searching on Steam/GOG/Geforce Now/Epic/Uplay<br>
--------------------------------------<br>
<b><big>TBA:</b></big><br>
-scalable for different screen sizes.<br>
-links to game site on different sites.<br>
--------------------------------------<br>
<big><b>How does it work?</b></big><br>
Rather simply.<br>
1. Input from HTML form is stored as a variable, that represents game name that we are looking for,<br>
2. For each site it googles for term [site] + [game name]*<br>
3. Next comes site scraping and looking for certain element (mostly divs), that indicate MacOS version*<br>
<br>
*- does not apply to Geforce Now and UPlay, due to:<br>
Geforce Now - every game on GN is available on MacOS, so this app just search game title on <a href="https://www.nvidia.com/pl-pl/geforce/geforce-experience/games/">Now page</a>.<br>
UPlay - as far as I am aware, it does not have MacOS versions, so it's just hardcoded <b>NO</b> xD<br>

--------------------------------------<br>