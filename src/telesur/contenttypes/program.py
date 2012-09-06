# -*- coding: utf-8 -*-

from zope import schema

from five import grok
from plone.directives import dexterity, form

from telesur.contenttypes import _


# TODO: validar campo
class IProgram(form.Schema):
    """A TV show.
    """

    program_widget = schema.TextLine(
        title=_(u'Widget'),
        description=_(u'help_widget',
                      default=u"URL of the widget that shows the most recent programs."),
        required=False,
        )


class Program(dexterity.Container):
    """
    """
