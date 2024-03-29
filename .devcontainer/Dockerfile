# See here for image contents: https://github.com/microsoft/vscode-dev-containers/blob/v0.191.0/containers/python-3/.devcontainer/base.Dockerfile
# [Choice] Python version: 3, 3.9, 3.8, 3.7, 3.6
ARG VARIANT="3"
FROM mcr.microsoft.com/vscode/devcontainers/python:0-${VARIANT}

# [Optional] Allow the vscode user to pip install globally w/o sudo
ENV PIP_TARGET=/usr/local/pip-global
ENV PYTHONPATH=${PIP_TARGET}:${PYTHONPATH}
ENV PATH=${PIP_TARGET}/bin:${PATH}
RUN if ! cat /etc/group | grep -e "^pip-global:" > /dev/null 2>&1; then groupadd -r pip-global; fi \
    && usermod -a -G pip-global vscode \
    && umask 0002 && mkdir -p ${PIP_TARGET} \
    && chown :pip-global ${PIP_TARGET} \
    && ( [ ! -f "/etc/profile.d/00-restore-env.sh" ] || sed -i -e "s/export PATH=/export PATH=\/usr\/local\/pip-global:/" /etc/profile.d/00-restore-env.sh )

# [Choice] Node.js version: none, lts/*, 16, 14, 12, 10
ARG NODE_VERSION="none"
RUN if [ "${NODE_VERSION}" != "none" ]; then su vscode -c "umask 0002 && . /usr/local/share/nvm/nvm.sh && nvm install ${NODE_VERSION} 2>&1"; fi

# [Optional] If your pip requirements rarely change, uncomment this section to add them to the image.
# COPY requirements.txt /tmp/pip-tmp/
# RUN pip3 --disable-pip-version-check --no-cache-dir install -r /tmp/pip-tmp/requirements.txt \
#    && rm -rf /tmp/pip-tmp

# [Optional] Uncomment this section to install additional OS packages.
RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get -y install --no-install-recommends peco

# [Optional] Uncomment this line to install global node packages.
# RUN su vscode -c "source /usr/local/share/nvm/nvm.sh && npm install -g <your-package-here>" 2>&1


#
# Customize
#

# Install Prezto. (zsh framework)
RUN su vscode -c "git clone --recursive \
    https://github.com/sorin-ionescu/prezto.git \
    /home/vscode/.zprezto"
RUN su vscode -c "ln -s -f /home/vscode/.zprezto/runcoms/zlogin /home/vscode/.zlogin \
    && ln -s -f /home/vscode/.zprezto/runcoms/zlogout /home/vscode/.zlogout \
    && ln -s -f /home/vscode/.zprezto/runcoms/zpreztorc /home/vscode/.zpreztorc \
    && ln -s -f /home/vscode/.zprezto/runcoms/zprofile /home/vscode/.zprofile \
    && ln -s -f /home/vscode/.zprezto/runcoms/zshenv /home/vscode/.zshenv \
    && ln -s -f /home/vscode/.zprezto/runcoms/zshrc /home/vscode/.zshrc"
ENV SHELL /usr/bin/zsh

# Change shell.
RUN sudo chsh vscode -s $(which zsh)

# Download zsh auto suggestion tool.
RUN su vscode -c "git clone https://github.com/zsh-users/zsh-autosuggestions /home/vscode/.zsh/zsh-autosuggestions"

# Copy dotfiles.
COPY .devcontainer/dotfiles/* /home/vscode
