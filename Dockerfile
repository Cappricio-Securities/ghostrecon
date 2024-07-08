# Use the official Ubuntu LTS image as the base image
FROM ubuntu:latest

# Avoid prompts during installation
ENV DEBIAN_FRONTEND=noninteractive

# Update packages and install necessary tools
RUN apt-get update && \
    apt-get install -y sudo \
                       nodejs \
                       npm

# Install sudo and create a new user 'deamon'
RUN useradd -m -s /bin/bash deamon

# Set the password for the 'deamon' user
RUN echo 'deamon:ghostrecon' | chpasswd

# Add 'deamon' to the sudoers file with no password requirement for sudo commands
RUN echo 'deamon ALL=(ALL:ALL) NOPASSWD:ALL' > /etc/sudoers.d/deamon

# Set the working directory
WORKDIR /app

# Change ownership of the working directory to the new user
RUN chown -R deamon:deamon /app

# Switch to the new user
USER deamon

# Copy the application files
COPY . .



# Make setup.sh and install.sh executable (if needed)
RUN sudo chmod +x /app/setup.sh
RUN sudo chmod +x /app/install.sh

# Run setup.sh and install.sh with non-interactive flags
RUN /app/setup.sh -y \
    || true  # Continue even if setup.sh returns a non-zero exit code

RUN /app/install.sh -y \
    || true  # Continue even if install.sh returns a non-zero exit code

# Install dependencies and start the application as 'deamon' user
RUN npm install || true

# Command to run the application
# CMD ["npm", "start"]
