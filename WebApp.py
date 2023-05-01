from flask import Flask, request, abort
from Solution import Solution

app = Flask(__name__)


def parse_matrix_data(matrix_height, matrix_width, matrix_string):
    string = matrix_string.split(" ")

    matrix = [[0] for i in range(matrix_height)]
    matrix_index = 0
    for height in range(matrix_height):
        matrix[height] = []
        for width in range(matrix_width):
            matrix[height].append(int(string[matrix_index]))
            matrix_index += 1
    return matrix


@app.route('/', methods=['GET', 'POST'])
def hello_world():

    if request.method == 'POST':
        try:
            height = request.form['height']
            width = request.form['width']
            matrix_data = request.form['matrix_data']
            if int(height) * int(width) != len(matrix_data.split(" ")):
                raise ValueError
            matrix = parse_matrix_data(int(height), int(width), matrix_data)
            return str(Solution.longest_increasing_path(matrix))
        except ValueError:
            abort(400)
            return "Ошибка: введенные данные некорректны"

    return f'<html>' \
           f'<head>' \
           f'<title>Longest Increasing Path In a Matrix</title>' \
           f'</head>' \
           f'<body>' \
           f'<h1 id="header">Longest Increasing Path In a Matrix</h1>' \
           f'<form action="/" method="POST">' \
           f'<h3 id="header_height">Введите высоту матрицы</h3>' \
           f'<input type="text" id="height" name="height" /><br />' \
           f'<h3 id="header_width">Введите ширину матрицы</h3>' \
           f'<input type="text" id="width" name="width" /><br />' \
           f'<h3 id="header_matrix_data">Введите содержимое матрицы через пробел</h3>' \
           f'<input type="text" id="matrix_data" name="matrix_data"/><br /><br />' \
           f'<input id="submit" type="submit" />' \
           f'</form>' \
           f'</body>' \
           f'</html>'
