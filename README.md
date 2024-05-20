# ff-cookies

1. Install Required Packages:
- `sudo apt update`
- `sudo apt install python3-pip python3-venv`

2. Create a Virtual Environment and Install Flask:
- `python3 -m venv ff-cookies`
- `source ff-cookies/bin/activate`
- `pip install Flask requests`

3. Run the Flask App
- `python app.py

4. Configure Nginx as a Reverse Proxy (Optional):

`/etc/nginx/sites-available/myflaskapp`

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
