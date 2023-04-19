# Define as variáveis para o cluster
CLUSTER_NAME="meu-cluster"
NUM_NODES="3"
MACHINE_TYPE="n1-standard-2"
REGION="us-central1"
ZONE="us-central1-a"

# Cria o cluster
gcloud container clusters create $CLUSTER_NAME \
    --num-nodes=$NUM_NODES \
    --machine-type=$MACHINE_TYPE \
    --region=$REGION \
    --zone=$ZONE

# Autentica o kubectl com o cluster
gcloud container clusters get-credentials $CLUSTER_NAME \
    --region $REGION \
    --zone $ZONE

# Verifica se a autenticação foi bem sucedida
kubectl get nodes
