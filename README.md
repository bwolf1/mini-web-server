# Setting up systemd

```
sudo cp testserver.service /lib/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable testserver.service
```

# Starting the server

```bash
sudo systemctl start testserver.service
```


# Stopping the server

```bash
sudo systemctl stop testserver.service
```

# More

```bash
man systemctl
```
