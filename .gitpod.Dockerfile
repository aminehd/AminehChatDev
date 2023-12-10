FROM gitpod/workspace-full:latest

# RUN sudo apt-get update && apt-get install -y wget
RUN sudo apt-get install libgl1-mesa-glx libegl1-mesa libxrandr2 libxrandr2 libxss1 libxcursor1 libxcomposite1 libasound2 libxi6 libxtst6 -y
RUN curl -o  ~/Anaconda3-2023.11.0-Linux-x86_64.sh https://repo.anaconda.com/archive/Anaconda3-2023.09-0-Linux-x86_64.sh 

RUN bash ~/Anaconda3-2023.11.0-Linux-x86_64.sh -b -u



# # Add conda to terminal
# For Bash
RUN echo "source ~/anaconda3/bin/activate" >> ~/.bashrc

# RUN echo "conda activate base" >> ~/.bashrc

# # For Zsh
# RUN echo ". /root/miniconda3/etc/profile.d/conda.sh" >> ~/.zshrc
# RUN echo "conda activate base" >> ~/.zshrc


# # Set the default shell to bash
# SHELL ["/bin/bash", "-c"]

# # Any other commands you want to include
