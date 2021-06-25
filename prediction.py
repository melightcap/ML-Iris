from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC
from loadData import loadData
from evaluateAlgorithms import validation

# Load dataset
names, dataset = loadData()

# Split-out validation dataset
array, X_train, X_validation, Y_train, Y_validation = validation()

# Make predictions
# Make predictions on validation dataset
model = SVC(gamma='auto')
model.fit(X_train, Y_train)
predictions = model.predict(X_validation)

# Evaluate predictions
print(accuracy_score(Y_validation, predictions))
print(confusion_matrix(Y_validation, predictions))
print(classification_report(Y_validation, predictions))