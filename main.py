import wx

if __name__ == '__main__':
    app = wx.App()
    frame = wx.Frame(None, wx.ID_ANY, "Hello WxPython")
    frame.Show()
    app.MainLoop()
