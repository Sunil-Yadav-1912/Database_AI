from vanna.chromadb import ChromaDB_VectorStore
from vanna.google import GoogleGeminiChat
class MyVanna(ChromaDB_VectorStore, GoogleGeminiChat):
    def __init__(self, config=None):
        ChromaDB_VectorStore.__init__(self, config=config)
        GoogleGeminiChat.__init__(self, config={'api_key': 'AIzaSyAlEoLbvOCy87ETAQghcmL-DTXsfE0Hd8A',
                                                'model': "gemini-1.5-flash"})




    # @app.route('/api/v0/remove_all_training_data', methods=['POST'])
    # def remove_all_training_data():

    #     try :
    #         bool = vn.remove_collection(collection_name="sql")
    #         bool = vn.remove_collection(collection_name="ddl")
    #         bool = vn.remove_collection(collection_name="documentation")
    #     except Exception as e:
    #         print("ERASING ERROR", e)
    #         return jsonify({"type": "error", "error": str(e)})
    #     if bool:
    #         return jsonify({"success": True})
    #     else:
    #         return jsonify({"type": "error", "error": "Couldn't remove training data"})

        
    # @app.route('/api/v0/train', methods=['POST'])
    # def add_training_data():
    #     # question = flask.request.json.get('question')
    #     # sql = flask.request.json.get('sql')
    #     # ddl = flask.request.json.get('ddl')
    #     # documentation = flask.request.json.get('documentation')
    #     # print(training_data)
    #     # Iterate over each row in the DataFrame

    #     try:
    #         training_data = pd.read_csv(r"vanna training data - Sheet1.csv")
    #         for index, row in training_data.iterrows():
    #             if row['training_data_type'] == 'ddl':
    #                 vn.train(ddl=row['content'])
    #             elif row['training_data_type'] == 'documentation':
    #                 vn.train(documentation=row['content'])
    #             elif row['training_data_type'] == 'sql':
    #                 if row['question'] != 'empty':
    #                     vn.train(
    #                         question=row['question'],
    #                         sql=row['content'])
    #                 else:
    #                     vn.train(sql=row['content'])
    #         # id = vn.train(question=question, sql=sql, ddl=ddl, documentation=documentation)
    #         return jsonify({"response": "true"})
    #     except Exception as e:
    #         print("TRAINING ERROR", e)
    #         return jsonify({"type": "error", "error": str(e)})