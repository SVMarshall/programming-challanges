
def find_common_manager(employees, current, employee_1, employee_2):

    employee_1_found = current == employee_1
    employee_2_found = current == employee_2
    printed = False

    if current in employees:
        for child in employees[current]:
            if not employee_1_found or not employee_2_found:
                found1, found2, yet_printed = find_common_manager(employees, child, employee_1, employee_2)
                employee_1_found = employee_1_found or found1
                employee_2_found = employee_2_found or found2
                if employee_1_found and employee_2_found and not yet_printed:
                    printed = True
                    print(current)

    return employee_1_found, employee_2_found, printed


def OutputCommonManager(count):
    employees = {}

    # first, get the two selected employees
    employee_1 = str(input())
    employee_2 = str(input())

    # Build the tree from input
    top = None
    while True:
        try:
            a, b = map(str, input().strip().split())

            if top is None:
                top = a

            if a not in employees:
                employees[a] = [b]
            else:
                employees[a].append(b)

        except EOFError:
            break

    # DFS
    find_common_manager(employees, top, employee_1, employee_2)


_count = int(input())
OutputCommonManager(_count)
