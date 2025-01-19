from collections import defaultdict, deque

class Formula:
    def __init__(self, constants, dependent_cells):
        self.constants = constants
        self.dependent_cells = dependent_cells

    def evaluate(self, evaluations):
        total = sum(self.constants)
        for cell in self.dependent_cells:
            row, col = CoordinateUtil.cell_to_2d_coordinate(cell)
            total += evaluations[row][col]
        return total


class Cell:
    CONSTANT = "CONSTANT"
    FORMULA = "FORMULA"

    def __init__(self, constant=None, formula=None):
        if formula is not None:
            self.type = Cell.FORMULA
            self.formula = formula
        else:
            self.type = Cell.CONSTANT
            self.constant = constant

    def evaluate(self, evaluations):
        if self.type == Cell.CONSTANT:
            return self.constant
        return self.formula.evaluate(evaluations)


class CoordinateUtil:
    @staticmethod
    def cell_to_2d_coordinate(cell):
        col = ord(cell[0]) - ord('A')
        row = int(cell[1]) - 1
        return row, col

    @staticmethod
    def cell_to_1d_coordinate(cell, total_cols):
        row, col = CoordinateUtil.cell_to_2d_coordinate(cell)
        return row * total_cols + col

    @staticmethod
    def to_1d_coordinate(coordinate_2d, total_cols):
        row, col = coordinate_2d
        return row * total_cols + col

    @staticmethod
    def to_2d_coordinate(coordinate_1d, total_cols):
        row = coordinate_1d // total_cols
        col = coordinate_1d % total_cols
        return row, col


class ExcelSpreadsheet:
    def compute_spreadsheet(self, spreadsheet):
        rows = len(spreadsheet)
        cols = len(spreadsheet[0])
        graph = defaultdict(list)
        indegrees = [0] * (rows * cols)

        # Build the dependency graph
        for i in range(rows):
            for j in range(cols):
                cell = spreadsheet[i][j]
                if cell.type == Cell.FORMULA:
                    for dependent_cell in cell.formula.dependent_cells:
                        dep_1d = CoordinateUtil.cell_to_1d_coordinate(dependent_cell, cols)
                        current_1d = CoordinateUtil.to_1d_coordinate((i, j), cols)
                        graph[dep_1d].append(current_1d)
                        indegrees[current_1d] += 1

        # Initialize queue with cells having no dependencies
        queue = deque()
        for i in range(rows * cols):
            if indegrees[i] == 0:
                queue.append(i)

        evaluations = [[0] * cols for _ in range(rows)]

        # Process the graph using topological sort
        while queue:
            cell_1d = queue.popleft()
            row, col = CoordinateUtil.to_2d_coordinate(cell_1d, cols)
            evaluations[row][col] = spreadsheet[row][col].evaluate(evaluations)

            for dependent_cell_1d in graph[cell_1d]:
                indegrees[dependent_cell_1d] -= 1
                if indegrees[dependent_cell_1d] == 0:
                    queue.append(dependent_cell_1d)

        return evaluations

    def print_spreadsheet(self, spreadsheet):
        for row in spreadsheet:
            print(row)
        print()


# Example Usage
if __name__ == "__main__":
    excel = ExcelSpreadsheet()

    # Example 1
    spreadsheet = [
        [Cell(constant=1), Cell(formula=Formula([2], ["A1"]))]
    ]
    excel.print_spreadsheet(excel.compute_spreadsheet(spreadsheet))

    # Example 2
    spreadsheet2 = [
        [Cell(constant=1), Cell(constant=4)],
        [Cell(constant=3), Cell(constant=3)]
    ]
    excel.print_spreadsheet(excel.compute_spreadsheet(spreadsheet2))

    # Example 3
    spreadsheet3 = [
        [Cell(constant=2), Cell(formula=Formula([5], ["A1"]))],
        [Cell(formula=Formula([1], ["B3"])), Cell(formula=Formula([2], ["A1", "B1"]))],
        [Cell(formula=Formula([], ["B2"])), Cell(constant=4)]
    ]
    excel.print_spreadsheet(excel.compute_spreadsheet(spreadsheet3))