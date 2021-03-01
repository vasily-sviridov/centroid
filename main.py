from shapely.geometry import Polygon


def main():
    print('Введите количество вершин:')
    count_of_vertex = int(input())
    list_of_vertex = []
    print('Введите координаты вершин:')
    for i in range(count_of_vertex):
        x, y = map(float, input().split())
        list_of_vertex.append([x, y])

    p = Polygon(list_of_vertex)

    print(p.centroid)


if __name__ == "__main__":
    main()

