# -*- coding: utf-8 -*-

from Acquisition import aq_inner

from five import grok

from Products.CMFCore.utils import getToolByName

from telesur.contenttypes.program import IProgram
from telesur.contenttypes.edition import IEdition

grok.templatedir('templates')


class View(grok.View):
    """ Default view of Programs.
    """
    grok.context(IProgram)
    grok.require('zope2.View')

    def editions(self):
        """ Return a catalog search result of editions to show.
        """

        context = aq_inner(self.context)
        catalog = getToolByName(context, 'portal_catalog')

        return catalog(object_provides=IEdition.__identifier__,
                       path='/'.join(context.getPhysicalPath()),
                       sort_on='getObjPositionInParent')
