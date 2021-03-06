# -*- coding: utf-8 -*-

import unittest2 as unittest

from zope.component import createObject
from zope.component import queryUtility

from plone.app.testing import TEST_USER_ID
from plone.app.testing import setRoles

from plone.app.referenceablebehavior.referenceable import IReferenceable
from plone.dexterity.interfaces import IDexterityFTI
from plone.uuid.interfaces import IAttributeUUID

from telesur.contenttypes.program import IProgram
from telesur.contenttypes.testing import INTEGRATION_TESTING


class IntegrationTest(unittest.TestCase):

    layer = INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.portal.invokeFactory('Folder', 'test-folder')
        setRoles(self.portal, TEST_USER_ID, ['Member'])
        self.folder = self.portal['test-folder']

    def test_adding(self):
        self.folder.invokeFactory('telesur.contenttypes.program', 'p1')
        p1 = self.folder['p1']
        self.failUnless(IProgram.providedBy(p1))

    def test_fti(self):
        fti = queryUtility(IDexterityFTI, name='telesur.contenttypes.program')
        self.assertNotEquals(None, fti)

    def test_schema(self):
        fti = queryUtility(IDexterityFTI, name='telesur.contenttypes.program')
        schema = fti.lookupSchema()
        self.assertEquals(IProgram, schema)

    def test_factory(self):
        fti = queryUtility(IDexterityFTI, name='telesur.contenttypes.program')
        factory = fti.factory
        new_object = createObject(factory)
        self.failUnless(IProgram.providedBy(new_object))

    def test_is_referenceable(self):
        self.folder.invokeFactory('telesur.contenttypes.program', 'p1')
        p1 = self.folder['p1']
        self.assertTrue(IReferenceable.providedBy(p1))
        self.assertTrue(IAttributeUUID.providedBy(p1))

    def test_default_workflow(self):
        workflow_tool = getattr(self.portal, 'portal_workflow')
        self.folder.invokeFactory('telesur.contenttypes.program', 'p1')
        p1 = self.folder['p1']
        chain = workflow_tool.getChainForPortalType(p1.portal_type)
        self.assertEqual(len(chain), 1)
        self.assertEqual(chain[0], 'one_state_workflow')


def test_suite():
    return unittest.defaultTestLoader.loadTestsFromName(__name__)
