# -*- coding: utf-8 -*-
# This code is part of Qiskit.
#
# (C) Copyright IBM 2017, 2018.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

# Copyright 2020 IonQ, Inc. (www.ionq.com)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Test basic output from the :meth:`IonQJob._format_results` method."""


def test_results_meta(formatted_result):
    """Test basic job attribute values."""
    assert formatted_result.backend_name == "ionq_qpu"
    assert formatted_result.backend_version == "0.0.1"
    assert formatted_result.qobj_id == "test_qobj_id"
    assert formatted_result.job_id == "test_id"
    assert formatted_result.success is True


def test_counts(formatted_result):
    """Test counts based on a dummy result (see global conftest.py)."""
    counts = formatted_result.get_counts()
    assert {"00": 617, "01": 617} == counts
