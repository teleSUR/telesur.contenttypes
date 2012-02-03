# -*- coding: utf-8 -*-

from zope import schema

from plone.directives import form
from plone.namedfile.field import NamedBlobImage

from telesur.contenttypes import _


# TODO: validar tamaño de la imagen
class IEdition(form.Schema):
    """An edition of a TV show.
    """

    image = NamedBlobImage(
        title=_(u'Image'),
        description=_(u'help_image',
                      default=u''),
        required=False,
        )
