# -*- coding: utf-8 -*-

from zope import schema

from plone.directives import form

from telesur.contenttypes import _


# TODO: validar campo
class IProgram(form.Schema):
    """A TV show.
    """

    widget = schema.TextLine(
        title=_(u'Widget'),
        description=_(u'help_widget',
                      default=u"URL of the widget that shows the most recent programs."),
        required=False,
        )
