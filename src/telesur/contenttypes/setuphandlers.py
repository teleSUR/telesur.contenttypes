# -*- coding:utf-8 -*-
from five import grok

from Products.CMFPlone.interfaces import INonInstallable


class HiddenProfiles(grok.GlobalUtility):

    grok.implements(INonInstallable)
    grok.provides(INonInstallable)
    grok.name('telesur.contenttypes.program')

    def getNonInstallableProfiles(self):
        profiles = ['telesur.contenttypes.program:uninstall', ]
        return profiles
