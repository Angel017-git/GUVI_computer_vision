import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets,metrics
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
#load digits datasets
digits=datasets.load_digits()
X=digits.images
y=digits.target
n_samples=len(X)
X=X.reshape((n_samples,-1))
#train and test
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.5,shuffle=False)
#create and rain knn model (k=s)
knn=KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train,y_train)
y_pred=knn.predict(X_test)
print("KNN Accuracy:",metrics.accuracy_score(y_test,y_pred))
images_and_prediction=list(zip(digits.images[n_samples//2:],y_pred))
for index,(images,prediction) in enumerate(images_and_prediction[:4]):
    plt.subplot(1,4,index+1)
    plt.axis("off")
    plt.imshow(images,cmap=plt.cm.gray_r,interpolation="nearest")
    plt.title(f"pred:{prediction}")
plt.show()    