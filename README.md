# 基于opencv、tensorflow的人脸识别
  **BY**  [GJ](https://github.com/Acemyzoe/face-recognition)
## 使用指南
1. 运行catch_face.py获取自己的脸  
>或者catch_face_cv.py，图片将保存在myface文件夹（可自定义）。      

2. 可使用other_face.py处理其他r人的图片。  
>例如处理lfw图片集。  

3. face_data.py作为模块用于后续图片的预处理。

4. 运行face_train.py来训练神经网络。  
>载入的数据集即为face_data文件夹，包含myface文件夹和other_faces文件夹。  *训练过程，终端显示每一波训练时训练和测试的损失和准确率，训练结束将模型保存至model文件夹。*   

5. 运行face_r.py可以打开摄像头开始识别我的脸了。