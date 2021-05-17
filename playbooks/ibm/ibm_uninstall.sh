kubectl delete -f https://operatorhub.io/install/ibmcloud-operator.yaml
curl -sL https://raw.githubusercontent.com/IBM/cloud-operators/master/hack/configure-operator.sh | bash -s -- remove
