import Backward_code as pro
import sys
# Main function
def main():
    dimensions_input = input("Enter the grid size (e.g., '3x3'): ").strip()
    if dimensions_input == "":
        rows, cols = 5, 5
    else:
        try:
            rows, cols = map(int, dimensions_input.lower().split('x'))
        except ValueError:
            print('Invalid input: "Please use Letter [x]","Do not use multiplication symbol [*]".')
            return
    
        if rows < 3 or cols < 3 or rows > 9 or cols > 9:
            print("Invalid input: Dimensions must be between 3x3 and 9x9")
            return

    grid = pro.generate_grid(rows, cols)
    result,column_filling = pro.display_and_check(grid)
    print(result)
    pro.save_to_file(result)
    pro.generate_html(grid,column_filling)

if __name__ == "__main__":
    main()

