# -*- coding: utf-8 -*-

from zope import schema

from plone.directives import form
from plone.namedfile.field import NamedBlobImage

from telesur.contenttypes import _


# TODO: validar campos
class IProgram(form.Schema):
    """A TV show.
    """

    image = NamedBlobImage(
        title=_(u'Image'),
        description=_(u'help_image',
                      default=u''),
        required=False,
        )

    url = schema.TextLine(
            title=_(u'URL'),
            description=_(u'help_url',
                          default=u"URL of the frontpage in the video "
                                   "system."),
            required=False,
        )

    host = schema.TextLine(
            title=_(u'Host'),
            description=_(u'help_host',
                          default=u"The name of the host."),
            required=False,
        )

    email = schema.TextLine(
            title=_(u'Email'),
            description=_(u'help_email',
                          default=u"Email address of the host."),
            required=False,
        )

    twitter = schema.TextLine(
            title=_(u'Twitter account'),
            description=_(u'help_twitter',
                          default=u"Twitter account associated with the "
                                   "program."),
            required=False,
        )

    widget = schema.TextLine(
            title=_(u'Widget'),
            description=_(u'help_widget',
                          default=u"URL of the widget that shows the most "
                                   "recent programs."),
            required=False,
        )
