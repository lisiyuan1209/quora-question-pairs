# quora-question-pairs
quora-question-pairs based on bert 
## 1. data_loader 用于加载数据
## 2. models 三个模型：bert+fc, bert+textcnn, bert+rcnn
## 3. train 训练模型，使用对抗训练和early_stopping防止过拟合
## 4. prediction 模型预测，融合三个模型
## 5. main 运行train和prediction
