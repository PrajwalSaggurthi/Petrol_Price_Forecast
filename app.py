from flask import *
import pickle

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('base.html')




@app.route('/result', methods=['GET'])
def result():
    data = request.args.get('data')
    data = str(data)
    data = data.split('-')
    string=''
    for i in data:
        string+=i
    modelgnb=pickle.load(open('modelgnb.pkl','rb'))
    modellogic = pickle.load(open('modellogic.pkl','rb'))
    modellr=pickle.load(open('modellr.pkl','rb'))
    modelrfc=pickle.load(open('modelrfc.pkl','rb'))
    gnb=str(modelgnb.predict([[int(string)]]))
    log=str(modellogic.predict([[int(string)]]))
    lr=str(modellr.predict([[int(string)]]))
    rfc=str(modelrfc.predict([[int(string)]]))
    return render_template('result.html',gnb=gnb,log=log,lr=lr,rfc=rfc)

if __name__ == '__main__':
    app.run(debug=False)
