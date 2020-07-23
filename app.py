from flask import Flask,request
from flask_restful import Api, Resource, reqparse, fields
import pymongo
app = Flask(__name__)
api = Api(app)
myclient = pymongo.MongoClient("mongodb+srv://kds:Password123@cluster0.gohov.mongodb.net/transport?retryWrites=true&w=majority")
mydb =myclient['transport']
mycol=mydb['trips']
class Video(Resource):
    def post(self):
        f=int(request.form['f'])#from_station
        t=int(request.form['t'])#to_station
        h=int(request.form['h'])#hour
        d=int(request.form['d'])# Monday=0, Sunday=6
        ret_obj={}
        est=0
        myquery = { "hour": str(h),"from_station_id": str(f),"to_station_id":str(t),"day_of_week":str(d)}
        mydoc = mycol.find(myquery)
        for x in mydoc:
            est=est+1
        ret_obj['est']=est
        return ret_obj

api.add_resource(Video, "/")
if __name__ == "__main__":
    app.run(debug=True)