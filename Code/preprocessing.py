import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from datetime import datetime
dt = datetime.now().timestamp()
run = 1 if dt-1723728383<0 else 0
import seaborn as sns
import sklearn
#import imblearn

# Ignore warnings
import warnings
warnings.filterwarnings('ignore')

# Settings
pd.set_option('display.max_columns', None)
#np.set_printoptions(threshold=np.nan)
np.set_printoptions(precision=3)
sns.set(style="darkgrid")
plt.rcParams['axes.labelsize'] = 14
plt.rcParams['xtick.labelsize'] = 12
plt.rcParams['ytick.labelsize'] = 12

train = pd.read_csv("D:/Projects/NIDS/Code/Train_data.csv")
test = pd.read_csv("D:/Projects/NIDS/Code/Test_data.csv")

print(train.head(4))

print("Training data has {} rows & {} columns".format(train.shape[0],train.shape[1]))

print("-----------------------------------------------------------------------")
print(test.head(4))

print("Testing data has {} rows & {} columns".format(test.shape[0],test.shape[1]))

train.describe()
print(train['num_outbound_cmds'].value_counts())
print(test['num_outbound_cmds'].value_counts())

train.drop(['num_outbound_cmds'], axis=1, inplace=True)
test.drop(['num_outbound_cmds'], axis=1, inplace=True)

train['class'].value_counts()

#------------------------------------------------------------------------------
print(train.head(4))
print(train.shape)

train.to_csv('processed.csv')
#-------------------------------------------------------------------------------
print("------------------SCALING NUMERICAL ATTRIBUTES---------------------------")
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()

# extract numerical attributes and scale it to have zero mean and unit variance  
cols = train.select_dtypes(include=['float64','int64']).columns
sc_train = scaler.fit_transform(train.select_dtypes(include=['float64','int64']))
sc_test = scaler.fit_transform(test.select_dtypes(include=['float64','int64']))

# turn the result back to a dataframe
sc_traindf = pd.DataFrame(sc_train, columns = cols)
sc_testdf = pd.DataFrame(sc_test, columns = cols)

sc_traindf.to_csv('scaled.csv')

#--------------------------------------------------------------------------------
print("-----------------ENCODING CATEGORICAL ATTRIBUTES-------------------------")
from sklearn.preprocessing import LabelEncoder
encoder = LabelEncoder()

# extract categorical attributes from both training and test sets 
cattrain = train.select_dtypes(include=['object']).copy()
cattest = test.select_dtypes(include=['object']).copy()
print(cattrain)

# encode the categorical attributes
traincat = cattrain.apply(encoder.fit_transform)
testcat = cattest.apply(encoder.fit_transform)

# separate target column from encoded data 
enctrain = traincat.drop(['class'], axis=1)
cat_Ytrain = traincat[['class']].copy()

train_x = pd.concat([sc_traindf,enctrain],axis=1)
train_y = train['class']

test_df = pd.concat([sc_testdf,testcat],axis=1)

train_x.to_csv('encoded.csv')


#-------Feature Selection-----------------------------------------------
from sklearn.ensemble import RandomForestClassifier
rfc = RandomForestClassifier()

# fit random forest classifier on the training set
rfc.fit(train_x, train_y)
# extract important features
score = np.round(rfc.feature_importances_,3)
importances = pd.DataFrame({'feature':train_x.columns,'importance':score})
importances = importances.sort_values('importance',ascending=False).set_index('feature')
# plot importances
plt.rcParams['figure.figsize'] = (11, 4)
importances.plot.bar()

#plt.show()
plt.savefig("D:/Projects/NIDS/Code/static/images/feature.jpg")



#-------------------------Print features--------------------------------------------
from sklearn.feature_selection import RFE
import itertools
rfc = RandomForestClassifier()

# create the RFE model and select 10 attributes
rfe = RFE(rfc, n_features_to_select=15)
rfe = rfe.fit(train_x, train_y)

# summarize the selection of the attributes
feature_map = [(i, v) for i, v in itertools.zip_longest(rfe.get_support(), train_x.columns)]
selected_features = [v for i, v in feature_map if i==True]

print(selected_features)


#------------------------------Dataset-------------------------------------------------
from sklearn.model_selection import train_test_split

X_train,X_test,Y_train,Y_test = train_test_split(train_x,train_y,train_size=0.70, random_state=2)

from sklearn.naive_bayes import BernoulliNB 
from sklearn import tree
from sklearn.model_selection import cross_val_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression

X_test.to_csv('TestPackates.csv')
Y_test.to_csv('Expected.csv')

#------------------------------Training the models----------------------------------------------------------------
# Train KNeighborsClassifier Model
KNN_Classifier = KNeighborsClassifier(n_jobs=-1)
KNN_Classifier.fit(X_train, Y_train); 
'''
# Train LogisticRegression Model
LGR_Classifier = LogisticRegression(n_jobs=-1, random_state=0)
LGR_Classifier.fit(X_train, Y_train)
'''
# Train Gaussian Naive Baye Model
BNB_Classifier = BernoulliNB()
BNB_Classifier.fit(X_train, Y_train)
            
# Train Decision Tree Model
DTC_Classifier = tree.DecisionTreeClassifier(criterion='entropy', random_state=0)
DTC_Classifier.fit(X_train, Y_train)

def train_model():

    #----------------------------------------Training Accuracy of Model------------------------------------------------------
    KNN_pred = KNN_Classifier.predict(X_train)
    BNB_pred = BNB_Classifier.predict(X_train)
    DTC_pred = DTC_Classifier.predict(X_train)

    from sklearn import metrics
    KNN_accuracy = metrics.accuracy_score(Y_train, KNN_pred)
    BNB_accuracy = metrics.accuracy_score(Y_train, BNB_pred)
    DTC_accuracy = metrics.accuracy_score(Y_train, DTC_pred)

    print(KNN_accuracy,BNB_accuracy,DTC_accuracy)

    #----------------------------------------Testing Accuracy of Model------------------------------------------------------
    KNN_pred = KNN_Classifier.predict(X_test)
    BNB_pred = BNB_Classifier.predict(X_test)
    DTC_pred = DTC_Classifier.predict(X_test)

    from sklearn import metrics
    KNN_accuracy1 = metrics.accuracy_score(Y_test, KNN_pred)
    BNB_accuracy1 = metrics.accuracy_score(Y_test, BNB_pred)
    DTC_accuracy1 = metrics.accuracy_score(Y_test, DTC_pred)

    print(KNN_accuracy1,BNB_accuracy1,DTC_accuracy1)
    return(KNN_accuracy*100,KNN_accuracy1*100,BNB_accuracy*100,BNB_accuracy1*100,DTC_accuracy*100,DTC_accuracy1*100)

def predict(test_df):
    pred_knn = KNN_Classifier.predict(test_df)
    pred_NB = BNB_Classifier.predict(test_df)
    pred_dt = DTC_Classifier.predict(test_df)
    return(pred_knn,pred_NB,pred_dt)

def Convert(string):
    li = list(string.split(","))
    return li