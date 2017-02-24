__author__ = 'Michael'
import wx
import ggplot2_gui_wxfb

class gui_main(ggplot2_gui_wxfb.MainFrame):
    def __init__(self,parent):
        self.parent=parent
        ggplot2_gui_wxfb.MainFrame.__init__(self,parent)



class MyApp(wx.App):
    def OnInit(self):
        self.mainframe = image_manager(None)
        self.SetTopWindow(self.mainframe)
        self.mainframe.SetIcon(wx.Icon('resources/icnPhyloMain32.png'))
        self.mainframe.Show()

        return True

