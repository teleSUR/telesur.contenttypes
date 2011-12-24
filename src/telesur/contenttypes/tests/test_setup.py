# -*- coding: utf-8 -*-

import unittest2 as unittest

from plone.app.testing import TEST_USER_ID
from plone.app.testing import TEST_USER_NAME
from plone.app.testing import login
from plone.app.testing import setRoles

from plone.browserlayer.utils import registered_layers

from telesur.contenttypes.config import PROJECTNAME
from telesur.contenttypes.testing import INTEGRATION_TESTING


class InstallTest(unittest.TestCase):

    layer = INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']

    def test_installed(self):
        qi = getattr(self.portal, 'portal_quickinstaller')
        self.assertTrue(qi.isProductInstalled(PROJECTNAME))

    def test_browserlayer_installed(self):
        layers = [l.getName() for l in registered_layers()]
        self.assertTrue('ITelesurContentTypesLayer' in layers,
                        'browser layer not installed')

    def test_add_permissions(self):
        permission = 'telesur.contenttypes: Add program'
        roles = self.portal.rolesOfPermission(permission)
        roles = [r['name'] for r in roles if r['selected']]
        self.assertEqual(roles, ['Contributor', 'Manager', 'Owner', 'Site Administrator'])


class UninstallTest(unittest.TestCase):

    layer = INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        login(self.portal, TEST_USER_NAME)

    def test_uninstalled(self):
        qi = getattr(self.portal, 'portal_quickinstaller')
        qi.uninstallProducts(products=[PROJECTNAME])
        self.assertTrue(not qi.isProductInstalled(PROJECTNAME))

    def test_browserlayer_uninstalled(self):
        layers = [l.getName() for l in registered_layers()]
        self.assertTrue('ITelesurContentTypesLayer' not in layers,
                        'browser layer not removed')


def test_suite():
    return unittest.defaultTestLoader.loadTestsFromName(__name__)
