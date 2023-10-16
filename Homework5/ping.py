from flask import Flask

app = Flask('ping')

@app.route('/ping', methods = ['GET'])
def ping():
    print("LLLL")



print("ldkldshdlh")

if __name__ =="__main__":
    app.run(debug=True, host = '0.0.0.0', port=9696)

