# -*- coding: utf-8 -*-

import unittest2 as unittest

from zope.interface import directlyProvides

from plone.app.customerize import registration

from plone.app.testing import TEST_USER_ID
from plone.app.testing import setRoles

from telesur.contenttypes.interfaces import ITelesurContentTypesLayer
from telesur.contenttypes.testing import INTEGRATION_TESTING


class BrowserLayerTest(unittest.TestCase):

    layer = INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.request = self.layer['request']
        directlyProvides(self.request, ITelesurContentTypesLayer)

        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.portal.invokeFactory('Folder', 'test-folder')
        setRoles(self.portal, TEST_USER_ID, ['Member'])
        self.folder = self.portal['test-folder']

        self.folder.invokeFactory('telesur.contenttypes.program', 'p1')
        self.p1 = self.folder['p1']

    def test_views_registered(self):
        views = ['view']
        registered = [v.name for v in registration.getViews(ITelesurContentTypesLayer)]
        # empty set only if all 'views' are 'registered'
        self.assertEquals(set(views) - set(registered), set([]))

    def test_default_view(self):
        pt = getattr(self.portal, 'portal_types')
        self.assertEquals(pt['telesur.contenttypes.program'].default_view, 'view')

    def test_view(self):
        name = '@@view'
        try:
            self.p1.unrestrictedTraverse(name)
        except AttributeError:
            self.fail('%s has no view %s' % (self.p1, name))


def test_suite():
    return unittest.defaultTestLoader.loadTestsFromName(__name__)
