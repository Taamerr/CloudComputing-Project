#!bin/bash
kubectl apply -f Deployment.yml
kubectl wait --for=condition=available deployment/our-app
kubectl port-forward deployment/our-app 4000:4000 8080:8080 5000:5000 3000:3000