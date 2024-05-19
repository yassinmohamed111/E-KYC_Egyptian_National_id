from flask import Flask, jsonify,jsonify, request
from run import get_ocr , get_id_for_super_app
import os


app = Flask(__name__)




@app.route('/login_id', methods=['POST'])
def login_super():
    
    if 'file' not in request.files:
        return jsonify({'error': 'No file part in the request'}), 400
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    
    file.save(r'C:\Users\yassi\Desktop\my_ocr\id.jpg')

    
    ocr_data = get_id_for_super_app()
    #upload_data(ocr_data)
    return jsonify({'status': 'success', 'ocr_data': ocr_data})





@app.route('/flutter', methods=['POST'])
def flutter_image():
    
    if 'file' not in request.files:
        return jsonify({'error': 'No file part in the request'}), 400
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    
    file.save(r'C:\Users\yassi\Desktop\my_ocr\id.jpg')
   
    
    ocr_data = get_ocr()
    return jsonify({'status': 'success', 'ocr_data': ocr_data})





if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)






