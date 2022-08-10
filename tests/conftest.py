# Copyright 2022 Pulser Development Team
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import numpy as np
import pytest

from pulser.channels import Raman, Rydberg
from pulser.devices import Device


@pytest.fixture
def mod_device() -> Device:
    return Device(
        name="ModDevice",
        dimensions=3,
        rydberg_level=70,
        max_atom_num=2000,
        max_radial_distance=1000,
        min_atom_distance=1,
        _channels=(
            (
                "rydberg_global",
                Rydberg(
                    "Global",
                    1000,
                    200,
                    clock_period=1,
                    min_duration=1,
                    mod_bandwidth=4.0,  # MHz
                ),
            ),
            (
                "rydberg_local",
                Rydberg(
                    "Local",
                    2 * np.pi * 20,
                    2 * np.pi * 10,
                    max_targets=2,
                    phase_jump_time=0,
                    fixed_retarget_t=0,
                    min_retarget_interval=220,
                    mod_bandwidth=4.0,
                ),
            ),
            (
                "raman_local",
                Raman(
                    "Local",
                    2 * np.pi * 20,
                    2 * np.pi * 10,
                    max_targets=2,
                    phase_jump_time=0,
                    fixed_retarget_t=0,
                    min_retarget_interval=220,
                    mod_bandwidth=4.0,
                ),
            ),
        ),
    )
