# Use ROCm enabled base image
FROM rocm/dev-ubuntu-22.04:5.4.2

# Install required tools and libraries
RUN apt-get update && apt-get install -y \
    cmake \
    golang \
    libclblast-dev \
    rocm-dev \
    git

# Set environment variables to specify ROCm and CLBlast paths
ENV ROCM_PATH=/opt/rocm
ENV CLBlast_DIR=/usr/lib/cmake/CLBlast

# Set up working directory
WORKDIR /ollama

# Copy the Ollama source code into the container
RUN git clone --depth 1 -b v0.1.43 https://github.com/ollama/ollama.git
RUN cd ollama
RUN go generate ./...
RUN go build .
