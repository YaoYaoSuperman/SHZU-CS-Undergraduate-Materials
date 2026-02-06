import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, roc_curve, auc
from sklearn.metrics import precision_score, recall_score, f1_score

# 读取数据
df = pd.read_csv('/Users/luyao/Desktop/课内/DM/EX/实验五 分类实验-DT Bayes RF/rumor.txt', sep='\t')

# 准备数据
x, y = df.iloc[:, 0:12].values, df.iloc[:, 13].values
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)
feat_labels = df.columns[0:12]

# 定义模型
models = {
    'Random Forest': RandomForestClassifier(n_estimators=100, random_state=0, n_jobs=-1),
    'Decision Tree': DecisionTreeClassifier(random_state=0),
    'Naive Bayes': GaussianNB()
}

# 训练和评估模型
for name, model in models.items():
    model.fit(x_train, y_train)
    y_pred = model.predict(x_test)
    probas = model.predict_proba(x_test)
    fpr, tpr, thresholds = roc_curve(y_test, probas[:, 1])
    roc_auc = auc(fpr, tpr)

    # 打印评价指标
    print(f"{name}:")
    print("  Accuracy: ", accuracy_score(y_test, y_pred))
    print("  Precision: ", precision_score(y_test, y_pred))
    print("  Recall: ", recall_score(y_test, y_pred))
    print("  F1-Score: ", f1_score(y_test, y_pred))
    print("  Confusion Matrix:\n", confusion_matrix(y_test, y_pred))

    # 绘制ROC曲线
    plt.figure()
    plt.plot(fpr, tpr, label=f'AUC = {roc_auc:.2f}')
    plt.plot([0, 1], [0, 1], 'k--')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title(f'ROC Curve for {name}')
    plt.legend(loc="lower right")
    plt.savefig(f'/Users/luyao/Desktop/课内/DM/EX/实验五 分类实验-DT Bayes RF/ROC_{name}.png')
    plt.show()

