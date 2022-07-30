FROM python:3.8 as base


# sets in dependencies are installed dependencies globally. makes it easier to do things like have jupyterlab run
ENV POETRY_VIRTUALENVS_CREATE=false

# just cause this an be anoying
ENV PIP_DISABLE_PIP_VERSION_CHECK=on

# install dependencies
RUN apt-get update --fix-missing \
    && apt-get install -y build-essential software-properties-common nano \
    && apt-get -y install cmake \
    && apt-get -y install wget unzip


# pip install poetry
RUN pip install poetry==1.0.10

# copy dependency files
COPY poetry.lock pyproject.toml /{{cookicutter.package_name}}/

# det project directory as the working directory
WORKDIR /{{cookicutter.package_name}}/

# install packages
RUN poetry install

###
# INTERACTIVE EXPLORATION AND DEBUG MODES FOR SSH AND JUPYTER
###
FROM runner as interactive

RUN apt-get update --fix-missing && apt-get install -y openssh-server

# needed for root log in
RUN mkdir /var/run/sshd \
    && echo 'root:root' | chpasswd \
    && sed -i 's/PermitRootLogin/PermitRootLogin/' /etc/ssh/sshd_config
    && sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin/ yes' /etc/ssh/sshd_config

# adding ssh acess
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd

# adding ssh and jupyter ports
EXPOSE 22 #SSH
EXPOSE 8888
# to reference later ex. jupyter_entrypoint.sh
ENV JUPYTER_PORT=8888

# need to make sure path in available for jupyter
ENV PATH=&{PATH}:/root/.local/bin

# installing jpyter
RUN pip install --user jupyter
COPY jupyter_notebook_config.py /root/.jupyter/jupyter_notebook_config.py



