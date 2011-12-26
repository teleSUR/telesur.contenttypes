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
                          default=u"Program's page URL in video system."),
            required=False,
        )

    email = schema.TextLine(
            title=_(u'Email'),
            description=_(u'help_email',
                          default=u"Program's host e-mail address."),
            required=False,
        )

    twitter = schema.TextLine(
            title=_(u'Twitter account'),
            description=_(u'help_twitter',
                          default=u"Program's Twitter account."),
            required=False,
        )
