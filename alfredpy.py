# -*- coding: utf8 -*-
#
# Workflow Feedback Documentation:
# http://www.alfredforum.com/topic/5-generating-feedback-in-workflows/
#

class Item(object):
    """Each item"""
    ITEM_TEMPLATE = """<item uid="%s" arg="%s" valid="%s" autocomplete="%s">
      <title>%s</title>
      <subtitle>%s</subtitle>
      %s
    </item>
    """
    ICON_TEMPLATE = "<icon>%s</icon>"
    
    # Attributes
    uid = None
    arg = None
    valid = None # Optional
    autocomplete = None # Optional
    # Elements
    title = None
    subtitle = None
    icon = None # Optional
    
    def __init__(self, uid="", arg="", valid=True, autocomplete="", \
        title="", subtitle="", icon=None):
        self.uid = uid
        self.arg = arg
        self.valid = valid
        self.autocomplete = autocomplete
        self.title = title
        self.subtitle = subtitle
        self.icon = icon
        
    def get_icon_string(self):
        icon = ""
        if isinstance(self.icon, basestring):
            icon = self.ICON_TEMPLATE % self.icon
        return icon
        
    def get_valid_string(self):
        valid = "no"
        if self.valid:
            valid = "yes"
        return valid
        
    def to_xml(self, encoding="utf-8"):
        """docstring for to_xml"""
        xml = self.ITEM_TEMPLATE % (self.uid, self.arg, self.get_valid_string(), \
            self.autocomplete, self.title, self.subtitle, self.get_icon_string())
        return xml.encode(encoding)

class Feedback(object):
    """Feedback generator for Alfred 2 Workflow"""
    FEEDBACK_TEMPLATE = """<?xml version="1.0"?>
    <items>%s</items>
    """
    
    items = list()
    icon = None
    
    def add_item(self, uid="", arg="", valid=True, autocomplete="", \
        title="", subtitle="", icon=self.icon):
        """docstring for add_item"""
        self.items.append( Item(uid, arg, valid, autocomplete, title, subtitle, icon) )
    
    def get_items(self):
        """docstring for get_items"""
        return self.items
    
    def set_icon(self, icon):
        self.icon = icon
        
    def get_icon(self):
        return self.icon
        
    def to_xml(self, encoding="utf-8"):
        xml = self.FEEDBACK_TEMPLATE % "".join([i.to_xml() for i in self.items])
        return xml.encode(encoding)
        