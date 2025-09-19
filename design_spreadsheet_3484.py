# https://leetcode.com/problems/design-spreadsheet/description/?envType=daily-question&envId=2025-09-19

class Spreadsheet:

    def __init__(self, rows: int):

        self.rows_cols = [
            {chr(c): 0 for c in range(65, 91)} for r in range(rows)
            ]
        

    def setCell(self, cell: str, value: int) -> None:
        # print(f"Setting {cell[0]}{int(cell[1:])-1} to {value}")
        self.rows_cols[int(cell[1:])-1][cell[0]] = value

    def resetCell(self, cell: str) -> None:
        self.rows_cols[int(cell[1:])-1][cell[0]] = 0

    def getValue(self, formula: str) -> int:
        c1, c2 = formula[1:].split("+")

        if 90>= ord(c1[0]) >= 65:
            c1_v = self.rows_cols[int(c1[1:])-1][c1[0]]
        else:
            c1_v = int(c1)

        if 90>= ord(c2[0]) >= 65:
            c2_v = self.rows_cols[int(c2[1:])-1][c2[0]]
        else:
            c2_v = int(c2)

        return c1_v + c2_v


# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)