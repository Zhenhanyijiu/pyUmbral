"""
Copyright (C) 2018 NuCypher

This file is part of pyUmbral.

pyUmbral is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published b
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

pyUmbral is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with pyUmbral. If not, see <https://www.gnu.org/licenses/>.
"""

from typing import List

from umbral.curvebn import CurveBN


def lambda_coeff(id_i: CurveBN, selected_ids: List[CurveBN]) -> CurveBN:
    ids = [x for x in selected_ids if x != id_i]

    if not ids:
        return CurveBN.from_int(1, id_i.curve)

    result = ids[0] / (ids[0] - id_i)
    for id_j in ids[1:]:
        result = result * id_j / (id_j - id_i)

    return result


def poly_eval(coeff: List[CurveBN], x: CurveBN) -> CurveBN:
    result = coeff[-1]
    for i in range(-2, -len(coeff) - 1, -1):
        result = (result * x) + coeff[i]

    return result
