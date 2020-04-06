#I refered below web site when I code for uploading files. 
#http://blog.kzfmix.com/entry/1311764119
from flask import Flask, request, url_for, render_template, make_response
#import os
from predict_breed_savedmodel import dog_breed_resemble_human_detector
from PIL import Image  

#debug memo: I can choose to save file and delete the file.
#UPLOAD_FOLDER = 'data'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config.from_object(__name__)

def allowed_file(filename):
    #return True or False, if the extentions allowed or not.
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/')
def show_index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def do_upload():
    file = request.files['xhr2upload']
    img = Image.open(file.stream).convert('RGB')
    print(img)
    if file and allowed_file(file.filename):
#        filename = file.filename
# debug memo: choose to do not save file.
#       file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        result_msg = dog_breed_resemble_human_detector(img)
        response = make_response(result_msg)
        response.headers['Access-Control-Allow-Origin'] = '*'
# debug memo: delete the image file from server
#    os.remove(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    return response

#-------file upload end--------------
def main():
    app.run(host='0.0.0.0', port=3001, debug=True)

if __name__ == '__main__':
    main()