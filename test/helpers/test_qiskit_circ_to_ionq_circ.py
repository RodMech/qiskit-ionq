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

"""Test the qobj_to_ionq function."""

from qiskit import QuantumCircuit

from qiskit_ionq_provider.helpers import qiskit_circ_to_ionq_circ


def test_measurement_only_circuit():
    """Test a valid circuit with only measurements."""
    qc = QuantumCircuit(1, 1)
    qc.measure(0, 0)
    expected = []
    built, _, _ = qiskit_circ_to_ionq_circ(qc)
    assert built == expected


def test_simple_circuit():
    """Test basic structure of a simple circuit"""
    qc = QuantumCircuit(1, 1)
    qc.h(0)
    qc.measure(0, 0)
    expected = [{"gate": "h", "target": 0}]
    built, _, _ = qiskit_circ_to_ionq_circ(qc)
    assert built == expected


# pylint: disable=invalid-name
def test_circuit_with_entangling_ops():
    """Test structure of circuits with entangling ops."""
    qc = QuantumCircuit(2, 2)
    qc.cnot(1, 0)
    expected = [{"gate": "x", "target": 0, "controls": [1]}]
    built, _, _ = qiskit_circ_to_ionq_circ(qc)
    assert built == expected


def test_multi_control():
    """Test structure of circuits with multiple controls"""
    qc = QuantumCircuit(3, 3)
    qc.toffoli(0, 1, 2)
    expected = [{"gate": "x", "target": 2, "controls": [0, 1]}]
    built, _, _ = qiskit_circ_to_ionq_circ(qc)
    assert built == expected
