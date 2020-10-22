# Simpleton's conflict checker
# Copyright (C) 2020  Nguyễn Gia Phong
#
# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU Lesser General Public License as published
# by the Free Software Foundation, either version 3 of the License,
# or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

"""Simpleton's conflict checker"""

__version__ = '0.0.2'
__all__ = ['has_conflict']

from typing import Mapping, Sequence

from packaging.requirements import Requirement


def has_conflict(versions: Mapping[str, str],
                 requirements: Sequence[str]) -> bool:
    """Check if versions do not satisfy dependency specifications.

    >>> has_conflict({'x': '6.9', 'y': '4.20'},
    ...              ['x>6', 'x<9', 'y==4.20'])
    False
    >>> has_conflict({'x': '6.9', 'y': '4.2'},
    ...              ['x>6', 'x<9', 'y==4.20'])
    True
    """
    for req in map(Requirement, requirements):
        if versions[req.name] not in req.specifier: return True
    return False
