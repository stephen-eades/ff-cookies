# ff-cookies

## Configuring the Server
1. Install Required Packages:
- `sudo apt update`
- `sudo apt install python3-pip python3-venv`

2. Create a Virtual Environment and Install Flask and Flask-cors:
- `python3 -m venv ff-cookies`
- `source ff-cookies/bin/activate`
- `pip install Flask requests`
- `pip install flask-cors`

3. Run the Flask App
- `python app.py`

4. Ensure the port is open
- `sudo ufw allow 5000/tcp`

5. Check if host machine can reach server
- `curl http://your_server_ip_here:5000`  

6. Configure Nginx as a Reverse Proxy (Optional):

**/etc/nginx/sites-available/myflaskapp**

`server {
    listen 80;
    server_name your_domain_or_IP;
    location / {
        proxy_pass http://127.0.0.1:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}`

- `sudo ln -s /etc/nginx/sites-available/myflaskapp /etc/nginx/sites-enabled`
- `sudo nginx -t`
- `sudo systemctl restart nginx`

## Accessing the Server
1. Login to the server (credentials required)
2. Navigate to `/home/xyz_admin/`
3. Activate the virtual environment: `source ff-cookies/bin/activate`
4. Navigate to `/home/repos/ff-cookies/`
5. Star the server: `python3 app.py`

## Setup the Server to Run as a Service
1. Create a systemd Service File: `sudo nano /etc/systemd/system/flaskapp.service`
2. Add the following code to the flaskapp.service file you just made:
   
`[Unit]
Description=Flask Application
After=network.target
[Service]
User=yourusername
WorkingDirectory=/path/to/your/flaskapp
ExecStart=/usr/bin/python3 /path/to/your/flaskapp/app.py
Restart=always
[Install]
WantedBy=multi-user.target`

3. Reload systemd and Start the Service
- `sudo systemctl daemon-reload`
- `sudo systemctl start flaskapp.service`
- `sudo systemctl enable flaskapp.service`

4. Check the Status of the Service: `sudo systemctl status flaskapp.service`
5. Need to debug? Use: `journalctl -u flaskapp.service -b`
