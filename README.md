# MultiCloud Management
Multi-cloud/Multi-operator management framework in kubernetes

Environment details:

Development Environment:
Platform: MacOSX
Language: Python 3.7.4

Supported OS:
Project uses below external python packages. Apologies for not maintaining a requirements file.
You can pip install below external packages.

Flask==1.1.2
PyYAML==5.3.1
PyMySQL==0.10.1
kubernetes==17.17.0

Below are the operations supported and respective REST APIs.
Operator install commands can be referred from operator hub.
This creation and installation does not include setup of preconditions. User has to setup requirements by referring to operator hub website.

Operators management

1. Create:

URL: http://127.0.0.1:5000/operator
METHOD: POST
Headers: {content-type: application/json}
Json Body (with example):

{"name":"ibm",
 "install_commands": ["curl -sL https://raw.githubusercontent.com/IBM-Cloud/ibm-cloud-developer-tools/master/linux-installer/idt-installer | bash",
              "ibmcloud login -u 'kaustud1@umbc.edu' -p 'Ibm@bhstukau235' -r 'us-east'", 
                      "ibmcloud target -g Default -r us-east", 
                      "curl -sL https://raw.githubusercontent.com/IBM/cloud-operators/master/hack/configure-operator.sh | bash -s -- install", "kubectl create -f https://operatorhub.io/install/ibmcloud-operator.yaml"],
 "uninstall_commands": ["kubectl delete -f https://operatorhub.io/install/ibmcloud-operator.yaml",
                        "curl -sL https://raw.githubusercontent.com/IBM/cloud-operators/master/hack/configure-operator.sh | bash -s -- remove"],
 "link": "https://operatorhub.io/operator/ibmcloud-operator"
}

2. Get

URL: http://127.0.0.1:5000/operator/<name>
METHOD: GET
Example: URL: http://127.0.0.1:5000/operator/ibm

3. Install

URL: http://127.0.0.1:5000/operator/install/<name>
METHOD: POST
Example: URL: http://127.0.0.1:5000/operator/install/ibm

4. Uninstall

URL: http://127.0.0.1:5000/operator/uninstall/<name>
METHOD: GET
EXAMPLE: URL: http://127.0.0.1:5000/operator/uninstall/ibm

5. Delete

URL: http://127.0.0.1:5000/operator/<name>
METHOD: DELETE
Example URl: http://127.0.0.1:5000/operator/ibm


Example command to check if an operator is installed:
> kubectl api-resources | grep ibm



Resource Management

1.  Create:

URL: http://127.0.0.1:5000/resource
METHOD: POST
Headers: {content-type: application/json}
Example JSON body:
{
  "apiVersion": "ibmcloud.ibm.com/v1",
  "kind": "Service",
  "metadata": {
    "annotations": {
      "ibmcloud.ibm.com/self-healing": "enabled"
    },
    "name": "demo"
  },
  "spec": {
    "plan": "lite",
    "serviceClass": "language-translator"
  }
}


2. Get:

URL: http://127.0.0.1:5000/resource/<name>
METHOD: GET
Example: http://127.0.0.1:5000/resource/demo

3. Deploy:

URL: http://127.0.0.1:5000/resource/deploy
METHOD: POST
Example JSON Body:
{"name": "demo"}

4. DELETE

URL: http://127.0.0.1:5000/resource/<name>
METHOD: DELETE
Example URL: http://127.0.0.1:5000/resource/demo
