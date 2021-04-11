# k8s_Ingress_PythonFlaskMicrosites
k8s Ingress setup using Python Flask Apps using Postgres database.
Create a Postgres Pod 
Create an app named Form to add users to Postres db
Create an app named Users to display users from Postgres db
Set the apps as microsites using an ingress with urls **<ip_address>/form** and **<ip_address>/users**

# Setup Postgres Pod
kubectl create -f postgres.yaml

# Setup Postgres Service
kubectl expose pod postgres --type ClusterIP --port 5432 --target-port 5432

# Create database, user and tables
kubectl exec -it postgres -- bash
su postgres
psql
postgres=# CREATE DATABASE users;
CREATE DATABASE
postgres=# CREATE USER mahesh WITH PASSWORD 'password@123';
CREATE ROLE
postgres=# GRANT ALL PRIVILEGES ON DATABASE users to mahesh;
GRANT
postgres=# \l
\dl
create table users (user_id serial PRIMARY KEY, first_name VARCHAR (50), last_name VARCHAR (50), email VARCHAR (50) NOT NULL);
\dt;

If you need to push the custom image to your dockerhub/private docker registry, please docker login.

# To create your own docker images for App1 (Optional)
cd flaskapp1
docker build -t form .
docker push <dockerhubuserid>form:latest
  
# To create your own docker images for App2 (Optional)
cd flaskapp2
docker build -t users .
docker push <dockerhubuserid>users:latest
  
# Create pods for app1 and app2
kubectl create -f form.yaml
kubectl create -f users.yaml

# Create services for app1 and app2
kubectl expose pod form --name form --type NodePort --port 5003 --target-port 5003
kubectl expose pod users --name users --type NodePort --port 5003 --target-port 5003

# Create Ingress
kubectl create -f ingress.yaml
