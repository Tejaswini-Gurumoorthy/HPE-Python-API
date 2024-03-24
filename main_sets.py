from flask import Flask
from flask_restful import Api, Resource
import csv

app= Flask(__name__)
api= Api(app)


class CountSets(Resource):
    def get(self, timestamp, optional_timestamp=None):
        unique_requests = set()
        if optional_timestamp is None:
            with open("hn_logs.tsv") as file:
                tsv_file = csv.reader(file, delimiter='\t')
                for line in tsv_file:
                    if timestamp in line[0]:
                        unique_requests.add(line[1])
        else:
            if len(timestamp) != 19 or len(optional_timestamp) != 19:
                print('Incorrect format of timestamp.')
            elif timestamp > optional_timestamp:
                print('Start and end timestamps are invalid.')
            else:
                with open("hn_logs.tsv") as file:
                    tsv_file = csv.reader(file, delimiter='\t')
                    for line in tsv_file:
                        if timestamp <= line[0] <= optional_timestamp:
                            unique_requests.add(line[1])
        
        count = len(unique_requests)
        return {"data": count}

api.add_resource(CountSets, "/countsets/<string:timestamp>/", "/countsets/<string:timestamp>/<string:optional_timestamp>")


if __name__ == "__main__":
    app.run(debug=True)
