# 🌟 E-KYC Egyptian National ID App 🌟

Welcome to the E-KYC Egyptian National ID App repository! This project simulates an e-KYC (Electronic Know Your Customer) feature for an e-payment app, inspired by the Egyptian company Al Ahly Momken. Our main focus is on the OCR (Optical Character Recognition) part.

## 📂 Repository Link

[GitHub Repository](https://github.com/yassinmohamed111/E-KYC_Egyptian_National_id)

## 🚀 Project Overview

This app is built using Flutter for the front-end and integrates with a Flask API to handle OCR tasks. The project has three main phases: Integration, AI Model, and OCR.

## 🌟 Features

1. **Integration with Flutter App**:
    - 🛠️ **Flask Server**: Connects the Flutter app with Python files.
    - 🌐 **Ngrok Tunneling**: Makes the local server accessible over the internet.
    - 📸 **HTTP POST Requests**: Flutter app sends ID images to the Flask server for OCR processing.

2. **AI Model**:
    - 🤖 **Yolov8 Models**:
        - Detects if the image is an Egyptian ID.
        - Extracts Arabic numbers from the ID.
    - ✂️ **Image Cropping**: Extracts valuable information and crops it into separate fields.

3. **OCR Processing**:
    - 📏 **Bounding Boxes**: Crops ID fields after detecting data.
    - 🎨 **Image Preprocessing**: Enhances readability for OCR.
    - 🔍 **Pre-trained OCR Models**: Uses TesseractOCR and ArabicOCR to extract text.

4. **Data Handling**:
    - 📄 **JSON Response**: Sends extracted data back in JSON format.
    - Possible responses:
        1. 🚫 Not an Egyptian ID.
        2. 📵 ID is unclear, request to retake the image.
        3. ✅ ID is valid, extracted data returned.

## 📖 Getting Started

### Prerequisites

- Flutter SDK
- Python 3.7+
- Flask
- Ngrok
- Yolov8
- TesseractOCR
- ArabicOCR

### Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yassinmohamed111/E-KYC_Egyptian_National_id.git
    cd E-KYC_Egyptian_National_id
    ```

2. **Set up Flask server**:
    - Navigate to the `server` directory.
    - Install required Python packages:
      ```bash
      pip install -r requirements.txt
      ```
    - Start the Flask server:
      ```bash
      python app.py
      ```

3. **Set up Ngrok**:
    - Start Ngrok to tunnel your Flask server:
      ```bash
      ngrok http 5000
      ```
    - Note the forwarding URL provided by Ngrok.

4. **Configure Flutter app**:
    - Update the server URL in the Flutter app to the Ngrok forwarding URL.

5. **Run the Flutter app**:
    - Navigate to the `flutter_app` directory.
    - Run the app using Flutter:
      ```bash
      flutter run
      ```

## 📲 Usage

1. Open the Flutter app and follow the prompts to capture an image of the Egyptian ID.
2. The image is sent to the Flask server for OCR processing.
3. The server returns the extracted data in JSON format, which is then displayed in the app.

## 🤝 Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 📬 Contact

For any questions or inquiries, please contact me at yassinmohamed022@gmail.com .

---

Thank you for using the E-KYC Egyptian National ID App! We hope this project helps you understand the integration of OCR with Flutter and Flask. 🎉
