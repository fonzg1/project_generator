# Copyright 2015 0xc0170
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import os

from unittest import TestCase

from project_generator.settings import ProjectSettings
from project_generator.tools.iar import IARDefinitions, IAREmbeddedWorkbench

class TestProject(TestCase):

    """test things related to the iar tool"""

    def setUp(self):
        self.defintions = IARDefinitions()
        workspace_dic = {
            'projects': [],
            'settings': {},
        }
        self.iar = IAREmbeddedWorkbench(workspace_dic, ProjectSettings())

    def test_export(self):
        self.iar.export_project()
