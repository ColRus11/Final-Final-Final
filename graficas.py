def graficar(data_sets, plot_type="scatter", width=50, height=25, symbols=['*']):
    grid = [[' ' for _ in range(width)] for _ in range(height)]
    
    # Normalizar todos los puntos para escalar
    all_x = []
    all_y = []
    for points in data_sets:
        if all(isinstance(p, (int, float)) for p in points):
            points = [[i, p] for i, p in enumerate(points)]
        all_x.extend(p[0] for p in points)
        all_y.extend(p[1] for p in points)
    
    x_min, x_max = min(all_x), max(all_x)
    y_min, y_max = min(all_y), max(all_y)
    
    if x_max == x_min:
        x_max += 1
    if y_max == y_min:
        y_max += 1
    
    # Dibujar ejes
    zero_x = int((-x_min) / (x_max - x_min) * (width - 1)) if x_min <= 0 <= x_max else None
    if zero_x is not None:
        for y in range(height):
            grid[y][zero_x] = '|' if grid[y][zero_x] == ' ' else grid[y][zero_x]
    
    zero_y = int((y_max) / (y_max - y_min) * (height - 1)) if y_min <= 0 <= y_max else None
    if zero_y is not None:
        for x in range(width):
            grid[zero_y][x] = '-' if grid[zero_y][x] == ' ' else grid[zero_y][x]
    
    # Dibujar cada conjunto de puntos
    for idx, points in enumerate(data_sets):
        symbol = symbols[idx % len(symbols)]  
        if all(isinstance(p, (int, float)) for p in points):
            points = [[i, p] for i, p in enumerate(points)]
        
        if plot_type == "scatter":
            for x, y in points:
                grid_x = int((x - x_min) / (x_max - x_min) * (width - 1))
                grid_y = int((y - y_min) / (y_max - y_min) * (height - 1))
                if 0 <= grid_x < width and 0 <= grid_y < height:
                    grid[height - 1 - grid_y][grid_x] = symbol
        elif plot_type == "line":
            for i in range(len(points) - 1):
                x1, y1 = points[i]
                x2, y2 = points[i + 1]
                grid_x1 = int((x1 - x_min) / (x_max - x_min) * (width - 1))
                grid_y1 = int((y1 - y_min) / (y_max - y_min) * (height - 1))
                grid_x2 = int((x2 - x_min) / (x_max - x_min) * (width - 1))
                grid_y2 = int((y2 - y_min) / (y_max - y_min) * (height - 1))
                dx = grid_x2 - grid_x1
                dy = grid_y2 - grid_y1
                steps = max(abs(dx), abs(dy)) or 1
                for j in range(steps + 1):
                    t = j / steps
                    x = int(grid_x1 + t * dx)
                    y = int(grid_y1 + t * dy)
                    if 0 <= x < width and 0 <= y < height:
                        grid[height - 1 - y][x] = symbol
        else:
            raise ValueError(f"Tipo de gráfico no soportado: {plot_type}")
    
    # Imprimir cuadrícula con bordes
    print(f"Gráfica ASCII ({plot_type}):")
    print('+' + '-' * width + '+')
    for row in grid:
        print('|' + ''.join(row) + '|')
    print('+' + '-' * width + '+')
    print(f"x: [{x_min:.2f}, {x_max:.2f}], y: [{y_min:.2f}, {y_max:.2f}]")
    print(f"Símbolos: {', '.join(s for s in symbols[:len(data_sets)])}")