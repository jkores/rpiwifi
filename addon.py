import xbmcaddon
import xbmcgui
 
addon       = xbmcaddon.Addon()
addonname   = addon.getAddonInfo('testovac� aadon')
 
line1 = "Zkou�ka spojen�"
line2 = "....."
line3 = "xxxxxxxxxxxxxxxxxx"
 
xbmcgui.Dialog().ok(addonname, line1, line2, line3)
