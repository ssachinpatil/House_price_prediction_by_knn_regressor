
import numpy as np
import pickle,json


class house():
    def __init__(self,X1transactiondate,X2houseage,X3distancetothenearestMRTstation,X4numberofconveniencestores,X5latitude,X6longitude):
        self.a=X1transactiondate
        self.b=X2houseage
        self.c=X3distancetothenearestMRTstation
        self.d=X4numberofconveniencestores
        self.e=X5latitude
        self.f=X6longitude


    def pred(self):

        with open("real_estate.pkl","rb") as f:
            self.knn=pickle.load(f)

    
        with open("json_data.json","r") as f:
            self.json_data=json.load(f)
    def pred1(self):
        self.pred()
    
        array=np.array([self.a,self.b,self.c,self.d,self.e,self.f])
        prediction=self.knn.predict([array])[0]
        print(prediction)
        return prediction
if __name__=="__main__":
    x=house(2013.455,12,1200.44,8,24.98454,121.5467)
    x.pred1()