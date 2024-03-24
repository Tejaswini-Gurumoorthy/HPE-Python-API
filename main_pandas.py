from flask import Flask
from flask_restful import Api, Resource
import pandas as pd

app= Flask(__name__)
api= Api(app)

column_names= ["timestamp", "request"]
df= pd.read_csv('hn_logs.tsv', sep='\t', engine='python', names=column_names)

class CountPandas(Resource):
    def get(self, timestamp, optional_timestamp=None):
        count=0
        if optional_timestamp is None: 
            filtered_df= df[df['timestamp'].str.contains(timestamp)]
            count= filtered_df['request'].nunique()

        
        else:
            if len(timestamp)!= 19 or len(optional_timestamp)!=19:
                print('Incorrect format of timestamp.')
            elif timestamp > optional_timestamp:
                print('Start and end timestamps are invalid.')
            else:
                filtered_df = df[(df['timestamp'] >= timestamp) & (df['timestamp'] <= optional_timestamp)]
                count= filtered_df['request'].nunique()

        return {"count":count}

api.add_resource(CountPandas, "/countpandas/<string:timestamp>/", "/countpandas/<string:timestamp>/<string:optional_timestamp>")

if __name__ == "__main__":
    app.run(debug=True)
