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

__version__ = '0.0.1'
__all__ = ['has_conflict']

from collections import defaultdict
from typing import Mapping, Sequence, Tuple

from packaging.specifiers import SpecifierSet


def multimap(specs: Sequence[Tuple[str, str]]) -> Mapping[str, SpecifierSet]:
    """Convert a sequence of pairs to a multimap of version specifiers.

    >>> multimap([('x', '<420'), ('y', '>6'), ('y', '==9')])
    {'x': <SpecifierSet('<420')>, 'y': <SpecifierSet('==9,>6')>}
    """
    result = defaultdict(list)
    for name, version_spec in specs:
        result[name].append(version_spec)
    return {name: SpecifierSet(','.join(specifiers))
            for name, specifiers in result.items()}


def has_conflict(versions: Mapping[str, str],
                 specifiers: Sequence[Tuple[str, str]]) -> bool:
    """Check if versions do not satisfy dependency specifications.

    >>> has_conflict({'x': '6.9', 'y': '4.20'},
    ...              [('x', '>6'), ('x', '<9'), ('y', '==4.20')])
    False
    >>> has_conflict({'x': '6.9', 'y': '4.2'},
    ...              [('x', '>6'), ('x', '<9'), ('y', '==4.20')])
    True
    """
    for name, specs in multimap(specifiers).items():
        if versions[name] not in specs: return True
    return False
