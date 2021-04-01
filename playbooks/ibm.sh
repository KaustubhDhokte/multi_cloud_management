# Install CLI
curl -sL https://raw.githubusercontent.com/IBM-Cloud/ibm-cloud-developer-tools/master/linux-installer/idt-installer | bash
ibmcloud login -u "kaustud1@umbc.edu" -p "Ibm@bhstukau235" -r "us-east"
ibmcloud target -g Default -r us-east
curl -sL https://raw.githubusercontent.com/IBM/cloud-operators/master/hack/configure-operator.sh | bash -s -- install
kubectl create -f https://operatorhub.io/install/ibmcloud-operator.yaml