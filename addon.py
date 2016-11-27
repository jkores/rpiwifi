import xbmcaddon
import xbmcgui
 
addon       = xbmcaddon.Addon()
addonname   = addon.getAddonInfo('testovací aadon')
 
line1 = "Zkouška spojení"
line2 = "....."
line3 = "xxxxxxxxxxxxxxxxxx"
 
xbmcgui.Dialog().ok(addonname, line1, line2, line3)
