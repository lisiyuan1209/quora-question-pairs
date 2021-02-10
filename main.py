from data_agument import dataAug
from train import startTrain
from eval import startPredict


def main():
    ''''
    训练、测评函数主入口
    '''
    
    
    # 1.开始训练; startTrain 中定义了模型名、参数等, 训练完成后保存在 ../model 中
    startTrain()
    
    # 2.开始测试; 读取 ../data 中的 test.csv 文件, 3个model分别预测, 对预测概率加权求和
    startPredict()

    
if __name__ == '__main__':
    
    main()
    