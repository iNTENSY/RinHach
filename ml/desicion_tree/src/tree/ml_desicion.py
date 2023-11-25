import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report, accuracy_score


class Treehandler:
    def __init__(self):
        self.df = self.get_df()
        self.model = DecisionTreeClassifier()
        self.prediction = None

    def get_df(self):
        df = pd.read_csv("fraud_dataset.csv", sep="|")
        # df = df.drop(columns="customer")

        le = LabelEncoder()
        for column in [
            "customer",
            "gender",
            "category",
            "step",
            "age",
            "zipMerchant",
            "zipcodeOri",
            "merchant",
        ]:
            df[column] = le.fit_transform(df[column])

        return df

    def input_split(self):
        return self.df.loc[:, "step":"amount"]

    def output_split(self):
        return self.df["fraud"]

    def train_split(self):
        X_train, X_test, y_train, y_test = train_test_split(
            self.input_split(), self.output_split(), test_size=0.2
        )
        self.model = self.model.fit(X_train, y_train)

        self.prediction = self.model.predict(X_test)
        return classification_report(y_test, self.prediction)
        # return accuracy_score(y_test, self.prediction)
        # return self.model.score(X_train, y_train), self.model.score(X_test, y_test)
        # return len([transaction for transaction in self.prediction if transaction])

    def get_result(self):
        """
        При создании обьекта необходимо нужно вызывать данный метод для получения результатов
        """
        return self.train_split()


a = Treehandler()
print(a.get_result())
