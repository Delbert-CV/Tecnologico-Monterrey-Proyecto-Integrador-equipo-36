### Proyecto Integrado - Equipo #36
# La finalidad de este script es la de descargar, por medio de HuggingFace, algunos LLMs
# los cuales podrían funcionar para llevar a cabo el fine-tuning para que el ChatBot a llevar
# a cabo pueda responder preguntas con base en nuestro dataset proporcionado por la CNIT.
#
# Algunos de los modelos presentados en este script se consideran como "gated", lo que significa
# que es necesario aceptar los términos y condiciones del publisher del modelo para
# descargar y hacer uso del mismo.
###



# Importamos las libresrías de Hugging-Face
from huggingface_hub import snapshot_download
from huggingface_hub import login
import os

# Cargamos la variable de entorno para autenticarnos en HugggingFace
# Este token se puede generar desde https://huggingface.co/settings/tokens al tener una cuenta vigente.

hf_auth_token = os.getenv("hf_auth")
login(token=hf_auth_token)


# Modelo Mistral-7B-Instruct-V0.3
# Disponible en https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.3

# local_dir = snapshot_download(
#     repo_id="mistralai/Mistral-7B-Instruct-v0.3",
#     local_dir="D:/LLM Models/Mistral7B",
#     local_dir_use_symlinks=False
# )

# ModeloTheBloke/MythoMax-L2-13B-GPTQ
# Disponible en https://huggingface.co/TheBloke/MythoMax-L2-13B-GPTQ
# local_dir = snapshot_download(
#     repo_id="TheBloke/MythoMax-L2-13B-GPTQ",
#     local_dir="D:/LLM Models/TheBlokeMythoMax-L2-13B-GPTQ",
#     local_dir_use_symlinks=False
# )

# Modelo meta-llama/Meta-Llama-3-8B
# Disponible en https://huggingface.co/meta-llama/Meta-Llama-3-8B
# local_dir = snapshot_download(
#     repo_id="meta-llama/Meta-Llama-3-8B",
#     local_dir="D:/LLM Models/meta-llamaMeta-Llama-3-8B",
#     local_dir_use_symlinks=False
# )


# Modelo microsoft/Phi-3-mini-4k-instruct
# Disponible en https://huggingface.co/microsoft/Phi-3-mini-4k-instruct

local_dir = snapshot_download(
    repo_id="microsoft/Phi-3-mini-4k-instruct",
    local_dir="D:/LLM Models/microsoft-phi-3-mini-4k-instruct",
    local_dir_use_symlinks=False
)


##########################################################################
# Unsloth es una libreria que funciona para que algunos modelos puedan
# converger o funcionar de forma más rápida. Requiere de algunos métodos
# más para cargar, procesar y hacer trabajar a los modelos.
##########################################################################

# Modelo unsloth/mistral-7b-bnb-4bit
# Disponible en https://huggingface.co/unsloth/mistral-7b-bnb-4bit
# Nota importante: el uso de Unsloth complica un poco todo lo relacionado al uso del modelo.
# Por lo tanto, sugerimos leer la documentación de Unsloth.

# local_dir = snapshot_download(
#     repo_id="unsloth/mistral-7b-bnb-4bit",
#     local_dir="D:/LLM Models/unsloth-mistral-7b-bnb-4bit",
#     local_dir_use_symlinks=False
# )

# Modelo unsloth/mistral-7b-instruct-v0.2-bnb-4bit
# Disponible en https://huggingface.co/unsloth/mistral-7b-instruct-v0.2-bnb-4bit
# local_dir = snapshot_download(
#     repo_id="unsloth/mistral-7b-instruct-v0.2-bnb-4bit",
#     local_dir="D:/LLM Models/unsloth-mistral-7b-instruct-v0.2-bnb-4bit",
#     local_dir_use_symlinks=False
# )



print(local_dir)