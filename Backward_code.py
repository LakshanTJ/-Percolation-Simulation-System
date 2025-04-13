import random
from datetime import datetime

# Function to generate a random grid with specified dimensions
def generate_grid(rows, cols):
    grid = []
    for _ in range(rows):
        row = []
        for _ in range(cols):
            if random.random() < 0.3:  
                row.append(None)
            else:
                row.append(random.randint(10, 99))
        grid.append(row)
    return grid


# Function to display the grid and check percolation
# Check column filling for each column
def display_and_check(grid):
    max_cell_width = max(len(str(cell)) if cell is not None else 0 for row in grid for cell in row)
    result = ""
    column_filling = []  
    
    for row in grid:
        for cell in row:
            if cell is None:
                result += f" {'':>{max_cell_width}}|"  
            else:
                result += f" {cell:>{max_cell_width}}|"
        result += "\n" + '_' * (max_cell_width + 2) * len(row)+"\n"
        

    
    for col_index in range(len(grid[0])):
        column = [row[col_index] for row in grid]
        column_filling_result = check_column_filling(column)
        column_filling.append(column_filling_result)
    for fill in column_filling:
        result += f" {fill}|"
    return result, column_filling

# Function to check if percolation is possible for a column
def check_column_filling(column):
    for cell in column:
        if cell is None:  
            return 'NO'
    return 'OK'

# Function to save result to a text file
def save_to_file(result):
    now = datetime.now()
    file_name = now.strftime("%Y_%m_%d_%H%M") + '.txt'
    with open(file_name, 'w') as file:
        file.write(result)
    file.close()   

# Function to generate and save HTML file
def generate_html(grid, column_filling):
    now = datetime.now()
    file_name = now.strftime("%Y_%m_%d_%H%M") + '.html'
    with open(file_name, 'w') as file:
        file.write('''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=4.0">
<title>Percolation Result</title>
</head>
<body>

<table border="10">\n''')
        for row in grid:
            file.write('<tr>\n')
            for cell in row:
                if cell is None:
                    file.write('<td></td>')
                else:
                    file.write('<td>{}</td>'.format(cell))
            file.write('</tr>\n')
        file.write('<tr>\n')
        for result in column_filling:
            file.write('<td>{}</td>'.format(result))
        file.write('</tr>\n')
        file.write('''</table>
</body>
</html>''')


