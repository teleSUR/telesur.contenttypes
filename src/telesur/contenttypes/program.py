# -*- coding: utf-8 -*-

from five import grok
from zope import schema

from plone.directives import form
from plone.namedfile.field import NamedBlobImage

from telesur.contenttypes import _
from telesur.contenttypes.interfaces import ITelesurContentTypesLayer


class IProgram(form.Schema):
    """A program.
    """

    image = NamedBlobImage(
        title=_(u'Image'),
        description=_(u'help_image',
                      default=u''),
        required=False,
        )

    email = schema.TextLine(
            title=_(u'Email'),
            description=_(u'help_email',
                          default=u''),
            required=False,
        )

    twitter = schema.TextLine(
            title=_(u'Twitter'),
            description=_(u'help_twitter',
                          default=u''),
            required=False,
        )


class View(grok.View):
    """Default view.
    """
    grok.context(IProgram)
    grok.require('zope2.View')
    grok.layer(ITelesurContentTypesLayer)
