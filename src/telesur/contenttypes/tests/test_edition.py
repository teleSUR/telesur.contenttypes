# -*- coding: utf-8 -*-

import unittest2 as unittest

from zope.component import createObject
from zope.component import queryUtility

from plone.app.testing import TEST_USER_ID
from plone.app.testing import setRoles

from plone.dexterity.interfaces import IDexterityFTI

from telesur.contenttypes.edition import IEdition
from telesur.contenttypes.testing import INTEGRATION_TESTING


class IntegrationTest(unittest.TestCase):

    layer = INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.portal.invokeFactory('telesur.contenttypes.program', 'p1')
        self.p1 = self.portal['p1']

    def test_adding(self):
        self.p1.invokeFactory('telesur.contenttypes.edition', 'e1')
        e1 = self.p1['e1']
        self.failUnless(IEdition.providedBy(e1))

    def test_fti(self):
        fti = queryUtility(IDexterityFTI, name='telesur.contenttypes.edition')
        self.assertNotEquals(None, fti)

    def test_schema(self):
        fti = queryUtility(IDexterityFTI, name='telesur.contenttypes.edition')
        schema = fti.lookupSchema()
        self.assertEquals(IEdition, schema)

    def test_factory(self):
        fti = queryUtility(IDexterityFTI, name='telesur.contenttypes.edition')
        factory = fti.factory
        new_object = createObject(factory)
        self.failUnless(IEdition.providedBy(new_object))

    def test_default_workflow(self):
        workflow_tool = getattr(self.portal, 'portal_workflow')
        self.p1.invokeFactory('telesur.contenttypes.edition', 'e1')
        e1 = self.p1['e1']
        chain = workflow_tool.getChainForPortalType(e1.portal_type)
        self.assertEqual(len(chain), 1)
        self.assertEqual(chain[0], 'one_state_workflow')


def test_suite():
    return unittest.defaultTestLoader.loadTestsFromName(__name__)
