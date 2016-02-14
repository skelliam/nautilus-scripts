from time import time
import gtk
import logging

class EntryDialog(gtk.MessageDialog):
    def __init__(self, *args, **kwargs):
        '''
        Creates a new EntryDialog. Takes all the arguments of the usual
        MessageDialog constructor plus one optional named argument 
        "default_value" to specify the initial contents of the entry.
        '''
        if 'default_value' in kwargs:
            default_value = kwargs['default_value']
            del kwargs['default_value']
        else:
            default_value = ''
        super(EntryDialog, self).__init__(*args, **kwargs)
        entry = gtk.Entry()        
        entry.set_text(str(default_value))
        entry.connect("activate", 
                      lambda ent, dlg, resp: dlg.response(resp), 
                      self, gtk.RESPONSE_OK)
        self.vbox.pack_end(entry, True, True, 0)
        self.vbox.show_all()
        self.entry = entry
    def set_value(self, text):
        self.entry.set_text(text)
    def run(self):
        result = super(EntryDialog, self).run()
        if (result == gtk.RESPONSE_OK or (result == gtk.RESPONSE_YES)):
            text = self.entry.get_text()
        elif (result == gtk.RESPONSE_NO):
            text = gtk.RESPONSE_NO
        else:
            text = None
        return text

#cool logging class from
#http://www.electricmonk.nl/log/2011/08/14/redirect-stdout-and-stderr-to-a-logger-in-python/
class StreamToLogger(object):
   """
   Fake file-like stream object that redirects writes to a logger instance.
   """
   def __init__(self, logger, log_level=logging.INFO):
      self.logger = logger
      self.log_level = log_level
      self.linebuf = ''
 
   def write(self, buf):
      for line in buf.rstrip().splitlines():
         self.logger.log(self.log_level, line.rstrip())


# The following message functions were from 
# License: Creative Commons Attribution-Share Alike 3.0 License
# http://creativecommons.org/licenses/by-sa/3.0/legalcode

def warningMessage(message):
    dlg = gtk.MessageDialog(None, 0, gtk.MESSAGE_WARNING, gtk.BUTTONS_YES_NO,
                            message)
    dlg.show_all()
    rc = dlg.run()
    dlg.destroy()
    if (rc == gtk.RESPONSE_NO):
      return gtk.RESPONSE_NO
    if (rc == gtk.RESPONSE_DELETE_EVENT):
      return gtk.RESPONSE_NO
    if (rc == gtk.RESPONSE_CLOSE):
      return gtk.RESPONSE_NO
    if (rc == gtk.RESPONSE_CANCEL):
      return gtk.RESPONSE_NO
                                                                                
    return rc
                                                                                
def errorMessage( message):
    dlg = gtk.MessageDialog(None, 0, gtk.MESSAGE_ERROR, gtk.BUTTONS_OK,
                            message)
    dlg.show_all()
    rc = dlg.run()
    dlg.destroy()
    return rc
                                                                                
def infoMessage( message):
    dlg = gtk.MessageDialog(None, 0, gtk.MESSAGE_INFO, gtk.BUTTONS_YES_NO,
                            message)
    dlg.show_all()
    rc = dlg.run()
    dlg.destroy()
    return rc
                                                                                
def simpleInfoMessage( message):
    dlg = gtk.MessageDialog(None, 0, gtk.MESSAGE_INFO, gtk.BUTTONS_OK,
                            message)
    dlg.show_all()
    rc = dlg.run()
    dlg.destroy()
    return rc

def now():
   return int( time() )

#Simple alert script from:
#http://www.ibm.com/developerworks/linux/library/l-script-linux-desktop-2/index.html
def alert(msg):
    """Show a dialog with a simple message."""
    dialog = gtk.MessageDialog()
    dialog.set_markup(msg)
    dialog.run()

# This is a function I wrote.  :)
def getDialogMessage(message, defaultval):
    dlg = EntryDialog(None, 0, gtk.MESSAGE_QUESTION, gtk.BUTTONS_YES_NO,
                            message, default_value=defaultval)
    dlg.show_all()
    rc = dlg.run()
    dlg.destroy()
    return rc

