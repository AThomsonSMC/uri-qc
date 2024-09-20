FROM mcr.microsoft.com/devcontainers/python:1-3.12-bookworm

# to listen to jypterlab
EXPOSE 8888

# install dependencies
RUN pip install \
    ipykernel \
    jupyterlab \
    qiskit-ibm-runtime \
    qiskit[visualization] \
    && rm -rf /root/.cache/pip/*

# switch to non-root user
USER vscode