import pandas as pd
import csv

# 导入文件的路径是自己存放文件的位置
data = pd.read_csv('./Data/dataset.csv', encoding='gbk')
data = pd.DataFrame(data)  # 转化为 DataFrame 格式
# print(data)  # 测试是否读取成果


# 以天为单位提取单车数据
def data_per_day():
    for i in range(1, 32):
        # 1.创建用于存放被提取数据的容器
        information = []

        # 2.遍历提取对应日期的数据
        for index, row_data in data.iterrows():
            date = row_data['start_time'].split(' ')[0].split('/')[-1]
            if date == str(i):
                information.append(row_data)

        # 3.将数据写入相应的.csv文件中
        head = ['orderid', 'bikeid', 'userid', 'start_time', 'start_location_x',
                'start_location_y', 'end_time', 'end_location_x', 'end_location_y', 'track']
        with open(f"./Data/everyday_data/day{i}.csv", 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(head)  # 写入首行标题
            writer.writerows(information)  # 写入具体信息

        # 提示程序运行进展
        print(f"Done the {i}th day of August in 2016")


# 2.建立单车数据集，对每辆单车的初始位置进行记录
def bike_record():
    # 设置单车编号集合（去重）
    bike_set = set()
    # 用于存放单车初始位置信息
    bike_information = []
    # 统计单车数量
    count = 0

    for index, row_data in data.iterrows():
        bike_id = row_data['bikeid']
        # 对于首次出现的单车，添加到单车信息表中
        if bike_id not in bike_set:
            bike_set.add(bike_id)  # 添加单车编号到集合中，用于去重
            count += 1
            # 构造单车初始位置信息：单车编号、初始经度、初始纬度 (保留三位小数)
            init_x = row_data['start_location_x']
            init_y = row_data['start_location_y']
            information = [bike_id, init_x, init_y]

            bike_information.append(information)

    head = ['bikeid', 'start_location_x', 'start_location_y']
    with open("./Data/init_bike_loc.csv", 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(head)  # 写入首行标题
        writer.writerows(bike_information)  # 写入具体信息

    # The total number of bike is: 79062.
    print(f"The total number of bike is: {count}.\n")


if __name__ == '__main__':
    data_per_day()

    bike_record()
