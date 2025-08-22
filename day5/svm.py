import numpy as np
from sklearn import datasets,svm,metrics
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
#load digits datasets 8*8 grayscale
#load digits datasets
digits=datasets.load_digits()
X=digits.images
y=digits.target
n_samples=len(X)
X=X.reshape((n_samples,-1))
#train and test
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.5,shuffle=False)
#create and rain knn model (k=s)
clf=svm.SVC(gamma=0.001)
clf.fit(X_train,y_train)
y_pred=clf.predict(X_test)
print("SVM Accuracy:",metrics.accuracy_score(y_test,y_pred))
images_and_prediction=list(zip(digits.images[n_samples//2:],y_pred))
for index,(images,prediction) in enumerate(images_and_prediction[:4]):
    plt.subplot(1,4,index+1)
    plt.axis("off")
    plt.imshow(images,cmap=plt.cm.gray_r,interpolation="nearest")
    plt.title(f"pred:{prediction}")
plt.show()