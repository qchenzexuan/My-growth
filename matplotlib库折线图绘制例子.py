from random import randint #调用random库中的randint方法
import matplotlib.pyplot as plt #调用 matplotlib 库

#生成随机数函数，传入生成随机数的个数
def random(age):
    data = list()
    for i in range(age):
        data.append(randint(1,100))
    return data

#生成初始数据
x = list(range(1,13))
y = random(12)

x1 = list(range(1,13))
y1 = random(12)

#绘制一个二维折线图，label为对线段进行命名
plt.plot(x,y,label='Company A')
plt.plot(x1,y1,label='Company B')

plt.legend() #增加图例，必须先对线段进行命名
plt.xlabel('Month') #对x轴进行命名
plt.ylabel('Sales') #对y轴进行命名
plt.title('Sales of Company') #命名标题

plt.show() #展示数据