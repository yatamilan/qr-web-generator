# QR Code Generator Web App

A simple web application built with **Flask**, **HTML/CSS**, and **Python** to generate QR codes from user input. Users can enter a name and website/info, and the app generates a downloadable QR code in real-time.

---

## 🚀 Features

- QR code generation using Python and the `qrcode` library
- Clean and modern UI with HTML/CSS
- Real-time QR rendering (embedded using base64)
- Simple and lightweight — ideal for learning projects

---

## 📸 Demo

![demo](https://user-images.githubusercontent.com/yourusername/demo.png)
> *(Add your own screenshot after uploading to GitHub)*

---

## 🛠️ Technologies Used

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Python, Flask
- **QR Library**: `qrcode` with Pillow

---

## 📂 Project Structure

#🧰 Python Libraries Required
##Your project depends on the following libraries:
| Library  | Purpose                               |
| -------- | ------------------------------------- |
| `flask`  | Web framework for Python              |
| `qrcode` | To generate QR codes                  |
| `pillow` | Image processing backend for `qrcode` |

qr-gen-webapp/
├── app.py
├── templates/
│ └── index.html
└── README.md

---

## 🧑‍💻 Getting Started

### Prerequisites

- Python 3.x
- pip

### Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/qr-gen-webapp.git
cd qr-gen-webapp

# Install dependencies
pip install flask qrcode[pil]

# Run the app
python app.py
```
Then open your browser and go to: http://127.0.0.1:5000

📜 License
This project is open-source and available under the MIT License.

🙌 Acknowledgments
Flask

qrcode Python package

