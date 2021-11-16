.\install_flask.ps1 Y python -m pip install flask

.\run.ps1
Y
$Env:FLASK_APP = "server.py"
python -m flask run -h 0.0.0.0 -p 12345