import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:

    # group by managerId, then filter out count > 5
    # 你可以使用 .groupby() 方法对 'managerId' 列进行分组，然后使用 .size() 方法计算每个经理（manager）所管理的员工数量
    # reset_index(name = 'directReports')重新设置索引并为重置后的索引添加一个新的名称
    manager_count = employee.groupby('managerId').size().reset_index(name = 'directReports')

    # filter out data that managers with at least 5 direct reports
    result = manager_count[manager_count['directReports'] >= 5]

    # merge with the employee table to get the names of managers
    result = result.merge(employee[['id', 'name']], left_on = 'managerId', right_on = 'id', how = 'inner')

    # select required col
    result = result[['name']]

    return result