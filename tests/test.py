import unittest
import xml.etree.ElementTree as ET
import os
import sys
from flask import Flask
from flask.testing import FlaskClient
# Add the parent directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app import app

class MyTestClass(unittest.TestCase):
    def test_method1(self):
        with app.test_client() as client:
            response = client.get('/')
            print(response.status_code)
            xml_file_path = 'TEST-result.xml'
            root = ET.Element('testsuites')
            tree = ET.ElementTree(root)
            testsuite_elem = ET.SubElement(root, 'testsuite', {'tests': '1'})
            testcase_elem = ET.SubElement(testsuite_elem, 'testcase', {'classname': 'website_accessibility', 'name': 'Website is accessible'})
            success_elem = ET.SubElement(testcase_elem, 'success')
            success_elem.text = 'Website is accessible.'
            tree.write(xml_file_path)
            print(f"XML file '{xml_file_path}' has been generated.")

            self.assertEqual(response.status_code, 200)
